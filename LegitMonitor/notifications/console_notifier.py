from .base_notifier import BaseNotifier


class ConsoleNotifier(BaseNotifier):
    def notify(self, data):
        print(data)
