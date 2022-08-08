from flask import request, Blueprint, Response
from . import conf

BP_NAME = 'github_webhooks'
bp = Blueprint(BP_NAME, __name__)


@bp.route('/githubRepository', methods=['POST'])
def monitor_github_repository():
    data = request.json
    for alert in conf.REPO_ALERTS:
        alert(data)
    return Response(status=200)


@bp.route('/githubTeam', methods=['POST'])
def monitor_github_team():
    data = request.json
    for alert in conf.TEAMS_ALERTS:
        alert(data)
    return Response(status=200)


@bp.route('/githubPush', methods=['POST'])
def monitor_github_push():
    data = request.json
    for alert in conf.PUSH_ALERTS:
        alert(data)
    return Response(status=200)
