from flask import request
from flask import Response
from functools import wraps
import json
import logging

logging.basicConfig(level=logging.INFO)

"""
Simple authentication decorator, using a static auth token.
A full implementation would include token creation, validation and refresh endpoints.
Additionally, a full implemention would use full OAuth2 Bearer tokens
"""
def requires_simple_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        logging.info(f"Authorising API request with simple auth")
        auth_token = request.headers.get('Authorization')
        if auth_token != "admin":
            logging.info(f"Unauthorising request")
            return Response(
                json.dumps({"Access denied": "Invalid auth token"}),
                status=401, mimetype='application/json')
        logging.info(f"Request authorized")
        return f(*args, **kwargs)
    return decorated
