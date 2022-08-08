from datetime import datetime
import logging
from LegitMonitor.notifications.notifier import notifier
from LegitMonitor import conf


def alert_immediate_deletion(data):
    """
    Notifies to user if a repo is deleted in less than the configured number of minutes since it was created.
    :param data: [DICT] Representing the action json
    :return: [BOOL] True if the deletion was immediate, False otherwise
    """
    if data.get('action') == 'deleted':
        number_of_minutes = conf.REPO_CREATE_DELETE_LIMIT_MINUTES
        try:
            creation_time = datetime.strptime(data['repository']['created_at'], conf.TIME_FORMAT)
            deletion_time = datetime.strptime(data['repository']['updated_at'], conf.TIME_FORMAT)
        except KeyError:
            logging.warning(
                f'Unexpected webhook json format. Must include repository.created_at and repository.updated_at')
            return False
        except ValueError:
            logging.warning(
                f'Unexpected time format in the webhook json. Expected format: {conf.TIME_FORMAT}')
            return False
        time_difference = deletion_time - creation_time
        if time_difference.days == 0 and time_difference.seconds / 60 < number_of_minutes:
            notifier.notify(f'NOTICE: creation and deletion of repository in less than '
                                   f'{number_of_minutes} mins.')
            return True
    return False
