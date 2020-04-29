import json
import os
import pytest
import tempfile
import uuid

from battle import app


class TestBattleResource(object):
    def setup(self):
        self.client = app.flask_app.test_client()
        self.json_request_headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

        self.valid_player_1_uuid = str(uuid.uuid4())
        test_player_1 = app.Player(name="test_player_1")
        test_player_1.uuid = self.valid_player_1_uuid
        app.db.session.add(test_player_1)
        valid_player_1_id = app.Player.query.filter_by(
            uuid=self.valid_player_1_uuid).first().id

        self.valid_player_2_uuid = str(uuid.uuid4())
        test_player_2 = app.Player(name="test_player_2")
        test_player_2.uuid = self.valid_player_2_uuid
        app.db.session.add(test_player_2)
        valid_player_2_id = app.Player.query.filter_by(
            uuid=self.valid_player_2_uuid).first().id

    def test_unauthenticated_get_request(self):
        url = f"/battles/{self.valid_player_1_uuid}"
        response = self.client.get(url, follow_redirects=True)
        assert response.status_code == 401

    def test_unsupported_patch(self):
        url = f"/battles/{self.valid_player_1_uuid}"
        response = self.client.patch(
            url,
            headers={"Authorization": "admin"},
            follow_redirects=True)
        assert response.json == None
        assert response.status_code == 405

    def test_unsupported_put(self):
        url = f"/battles/{self.valid_player_1_uuid}"
        response = self.client.put(
            url,
            headers={"Authorization": "admin"},
            follow_redirects=True)
        assert response.json == None
        assert response.status_code == 405

    def test_unsupported_delete(self):
        url = f"/battles/{self.valid_player_1_uuid}"
        response = self.client.delete(
            url,
            headers={"Authorization": "admin"},
            follow_redirects=True)
        assert response.json == None
        assert response.status_code == 405
