from engines.historical_engine import (
    analyze_history
)




MIN_CONFIDENCE = 81

MIN_PROBABILITY = 88





def evaluate_match(
    match,
    home_history,
    away_history
):


    analysis = analyze_history(

        home_history,

        away_history

    )



    if analysis["confidence"] < MIN_CONFIDENCE:


        return None




    if analysis["market_probability"] < MIN_PROBABILITY:


        return None





    return {


        "match_id":

        match.get(
            "api_match_id"
        ),



        "home":

        match.get(
            "home_team"
        ),



        "away":

        match.get(
            "away_team"
        ),



        "league":

        match.get(
            "league"
        ),



        "market":

        analysis["best_market"],



        "probability":

        analysis["market_probability"],



        "confidence":

        analysis["confidence"]

    }







def build_candidates(
    matches
):


    candidates = []



    for item in matches:



        result = evaluate_match(

            item["match"],

            item["home_history"],

            item["away_history"]

        )



        if result:


            candidates.append(
                result
            )





    return sorted(

        candidates,

        key=lambda x:

        x["confidence"],

        reverse=True

    )