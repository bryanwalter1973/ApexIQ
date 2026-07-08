from providers.football_provider import api_request




def get_team_last_matches(
    team_id
):


    return api_request({

        "action":
        "get_events",

        "team_id":
        team_id,

        "last_match":
        "5"

    })





def get_head_to_head(
    home_id,
    away_id
):


    return api_request({

        "action":
        "get_H2H",

        "firstTeam":
        home_id,

        "secondTeam":
        away_id

    })