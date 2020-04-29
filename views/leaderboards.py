from flask import request
from flask import Response
from flask.views import MethodView

import json
import logging
import uuid

from battle import app
from battle.auth import requires_simple_auth


logging.basicConfig(level=logging.INFO)


class LeaderboardsView(MethodView):
    methods = ['GET']

    @requires_simple_auth
    def get(self, *args, **kwargs):
        logging.info(f"GET request for leaderboard resource")
        player_data = app.Player.query.order_by(app.Player.gold.desc()).all()
        leaderboard = []

        for player in player_data:
            leaderboard.append({
                player.name: {
                    "gold": player.gold,
                    "uuid": str(player.uuid)
                }
            })

        logging.info(f"Leadeboard retrieved : {leaderboard}")
        return Response(json.dumps(leaderboard), mimetype='application/json', status=200)
