import logging
from LegitMonitor.notifications.notifier import notifier
from LegitMonitor import conf


def alert_prefixes_of_team(data):
    """
    Notifies to user if a team with a forbidden prefix is created
    :param data: [DICT] Representing the action json
    :return: [BOOL] True if one of the configured prefixes in the team name, False otherwise
    """
    if data.get('action') == 'created':
        prefixes = conf.TEAMS_FORBIDDEN_PREFIXES
        for prefix in prefixes:
            try:
                if data['team']['name'].startswith(prefix):
                    notifier.notify(f"NOTICE: creation of a team with the prefix: "
                                           f"'{prefix}': {data['team']['name']}")
                    return True
            except KeyError:
                logging.warning(
                    f'Unexpected webhook json format. Must include team.name')
                return False
            except SyntaxError:
                logging.warning(
                    f'Unexpected type in webhook json. team.name should be a string.')
                return False
    return False
