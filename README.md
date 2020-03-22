# Setup

    git clone https://github.com/huazhihao/soccer && cd soccer
    pip install -r requirement.txt
    FLASK_APP=soccer.py flask run

# Database

Download [soccer.zip](https://www.kaggle.com/hugomathien/soccer/data) and unzip to ./database.sqlite under this repo working directory.

# Query APIs

## Generic queries

    curl http://127.0.0.1:5000/q/league # all leagues
    curl http://127.0.0.1:5000/q/league/country_id/1729 # league "England Premier League"
    curl http://127.0.0.1:5000/q/team/team_api_id/8455 # team Chelsea

## Ad hoc queries

    curl http://127.0.0.1:5000/team/league/1729 # all teams under "England Premier League"
    curl http://127.0.0.1:5000/player/team/8455-10260 # all players attended the match between Chelsea and Manchester United
