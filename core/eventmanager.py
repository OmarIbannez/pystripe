from payments.models import Plan
import stripe

valid_events = {
    'plan.created': 'create_plan',
    'plan.updated': 'update_plan',
    'plan.deleted': 'delete_plan'
}
events = {}
event = lambda f: events.setdefault(f.__name__, f)

class EventManager:

    def __init__(self, event):
        try:
            self.event = stripe.Event.retrieve(event["id"])
        except Exception as e:
            raise Exception('This is not a valid event')

    def process(self):
        try:
            event_type = valid_events[self.event.type]
        except Exception as e:
            raise Exception('This event is not supported')

        return events[event_type](self.event)

    @event
    def create_plan(event):
        data = {
            'amount': event.data.object.amount,
            'currency': event.data.object.currency,
            'plan_id': event.data.object.id,
            'interval': event.data.object.interval,
            'interval_count': event.data.object.interval_count,
            'livemode': event.data.object.livemode,
            'name': event.data.object.name,
            'trial_period_days': event.data.object.trial_period_days or 0,
        }
        plan = Plan(**data)
        plan.save()

    @event
    def update_plan(event):
        try:
            plan = Plan.objects.get(plan_id=event.data.object.id)
        except Plan.DoesNotExist:
            raise Exception('You must create this event in the local database')

        data = {
            'amount': event.data.object.amount,
            'currency': event.data.object.currency,
            'plan_id': event.data.object.id,
            'interval': event.data.object.interval,
            'interval_count': event.data.object.interval_count,
            'livemode': event.data.object.livemode,
            'name': event.data.object.name,
            'trial_period_days': event.data.object.trial_period_days or 0,
        }

        for key, value in data.items():
            setattr(plan, key, value)
        plan.save()

    @event
    def delete_plan(event):
        try:
            plan = Plan.objects.get(plan_id=event.data.object.id)
        except Plan.DoesNotExist:
            raise Exception('You must create this event in the local database')

        plan.deleted = True
        plan.save()
