#!/usr/bin/venv python3
from core_app_root.security.auth.serializer.passwordreset_serializers import ResetPasswordSerializer, ResetPasswordConfirmSerializer
from rest_framework.exceptions import NotFound, ValidationError, AuthenticationFailed
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from core_app_root.security.user.models import User
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from django.utils.encoding import force_bytes
from django.templatetags.static import static
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import viewsets, status
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.conf import settings
from drf_yasg import openapi

token_generator = PasswordResetTokenGenerator()

@swagger_auto_schema(
    request_body=ResetPasswordSerializer,
    responses={200: ResetPasswordSerializer}
)
class ResetPasswordViewSet(viewsets.ModelViewSet):
    
    serializer_class = ResetPasswordSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']
    
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if not serializer.is_valid():
                raise ValidationError("User input is invalid")
            email = serializer.data['email']
            user = User.objects.filter(email=email).first()
            if not user:
                raise NotFound("User not found")
            user_id = urlsafe_base64_encode(force_bytes(user.pk))
            global token_generator
            token = token_generator.make_token(user)
            current_site = get_current_site(request)
            prot = request.scheme # the request protocal
            context = {
                "Password_reset_link": f"{prot}://{current_site.domain}/passwordresetconfirm/{user_id}/{token}"
            }
            email_template_path = "/home/leorizaserver/applegenie/templates/email_templates/Forgot password/new-email.html"
            html_message = render_to_string(email_template_path, context)
            plain_message = strip_tags(html_message)
            send_mail_var = send_mail(
                subject="Password Reset: FindersKeepers",
                message=plain_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email,],
                html_message=html_message,
                fail_silently=False
            )
            print("email sent" if send_mail_var else "email not sent")
            return Response({
                "user": serializer.data,
                "email_token": token,
                "user_id": user_id,
                "is_active":True,
                "status":True,
                "success_msg":"Password reset link has been sent to your email",
                "password_reset_link": context['Password_reset_link']
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                "is_active": False,
                "status": False,
                "error_msg": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordConfirmViewSet(viewsets.ModelViewSet):
    
    serializer_class = ResetPasswordConfirmSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']
    
    def post(self, request, user_id, token, *args, **kwargs):
        try:
            if not (user_id and token):
                raise ValidationError("Broken URL")
            serializer = self.serializer_class(data=request.data)
            if not serializer.is_valid():
                raise ValidationError("User input is invalid")
            user_id = urlsafe_base64_decode(user_id).decode()
            user = User.objects.filter(pk=user_id).first()
            if not user:
                raise NotFound("User not found")
            global token_generator
            if not token_generator.check_token(user, token):
                raise AuthenticationFailed("Invalid token")
            if authenticate(request, username=user.email, password=serializer.data['old_password']):
                user.set_password(serializer.data['new_password'])
                user.save()
            else:
                raise AuthenticationFailed("Invalid password")
            return Response({
                "is_active": True,
                "status": True,
                "success_msg": "Password has been reset successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "is_active": False,
                "status": False,
                "error_msg": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)