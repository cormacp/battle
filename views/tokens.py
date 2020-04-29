from flask import Response
from flask.views import MethodView
import json


class TokensView(MethodView):
    methods = ['GET', 'POST', 'PUT', 'DELETE']

    def get(self):
        data = {'get token': 'response'}
        return Response(json.dumps(data), mimetype='application/json', status=200)

    def post(self):
        data = {'post token': 'response'}
        return Response(json.dumps(data), mimetype='application/json', status=201)

    def put(self):
        data = {'put token': 'response'}
        return Response(json.dumps(data), mimetype='application/json', status=200)

    def delete(self):
        data = {'delete token': 'response'}
        return Response(json.dumps(data), mimetype='application/json', status=200)
