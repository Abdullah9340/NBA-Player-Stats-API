from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder


nba_teams = teams.get_teams()


def getTeamID(name):
    temp = teams.find_teams_by_nickname(name)
    if not temp:
        temp = teams.find_team_by_abbreviation(name)
    if not temp:
        temp = teams.find_teams_by_full_name(name)
    if not temp:
        temp = teams.find_teams_by_city(name)
    if not temp:
        temp = teams.find_teams_by_state(name)
    return temp


def getPlayerID(name):
    return players.find_players_by_full_name(name)


def getPlayerName(id):
    return players.find_player_by_id(id)


def get_last_5_games(abrv):
    team = [team for team in nba_teams if team['abbreviation'] == abrv][0]
    team_id = team['id']
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team_id)
    games = gamefinder.get_data_frames()[0]
    return games.head()


def get_player_college_totals(id):
    career_stats = playercareerstats.PlayerCareerStats(player_id=id)
    data = career_stats.get_normalized_dict()['CareerTotalsCollegeSeason']


def get_player_season_totals(id):
    career_stats = playercareerstats.PlayerCareerStats(player_id=id)
    data = career_stats.get_normalized_dict()['SeasonTotalsRegularSeason']
    return data


def get_player_picture(id):
    image_url = "https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/" + \
        str(id) + ".png"
    return image_url
