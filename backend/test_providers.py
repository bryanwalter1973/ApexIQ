from providers.football_provider import (
    get_today_fixtures,
    get_live_matches
)



print(
    "TODAY FIXTURES"
)


fixtures = get_today_fixtures()


print(
    len(fixtures)
)



print(
    "LIVE"
)


live = get_live_matches()


print(
    len(live)
)