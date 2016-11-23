import stripe
from django.conf import settings
stripe.api_key = settings.STRIPE_API_KEY


stripe.Plan.create(
    amount=500,
    interval="month",
    name="Amazing Basic Plan",
    currency="usd",
    id="basic",
    trial_period_days=30
)
