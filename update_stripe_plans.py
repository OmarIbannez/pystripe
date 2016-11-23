import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
import stripe
from django.conf import settings
from payments.models import Plan


stripe.api_key = settings.STRIPE_API_KEY
stripe_plans = stripe.Plan.list(limit=3)

for stripe_plan in stripe_plans.data:
    defaults = {
        'amount': stripe_plan.amount,
        'currency': stripe_plan.currency,
        'plan_id': stripe_plan.id,
        'interval': stripe_plan.interval,
        'interval_count': stripe_plan.interval_count,
        'livemode': stripe_plan.livemode,
        'name': stripe_plan.name,
        'trial_period_days': stripe_plan.trial_period_days or 0,
    }
    try:
        obj = Plan.objects.get(plan_id=stripe_plan.id)
        for key, value in defaults.items():
            setattr(obj, key, value)
        obj.save()
    except Plan.DoesNotExist:
        obj = Plan(**defaults)
        obj.save()
