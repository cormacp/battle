# from app.views.chord_editor import ChordEditor7DView
# from app.views.songs import (
#     Songs7DView, InternalSongs7DView, Songs7DAdminView, SongsQueueView
# )
# from app.views.releases import Releases7DView, Releases7DAdminView
# from app.views.artists import Artists7dView

#
# URLS = (
#     ('/api/mir/chord-editor/7d/songs',
#         ChordEditor7DView, 'chord editor songs'),
#     ('/api/mir/chord-editor/7d/songs/<uuid:uuid>',
#         ChordEditor7DView, 'song_editing'),
#     ('/api/mir/7d/<string:provider>/songs', Songs7DView, 'song_list'),
#     ('/api/mir/7d/<string:provider>/songs/<uuid:uuid>',
#         Songs7DView, 'song'),
#     ('/api/int/mir/7d/songs', InternalSongs7DView, 'songs7d_internal'),
#     ('/api/adm/mir/7d/songs', Songs7DAdminView, 'songs_admin'),
#     ('/api/adm/mir/7d/songs/<uuid:uuid>', Songs7DAdminView, 'song_admin'),
#     ('/api/mir/7d/<string:provider>/artists/<uuid:artist_id>/releases',
#         Releases7DView, 'releases'),
#     ('/api/mir/7d/<string:provider>/artists/<uuid:artist_id>' +
#         '/releases/<uuid:release_id>',
#         Releases7DView, 'release'),
#     ('/api/adm/mir/7d/artists/<uuid:artist_id>/releases',
#         Releases7DAdminView, 'releases_admin'),
#     ('/api/adm/mir/7d/artists/<uuid:artist_id>' +
#         '/releases/<uuid:release_id>',
#         Releases7DAdminView, 'release_admin'),
#     ('/api/mir/7d/<string:provider>/artists/<uuid:uuid>',
#         Artists7dView, 'artist view'),
#     ('/api/mir/7d/<string:provider>/artists', Artists7dView, 'artists view'),
#     ('/api/int/mir/7d/songs/queue/priority',
#         SongsQueueView, 'songs queue view')
# )

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
    
