import requests

from app.config import ODDS_API_KEY




BASE_URL = "https://odds-api.io"




def get_match_odds(
    match_id
):


    params = {


        "apiKey":

        ODDS_API_KEY,


        "match":

        match_id


    }



    response = requests.get(

        BASE_URL,

        params=params

    )


    return response.json()