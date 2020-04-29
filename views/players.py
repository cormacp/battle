from flask import request
from flask import Response
from flask.views import MethodView

import json
import logging
import uuid

from battle import app
from battle.auth import requires_simple_auth

logging.basicConfig(level=logging.INFO)


class PlayersView(MethodView):
    methods = ['GET', 'POST']

    @requires_simple_auth
    def get(self, *args, **kwargs):
        logging.info(f"GET request for Player resource")
        player_uuid = kwargs['uuid']
        player = app.Player.query.filter_by(uuid=player_uuid).first()
        if player:
            data = {
                'uuid': str(player.uuid),
                'id': player.id,
                'name': player.name,
                'gold': player.gold,
                'attack': player.attack,
                'hitpoints': player.hitpoints,
                'luck': player.luck
            }
            logging.info(f"Retrieved Player resource {str(player.uuid)}")
            return Response(json.dumps(data), mimetype='application/json', status=200)
        else:
            return Response(json.dumps({}), mimetype='application/json', status=404)

    @requires_simple_auth
    def post(self, *args, **kwargs):
        logging.info(f"POST request for Player resource")
        data=request.get_json()
        new_player = app.Player(
            name=data.get('name'),
            gold=data.get('gold'),
            attack=data.get('attack'),
            hitpoints=data.get('hitpoints'),
            luck=data.get('luck')
        )
        new_player.uuid = uuid.uuid4()
        app.db.session.add(new_player)
        app.db.session.commit()

        response_data = {
            'uuid': str(new_player.uuid),
            'name': new_player.name,
            'gold': new_player.gold,
            'attack': new_player.attack,
            'hitpoints': new_player.hitpoints,
            'luck': new_player.luck
        }
        logging.info(f"Created Player resource {str(new_player.uuid)}")
        return Response(json.dumps(response_data), mimetype='application/json', status=201)
