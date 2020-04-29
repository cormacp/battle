import json
import os
import pytest
import tempfile
import uuid

from battle import app


class TestPlayerResource(object):
    def setup(self):
        self.client = app.flask_app.test_client()
        self.json_request_headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        self.valid_player_1_uuid = str(uuid.uuid4())

        test_player_1 = app.Player(
            name="test_player",
            gold=123,
            attack=456,
            hitpoints=1000,
            luck=4
        )
        test_player_1.uuid = self.valid_player_1_uuid
        app.db.session.add(test_player_1)

    def test_unauthenticated_get_request(self):
        url = f"/players/{self.valid_player_1_uuid}"
        response = self.client.get(url, follow_redirects=True)
        assert response.status_code == 401

    def test_404_get_request(self):
        response = self.client.get(
            '/players/no_such_player',
            headers={"Authorization": "admin"},
            follow_redirects=True)
        assert response.status_code == 404

    def test_valid_get_request(self):
        url = f"/players/{self.valid_player_1_uuid}"
        response = self.client.get(
            url,
            headers={"Authorization": "admin"},
            follow_redirects=True)
        assert response.status_code == 200
        data = json.loads(response.get_data().decode('utf-8'))
        assert 'uuid' in data
        assert data['uuid'] == self.valid_player_1_uuid
        assert 'gold' in data
        assert data['gold'] == 123
        assert 'attack' in data
        assert data['attack'] == 456
        assert 'hitpoints' in data
        assert data['hitpoints'] == 1000
        assert 'luck' in data
        assert data['luck'] == 4

    # def test_valid_post_request(self):
    #     url = f"/players"
    #     json_request_body = {
    #         "name": "test_post_player",
    #         "gold": 1000,
    #         "attack": 40,
    #         "hitpoints": 13000,
    #         "luck": 40
    #     }
    #     response = self.client.post(
    #         url, data=json.dumps(json_request_body),
    #         headers={
    #             "Authorization": "admin",
    #             "Content-Type": "application/json",
    #             "Accept": "application/json"
    #         }
    #     )
    #     assert response.status_code == 201

    def test_unsupported_patch(self):
        url = f"/players/{self.valid_player_1_uuid}"
        response = self.client.patch(
            url,
            headers={"Authorization": "admin"},
            follow_redirects=True)
        assert response.json == None
        assert response.status_code == 405

    def test_unsupported_put(self):
        url = f"/players/{self.valid_player_1_uuid}"
        response = self.client.put(
            url,
            headers={"Authorization": "admin"},
            follow_redirects=True)
        assert response.json == None
        assert response.status_code == 405

    def test_unsupported_delete(self):
        url = f"/players/{self.valid_player_1_uuid}"
        response = self.client.delete(
            url,
            headers={"Authorization": "admin"},
            follow_redirects=True)
        assert response.json == None
        assert response.status_code == 405
