def calculate_probability(
    total,
    matches
):

    if matches == 0:

        return 0


    return round(
        (total / matches) * 100
    )




def calculate_confidence(
    matches,
    fh,
    sh,
    over2
):


    if matches == 0:

        return 0



    data_score = min(
        matches * 4,
        40
    )



    fh_score = (
        fh / matches
    ) * 30



    sh_score = (
        sh / matches
    ) * 30



    over_score = (
        over2 / matches
    ) * 20



    confidence = (

        data_score

        +

        fh_score

        +

        sh_score

        +

        over_score

    )


    return round(
        min(
            confidence,
            95
        )
    )






def select_best_market(
    fh_over,
    fh_under,
    sh_goal,
    over1,
    over2
):


    markets = {


        "FH_OVER_0.5":

        fh_over,



        "FH_UNDER_1.5":

        fh_under,



        "SH_OVER_0.5":

        sh_goal,



        "TOTAL_OVER_1":

        over1,



        "TOTAL_OVER_2":

        over2

    }



    best = max(

        markets,

        key=markets.get

    )



    return {


        "market":

        best,


        "probability":

        markets[best]

    }







def analyze_history(
    home_history,
    away_history
):


    games = (

        home_history

        +

        away_history

    )



    if not games:


        return {



            "fh_over_probability":0,

            "fh_under_probability":0,

            "sh_goal_probability":0,

            "over_1_probability":0,

            "over_2_probability":0,

            "over_25_probability":0,

            "avg_goals":0,

            "confidence":0,

            "best_market":None,

            "market_probability":0

        }





    count = len(games)



    fh_goals = 0

    sh_goals = 0

    over1 = 0

    over2 = 0

    over25 = 0

    total_goals = 0





    for game in games:



        home = int(

            game.get(

                "home_score",

                0

            )

        )



        away = int(

            game.get(

                "away_score",

                0

            )

        )



        goals = home + away



        total_goals += goals




        if goals >= 1:

            over1 += 1




        if goals >= 2:

            over2 += 1




        if goals >= 3:

            over25 += 1





        if game.get(

            "first_half_goals",

            0

        ) >= 1:


            fh_goals += 1






        if game.get(

            "second_half_goals",

            0

        ) >= 1:


            sh_goals += 1





    fh_over_probability = calculate_probability(

        fh_goals,

        count

    )



    fh_under_probability = calculate_probability(

        count - fh_goals,

        count

    )



    sh_goal_probability = calculate_probability(

        sh_goals,

        count

    )



    over1_probability = calculate_probability(

        over1,

        count

    )



    over2_probability = calculate_probability(

        over2,

        count

    )



    over25_probability = calculate_probability(

        over25,

        count

    )




    best_market = select_best_market(

        fh_over_probability,

        fh_under_probability,

        sh_goal_probability,

        over1_probability,

        over2_probability

    )




    confidence = calculate_confidence(

        count,

        fh_goals,

        sh_goals,

        over2

    )





    return {



        "fh_over_probability":

        fh_over_probability,



        "fh_under_probability":

        fh_under_probability,



        "sh_goal_probability":

        sh_goal_probability,



        "over_1_probability":

        over1_probability,



        "over_2_probability":

        over2_probability,



        "over_25_probability":

        over25_probability,



        "avg_goals":

        round(

            total_goals / count,

            2

        ),



        "confidence":

        confidence,



        "best_market":
        best_market["market"],



        "market_probability":

        best_market["probability"]

    }