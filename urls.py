from battle.views.players import PlayersView
from battle.views.battles import BattlesView
from battle.views.leaderboards import LeaderboardsView
from battle.views.api import ApiInfoView

URLS = (
    ('/api', ApiInfoView, 'root'),
    ('/players', PlayersView, 'players'),
    ('/players/<uuid:uuid>', PlayersView, 'player_by_uuid'),
    ('/battles', BattlesView, 'battles'),
    ('/battles/<uuid:uuid>', BattlesView, 'battle_by_uuid'),
    ('/leaderboards', LeaderboardsView, 'leaderboards')
)
