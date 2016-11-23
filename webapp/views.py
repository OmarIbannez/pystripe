from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
import json
import stripe
from django.conf import settings


stripe.api_key = settings.STRIPE_API_KEY


class WebhokView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(WebhokView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        event_json = json.loads(request.body)
        event = stripe.Event.retrieve(event_json["id"])
        print(event)

        return HttpResponse(status=200)