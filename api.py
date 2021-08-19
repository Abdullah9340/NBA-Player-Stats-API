from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from nbadata import getPlayerID, getTeamID, get_player_season_totals, get_player_college_totals, get_player_picture
import json

app = Flask(__name__)
CORS(app)
api = Api(app)


class getPlayerInfo(Resource):
    def get(self, name):
        nbaInfo = getPlayerID(name)
        return {'info': nbaInfo}


class getTeamInfo(Resource):
    def get(self, name):
        teamInfo = getTeamID(name)
        return {'info': teamInfo}


class getPlayerSeasonTotals(Resource):
    def get(self, id):
        seasonTotals = get_player_season_totals(id)
        return json.dumps(seasonTotals)


class getPlayerCollegeTotals(Resource):
    def get(self, id):
        collegeTotals = get_player_college_totals(id)
        return {'info': collegeTotals}


class getPlayerPicture(Resource):
    def get(self, id):
        picture = get_player_picture(id)
        return {'info': picture}


api.add_resource(getPlayerInfo, '/getPlayer/<string:name>')
api.add_resource(getTeamInfo, '/getTeam/<string:name>')
api.add_resource(getPlayerSeasonTotals, '/getPlayer/seasons/<int:id>')
api.add_resource(getPlayerCollegeTotals, '/getPlayer/college/<int:id>')
api.add_resource(getPlayerPicture, '/getPlayer/picture/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
