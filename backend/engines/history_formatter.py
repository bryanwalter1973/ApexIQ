def format_history(matches):


    formatted = []



    for match in matches:



        formatted.append({


            "home_score":

            int(
                match.get(
                    "match_hometeam_score",
                    0
                )
                or 0
            ),



            "away_score":

            int(
                match.get(
                    "match_awayteam_score",
                    0
                )
                or 0
            ),



            "first_half_goals":

            int(
                match.get(
                    "match_hometeam_score"
                    ,
                    0
                )
                or 0
            ),



            "second_half_goals":

            1


        })



    return formatted