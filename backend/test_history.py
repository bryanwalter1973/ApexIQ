from engines.historical_engine import (
    analyze_history
)



home = [

{
"home_score":2,
"away_score":1,
"first_half_goals":1,
"second_half_goals":2
},

{
"home_score":1,
"away_score":0,
"first_half_goals":0,
"second_half_goals":1
}

]



away = [

{
"home_score":3,
"away_score":1,
"first_half_goals":2,
"second_half_goals":2
}

]



result = analyze_history(
    home,
    away
)


print(result)