# Battle

A simple Flask API for carrying out turn-based battles

## Installation
All project requirements (Flask, SQLAlchemy, pytest, etc) are covered in this project's Pipfile, which can be used as follows:

```
cd <project_dir>
pipenv shell
pipenv install --dev
```

## DB Setup

This project requires a local running instance of PostreSQL, a correctly configured db admin user, and a newly-created database. The following commands will achieve this:

```
$ createuser --pwprompt dbadmin
  # use password abc123 when prompted

$ createdb -Odbadmin -Eutf8 battle_dev

For PSQL console access :
$ psql -U dbadmin -W battle_dev

To initialise and migrate db for Flask app
$ flask db init
$ flask db migrate
$ flask db upgrade
```

## Running

To run the Battle API:

```
cd <project_dir>
flask run
```

The API will begin listening at ``localhost:5000``, with all available API endpoints and resources documented in the next section. Additionally, this project includes a full export of Postman requests which can be used against a running API

## Unit Tests

All unit tests are contained in the ``/tests`` directory, and may be run as follows:

```
pytest tests/
======================================== test session starts ========================================
platform darwin -- Python 3.7.7, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: /Users/cormacphelan/Dropbox/code/flask/battle
collected 17 items

tests/test_battle_view.py ....                                                                [ 23%]
tests/test_leaderboard_view.py .......                                                        [ 64%]
tests/test_players_view.py ......                                                             [100%]

=================================== 17 passed, 1 warning in 0.66s ===================================
```

# API Resources

All API endpoints are protected with very simple authentication. This requires that all requests include ``Authorization: admin`` in their headers.

## Players

```
<domain>/players
<domain>/players/<player_uuid>
```
Supported methods:
* GET - to retrieve player data
* POST - to create player data

### sample CURL GET request

```
curl --location --request GET 'http://127.0.0.1:5000/players/f4f7e97d-9953-4970-8d8e-f0542a289797' \
--header 'Authorization: admin'
```

Response:
```
{
    "uuid": "9957bdb9-b403-46fe-94d2-2b2a6c4732d2",
    "id": 15,
    "name": "stingy_steve",
    "gold": 509,
    "attack": 200,
    "hitpoints": 3000,
    "luck": 100
}
```

* UUID (uuid) : Unique identifier for ID-obfuscated requests
* name (string) : Player name, limited to 1024 characters
* gold (int) : A player's balance of gold
* attack (int) : A player's attack power
* hitpoints (int) : A player's health-level
* luck (int) : A player's likelihood to miss during their turn (currently unused)


### sample CURL POST request

```
curl --location --request POST 'http://127.0.0.1:5000/players' \
--header 'Authorization: admin' \
--header 'Content-Type: application/json' \
--data-raw '{
	"name": "mediocre_mark",
	"gold": 1000,
    "attack": 40,
    "hitpoints": 13000,
    "luck": 40
}'
```

Response:
```
{
    "uuid": "9dd3a1e0-4fcc-4c2f-a48f-e1e27051030d",
    "name": "mediocre_mark",
    "gold": 1000,
    "attack": 40,
    "hitpoints": 13000,
    "luck": 40
}
```

## Battles

```
<domain>/battles
<domain>/battles/<battle_uuid>
```
Supported methods:
* GET - to retrieve historical battle data
* POST - to a new battle between players


### sample CURL POST request

```
curl --location --request POST 'http://127.0.0.1:5000/battles?player_a=14&player_b=15' \
--header 'Authorization: admin'
```

Response:
```
{
    "uuid": "17a246d7-8153-447b-bef3-e3a1c9119fc5",
    "richie_rich": 91,
    "stingy_steve": -91,
    "random_gold_percentage": 0.18
}
```

* UUID (uuid) : Unique identifier for the battle
* player_a_outcome (int) : player A's profit/loss from the battle
* player_b_outcome (int) : player B's profit/loss from the battle
* random_gold_percentage (float) : Random percentage between 10-20%, dictating the size of the winning purse

### sample CURL GET request

```
curl --location --request GET 'http://127.0.0.1:5000/battles/17a246d7-8153-447b-bef3-e3a1c9119fc5' \
--header 'Authorization: admin'
```

Response:
```
{
    "uuid": "17a246d7-8153-447b-bef3-e3a1c9119fc5",
    "player_a": 14,
    "player_b": 15,
    "outcome": {
        "uuid": "17a246d7-8153-447b-bef3-e3a1c9119fc5",
        "richie_rich": 91,
        "stingy_steve": -91,
        "random_gold_percentage": 0.18
    }
}
```
* UUID (uuid) : Unique identifier for the battle
* player_a (int) : ID for player A (foreign key: Players.id
* player_b (int) : ID for player B (foreign key: Players.id)
* outcome (dict) : a structured JSON object containing outcome information for a completed battle
