import json
from LegitMonitor.alerts import teams_alerts


def test_alert_prefixes_of_team_true():
    with open('team_test_team_test_forbidden_name_data.json', 'r') as f:
        data = json.load(f)
    assert teams_alerts.alert_prefixes_of_team(data)


def test_alert_prefixes_of_team_false():
    with open('team_test_team_test_allowd_name_data.json', 'r') as f:
        data = json.load(f)
    assert not teams_alerts.alert_prefixes_of_team(data)