from datetime import datetime
from LegitMonitor.notifications.notifier import notifier
from LegitMonitor import conf


def alert_push_in_forbidden_hours(data):
    """
    Notifies to user if a push was made between the configurable hours.
    :param data: [DICT] Representing the action json
    :return: [BOOL] True if the push was between forbidden_time_start and forbidden_time_end, False otherwise
    """
    forbidden_time_start = conf.PUSH_FORBIDDEN_TIME_START
    forbidden_time_end = conf.PUSH_FORBIDDEN_TIME_END
    pushing_time = datetime.now()
    if forbidden_time_start <= pushing_time.time() <= forbidden_time_end:
        notifier.notify(f"NOTICE: code pushing between {forbidden_time_start}-{forbidden_time_end}")
        return True
    return False

