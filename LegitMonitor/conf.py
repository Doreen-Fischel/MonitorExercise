from datetime import time
from . import push_alerts, repo_alerts, teams_alerts

REPO_CREATE_DELETE_LIMIT_MINUTES = 10

TEAMS_FORBIDDEN_PREFIXES = ['hacker']

PUSH_FORBIDDEN_TIME_START = time(14, 0)
PUSH_FORBIDDEN_TIME_END = time(16, 0)

TIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

PUSH_ALERTS = [
    push_alerts.alert_push_in_forbidden_hours,
                        ]

REPO_ALERTS = [
    repo_alerts.alert_immediate_deletion,
]

TEAMS_ALERTS = [
    teams_alerts.alert_prefixes_of_team,
]