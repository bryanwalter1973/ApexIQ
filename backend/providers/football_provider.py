import requests

from app.config import APIFOOTBALL_KEY



BASE_URL = "https://apiv3.apifootball.com"




def api_request(params):


    params["APIkey"] = APIFOOTBALL_KEY



    response = requests.get(

        BASE_URL,

        params=params

    )


    return response.json()






def get_today_fixtures():


    from datetime import datetime


    today = datetime.now().strftime(
        "%Y-%m-%d"
    )



    return api_request({

        "action":
        "get_events",


        "from":
        today,


        "to":
        today

    })





def get_live_matches():


    return api_request({

        "action":
        "get_events",


        "match_live":
        "1"

    })