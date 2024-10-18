from django.shortcuts import render

import stripe
import djstripe
from djstripe.models import Product, Price
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.conf import settings 

@method_decorator(login_required, name='dispatch')
class CheckoutView(TemplateView):
    template_name = "subscription/checkout.html"

    def get_context_data(self, **kwargs):
        products = Product.objects.all()
        context = super(CheckoutView, self).get_context_data(**kwargs)
        context.update({
            "products": products,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_TEST_PUBLIC_KEY
        })
        return context

import json  #add this
from django.http import JsonResponse  # add this 


@method_decorator(login_required, name='dispatch')
class StripeIntentView(View):
    def post(self, request, *args, **kwargs):
        try:

            data = json.loads(request.body)
            print(data)
            payment_method = data['payment_method']

            payment_method_obj = stripe.PaymentMethod.retrieve(payment_method)
            djstripe.models.PaymentMethod.sync_from_stripe_data(payment_method_obj)

        # This creates a new Customer and attaches the PaymentMethod in one API call.
            customer = stripe.Customer.create(
                payment_method=payment_method,
                email=request.user.email,
                invoice_settings={
                    'default_payment_method': payment_method
                }
              )

            djstripe_customer = djstripe.models.Customer.sync_from_stripe_data(customer)
            request.user.customer = djstripe_customer
         

          # At this point, associate the ID of the Customer object with your
          # own internal representation of a customer, if you have one.
          # print(customer)

          # Subscribe the user to the subscription created
            subscription = stripe.Subscription.create(
                customer=customer.id,
                items=[
                    {
                      "price": data["price_id"],
                    },
                ],
                expand=["latest_invoice.payment_intent"]
              )

            djstripe_subscription = djstripe.models.Subscription.sync_from_stripe_data(subscription)

            request.user.subscription = djstripe_subscription
            request.user.customer = djstripe_customer
            user=request.user.save()
            prinr(user)
          
            # creating the intent
            price = Price.objects.get(id=self.kwargs["pk"])
            intent = stripe.PaymentIntent.create(
                amount=price.unit_amount,
                currency='usd',
                customer=customer['id'],
                description="Software development services",
                metadata={
                    "price_id": price.id
                }
            )
        


            return JsonResponse({
                'clientSecret': intent['client_secret']
            })
        except Exception as e:
            return JsonResponse({'error': str(e)})