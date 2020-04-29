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
