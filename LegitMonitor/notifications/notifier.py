from .console_notifier import ConsoleNotifier


class Notifier:
    def __init__(self):
        self._notification_methods = []

    def register_notification_method(self, notification_method):
        self._notification_methods.append(notification_method)

    def notify(self, data):
        if not self._notification_methods:
            print(data)
        for method in self._notification_methods:
            method().notify(data)


notifier = Notifier()
notifier.register_notification_method(ConsoleNotifier)
