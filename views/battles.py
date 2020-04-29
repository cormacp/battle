from flask import request
from flask import Response
from flask.views import MethodView

import json
import logging
import random
import uuid

from battle import app
from battle.auth import requires_simple_auth

logging.basicConfig(level=logging.INFO)


class BattlesView(MethodView):
    methods = ['GET', 'POST']

    @requires_simple_auth
    def get(self, *args, **kwargs):
        logging.info(f"GET request for Battle resource")
        battle_uuid = kwargs['uuid']
        battle = app.Battle.query.filter_by(uuid=battle_uuid).first()

        if battle:
            data = {
                'uuid': str(battle.uuid),
                'id': battle.id,
                'player_a': battle.player_a,
                'player_b': battle.player_b,
                'outcome': battle.outcome
            }
            logging.info(f"Retrieved Battle resource {str(battle.uuid)}")
            return Response(json.dumps(data), mimetype='application/json', status=200)
        else:
            logging.info(f"Invalid Battle ID : {str(battle_uuid)}")
            return Response(json.dumps({}), mimetype='application/json', status=404)

    @requires_simple_auth
    def post(self, *args, **kwargs):
        logging.info(f"POST request for Battle resource")

        player_a_id = int(request.args.get('player_a'))
        player_b_id = int(request.args.get('player_b'))
        battle_outcome = {}

        new_battle = app.Battle(
            player_a = player_a_id,
            player_b = player_b_id,
            outcome = battle_outcome
        )
        new_battle.uuid = uuid.uuid4()
        new_battle.outcome['uuid'] = str(new_battle.uuid)

        if player_a_id and player_b_id:
            try:
                player_a = app.Player.query.get_or_404(player_a_id)
                player_b = app.Player.query.get_or_404(player_b_id)

                self.__execute_battle(player_a, player_b, new_battle.outcome)
                app.db.session.add(new_battle)
                app.db.session.commit()
                logging.info(f"Created Battle resource {str(new_battle.uuid)}")

                return Response(json.dumps(new_battle.outcome), mimetype='application/json', status=201)
            except Exception as e:
                return Response(json.dumps({"Bad Request": str(e)}), mimetype='application/json', status=400)
        else:
            return Response(json.dumps({"bad": "request"}), mimetype='application/json', status=400)

    def __execute_battle(self, player_a, player_b, battle_outcome):
        logging.info(f"Beginning battle between {player_a.name} and {player_b.name}")
        a_hp = player_a.hitpoints
        b_hp = player_b.hitpoints
        is_player_a_turn = True
        gold_percentage = random.randint(10, 20) / 100
        logging.info(f"Random gold percentage set to {gold_percentage}")

        """
        yet to be implemented:
            - using the Player.luck property to affect the likelihood of a completely failed attack
            - Expand the rules for each attack turn to include scaling of the attack value, proportional the the player's hit points
            - Additional checking for a player's gold balance being insufficient
        """

        while a_hp > 0 and b_hp > 0:
            if is_player_a_turn:
                # Subtract hit points from player b, equal to the amount of attack points of player a
                # This is greatly simplified due to time constraints
                b_hp = b_hp - player_a.attack
                logging.info(f"{player_a.name} attacked {player_b.name} with {player_a.attack} points. {b_hp} hit points remaining for {player_b.name}")
                is_player_a_turn  = False
            else:
                a_hp = a_hp - player_b.attack
                logging.info(f"{player_b.name} attacked {player_a.name} with {player_b.attack} points. {a_hp} hit points remaining for {player_a.name}")
                is_player_a_turn = True

        # carry out appropriate gold transactions
        if a_hp < 0:
            transaction_amt = int(player_a.gold * gold_percentage)
            logging.info(f"{player_a.name} loses, and will pay {transaction_amt} to {player_b.name}")
            player_a.gold -= transaction_amt
            player_b.gold += transaction_amt
            battle_outcome[player_a.name] = -transaction_amt
            battle_outcome[player_b.name] = transaction_amt
            battle_outcome['random_gold_percentage'] = gold_percentage
        else:
            transaction_amt = int(player_b.gold * gold_percentage)
            logging.info(f"{player_b.name} loses, and will pay {transaction_amt} to {player_a.name}")
            player_b.gold -= transaction_amt
            player_a.gold += transaction_amt
            battle_outcome[player_a.name] = transaction_amt
            battle_outcome[player_b.name] = -transaction_amt
            battle_outcome['random_gold_percentage'] = gold_percentage
