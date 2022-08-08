import json
from LegitMonitor.alerts import repo_alerts


def test_alert_immediate_deletion_true():
    with open('repo_test_immediate_deletion_data.json', 'r') as f:
        data = json.load(f)
    assert repo_alerts.alert_immediate_deletion(data)


def test_alert_immediate_deletion_false():
    with open('repo_test_not_immediate_deletion_data.json', 'r') as f:
        data = json.load(f)
    assert not repo_alerts.alert_immediate_deletion(data)