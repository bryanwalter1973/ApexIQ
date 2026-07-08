from engines.candidate_engine import (
    build_candidates
)



matches = [


{

"match":{


"api_match_id":"123",

"home_team":"Team A",

"away_team":"Team B",

"league":"Test League"

},


"home_history":[


{

"home_score":2,

"away_score":1,

"first_half_goals":1,

"second_half_goals":2

},


{

"home_score":1,

"away_score":1,

"first_half_goals":2,

"second_half_goals":0

}


],



"away_history":[


{

"home_score":3,

"away_score":1,

"first_half_goals":2,

"second_half_goals":2

}


]


}


]




result = build_candidates(
    matches
)


print(result)