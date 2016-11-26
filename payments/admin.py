from django.contrib import admin
from payments.models import Plan


class PlanAdmin(admin.ModelAdmin):
    list_display = (
        'plan_id',
        'name',
        'amount',
        'currency',
        'interval',
        'interval_count',
        'trial_period_days',
        'deleted',
    )

admin.site.register(Plan, PlanAdmin)
