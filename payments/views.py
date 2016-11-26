from django.views.generic import View, TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
import json
import stripe
from django.conf import settings
from core.eventmanager import EventManager
from django.shortcuts import redirect


stripe.api_key = settings.STRIPE_API_KEY


class WebhokView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(WebhokView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        event = json.loads(request.body)

        try:
            event_manager = EventManager(event)
        except Exception as e:
            return HttpResponse(status=500)

        try:
            event_manager.process()
        except Exception as e:
            return HttpResponse(status=500)

        return HttpResponse(status=200)


class AddCreditCard(TemplateView):
    template_name = 'add_credit_card.html'


@csrf_exempt
def create_suscription(request):
    if request.method == 'POST':
        stripe_token = request.POST['stripeToken']
        customer = stripe.Customer.create(
            description="Customer for " + request.user.email,
            source=stripe_token
        )

        stripe.Subscription.create(
            customer=customer.id,
            plan=request.user.plan.plan_id
        )

        request.user.stripe_customer_id = customer.id
        request.user.save()

        return redirect('/dashboard/')

    return redirect('/add_credit_card/')
