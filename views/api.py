from flask import Response
from flask.views import MethodView
import json

from battle.auth import requires_simple_auth


class ApiInfoView(MethodView):
    methods = ['GET']

    @requires_simple_auth
    def get(self):
        data = {'battle_api_version': '1.0'}
        return Response(json.dumps(data), mimetype='application/json', status=200)
