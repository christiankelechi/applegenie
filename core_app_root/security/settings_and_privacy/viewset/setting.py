#!/usr/bin/env python3
from core_app_root.security.settings_and_privacy.serializers import MatchPreferenceModelSerializer, CausesModelSerializer, QualitiesValueModelSerializer, SettingPrivacyModelSerializer
from core_app_root.security.settings_and_privacy.models import MatchPreferenceModel, CausesModel, QualitiesValueModel, SettingPrivacyModel
from rest_framework import serializers, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class DisplaySettingViewSet(viewsets.ModelViewSet):
    
    serializer_class = SettingPrivacyModelSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']
    
    def get_queryset(self, *args, **kwargs):
        return SettingPrivacyModel.objects.all()
    
    def display(self, requests, *args, **kwargs):
        try:
            user = request.user
            setting = user.settingprivacymodel
            match_pre = setting.matchpreferencemodel
            cause = setting.causesmodel_set.all()
            qualities = setting.qualitiesvaluemodel_set.all()
            data = {"Email": user.email, "Settings": setting.model_details()}
            data['Settings']["Match Preference"] = match_pre.model_details()
            data['Settings']['My causes and communities'] = {i.model_details()for i in cause}
            data["Settings"]["Qualities I value"] = {i.model_details()for i in qualities}
            return Response(data, status=status.HTTP_200_OK)
        except Exceptions as e:
            return Response({'error': "User is not authenticated"},status=status.HTTP_406_NOT_ACCEPTABLE)
        
class DisplaySettingsAPIView(APIView):
    pass
    
    