from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
import json
import stripe
from django.conf import settings
from core.eventmanager import EventManager


stripe.api_key = settings.STRIPE_API_KEY


class WebhokView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(WebhokView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        event_json = json.loads(request.body)
        try:
            event = stripe.Event.retrieve('evt_19J9TaJpcRKzNWIILX4TCH1f')#stripe.Event.retrieve(event_json["id"])
        except Exception as e:
            return HttpResponse(status=500)

        event_manager = EventManager(event)
        event_manager.process()

        return HttpResponse(status=200)

    def update_plan(self):
        print('UPDATED');