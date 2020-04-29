from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID, JSON
import uuid

from battle.views.players import PlayersView
from battle.views.battles import BattlesView
from battle.views.leaderboards import LeaderboardsView
from battle.views.api import ApiInfoView
from .urls import URLS


flask_app = Flask(__name__)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://dbadmin:abc123@localhost:5432/battle_dev"
logging.basicConfig(level=logging.INFO)
db = SQLAlchemy(flask_app)
migrate = Migrate(flask_app, db)

#  Parse URL definitions and initialize views
for route in URLS:
    flask_app.add_url_rule(
        route[0], view_func=route[1].as_view(route[2]))
logging.info(f"Application intialised")



class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    name = db.Column(db.String(1024), nullable=False)
    gold = db.Column(db.Integer())
    attack = db.Column(db.Integer())
    hitpoints = db.Column(db.Integer())
    luck = db.Column(db.Integer())

    def __init__(self, name, gold=1000, attack=50, hitpoints=100, luck=10):
        self.uuid = uuid.uuid4()
        self.name = name
        self.gold = gold
        self.attack = attack
        self.hitpoints = hitpoints
        self.luck = luck

    def __repr__(self):
        return f"<Player {self.name}, uuid {str(self.uuid)}>"


class Battle(db.Model):
    __tablename_ = 'battles'
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    player_a = db.Column(Integer, ForeignKey('players.id'), nullable=False)
    player_b = db.Column(Integer, ForeignKey('players.id'), nullable=False)
    outcome = db.Column(JSON)

    def __init__(self, player_a=None, player_b=None, outcome={}):
        self.player_a = player_a
        self.player_b = player_b,
        self.outcome = outcome

    def __repr__(self):
        return f"<Battle {self.player_a} vs {self.player_b}, uuid {str(self.uuid)}>"
