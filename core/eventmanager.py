
tasks = {}
event = lambda f: tasks.setdefault(f.__name__, f)

class EventManager:

    def __init__(self, event):
        self.event = event

    def process(self):
        if not self.event.type:
            return False

        try:
            event_type = valid_events[self.event.type]
        except Exception as e:
            return False

        tasks[event_type]()

    @event
    def update_plan():
        print('PLAN UPDATED!!!!')


valid_events = {
    'plan.updated': update_plan
}