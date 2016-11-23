from django.db import models
from core.models import BaseModel


class Plan(BaseModel):
    amount = models.IntegerField()
    currency = models.CharField(max_length=10, blank=False, null=False)
    plan_id = models.CharField(max_length=255, blank=False, null=False)
    interval = models.CharField(max_length=10, blank=True, null=True)
    interval_count = models.IntegerField(null=False)
    livemode = models.BooleanField(blank=False, default=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    trial_period_days = models.IntegerField(null=False)
