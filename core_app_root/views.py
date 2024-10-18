from django.shortcuts import render
from django.shortcuts import render
from djstripe.models import Product
# Create your views here.
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from djstripe.settings import djstripe_settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from djstripe.settings import djstripe_settings
from djstripe.models import Subscription
from core_app_root import base_url
import stripe
from django.views.decorators.http import require_POST

from django.conf import settings
stripe.api_key = settings.STRIPE_TEST_PRIVATE_KEY

@login_required
@require_POST
def create_portal_session(request):
    stripe.api_key = djstripe_settings.STRIPE_SECRET_KEY
    portal_session = stripe.billing_portal.Session.create(
        customer=request.user.customer.id,
        return_url=f"{base_url.backend_url}/subscription-details/",
    )
    print(portal_session)
    return HttpResponseRedirect(f"{base_url.backend_url}/subscription-confirm/?session_id={portal_session.id}")


@login_required
def subscription_confirm(request):
    # set our stripe keys up
    # print(request)
    stripe.api_key = djstripe_settings.STRIPE_SECRET_KEY

    # get the session id from the URL and retrieve the session object from Stripe
    session_id = request.GET.get("session_id")
    session = stripe.checkout.Session.retrieve(session_id)
    print(session)
    # get the subscribing user from the client_reference_id we passed in above
    client_reference_id = int(session.client_reference_id)
    subscription_holder = get_user_model().objects.get(id=client_reference_id)
    # sanity check that the logged in user is the one being updated
    assert subscription_holder == request.user

    # get the subscription object form Stripe and sync to djstripe
    subscription = stripe.Subscription.retrieve(session.subscription)
    djstripe_subscription = Subscription.sync_from_stripe_data(subscription)

    # set the subscription and customer on our user
    subscription_holder.subscription = djstripe_subscription
    subscription_holder.customer = djstripe_subscription.customer
    subscription_holder.save()

    # show a message to the user and redirect
    messages.success(request, f"You've successfully signed up. Thanks for the support!")
    return HttpResponseRedirect(reverse("subscription_details"))
def index(request):
    return render(request, "index.html")



# def pricing_page(request):
#     return render(request, 'pricing_page.html', {
#         'products': Product.objects.all()
#     })
@login_required
def pricing_page(request):
    return render(request, 'pricing_page.html',{
        'stripe_public_key': djstripe_settings.STRIPE_PUBLIC_KEY,
        'stripe_pricing_table_id': settings.STRIPE_PRICING_TABLE_ID,
    })
def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})

# @login_required
# def chat(request):
#     return TemplateResponse(request, "chat/single_chat.html")