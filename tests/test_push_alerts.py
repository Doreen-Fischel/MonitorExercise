import freezegun
from LegitMonitor import push_alerts


@freezegun.freeze_time("2022-08-08 14:21:34")
def test_alert_push_in_forbidden_hours_true():
    assert push_alerts.alert_push_in_forbidden_hours({})


@freezegun.freeze_time("2022-08-08 11:21:34")
def test_alert_push_in_forbidden_hours_false():
    assert not push_alerts.alert_push_in_forbidden_hours({})