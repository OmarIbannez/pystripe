import stripe
from django.conf import settings
stripe.api_key = settings.STRIPE_API_KEY

plan = stripe.Plan.retrieve("basic")

print(plan)
