from providers.football_provider import (
    get_today_fixtures
)

from providers.history_provider import (
    get_team_last_matches
)


from engines.history_formatter import (
    format_history
)


from engines.candidate_engine import (
    build_candidates
)


from app.database import supabase



BATCH_SIZE = 20

TARGET_CANDIDATES = 10





def save_candidates(
    candidates
):


    for item in candidates:



        supabase.table(
            "daily_candidates"
        ).insert({


            "market":

            item["market"],


            "confidence":

            item["confidence"],


            "analysis_score":

            item["probability"],


            "status":

            "WAITING"


        }).execute()





def run_daily_scan():



    fixtures = get_today_fixtures()



    print(
        "TOTAL FIXTURES:",
        len(fixtures)
    )



    selected = []



    for i in range(
        0,
        len(fixtures),
        BATCH_SIZE
    ):



        batch = fixtures[
            i:i+BATCH_SIZE
        ]



        print(

            "ANALYZING BATCH:",

            i,

            "-",


            i + BATCH_SIZE

        )



        formatted = []



        for match in batch:



            formatted.append({

                "match":{


                    "api_match_id":

                    match.get(
                        "match_id"
                    ),


                    "home_team":

                    match.get(
                        "match_hometeam_name"
                    ),


                    "away_team":

                    match.get(
                        "match_awayteam_name"
                    ),


                    "league":

                    match.get(
                        "league_name"
                    )

                },


                "home_history":
        
                format_history(

                    get_team_last_matches(

                        match.get(
                            "match_hometeam_id"
                        )

                    )

                ),



                "away_history":

                format_history(

                    get_team_last_matches(

                        match.get(
                            "match_awayteam_id"
                        )

                    )

                )


            })




        candidates = build_candidates(
            formatted
        )



        selected.extend(
            candidates
        )



        if len(selected) >= TARGET_CANDIDATES:


            break





    selected = selected[
        :TARGET_CANDIDATES
    ]



    print(

        "QUALIFIED:",

        len(selected)

    )



    save_candidates(
        selected
    )



    return selected