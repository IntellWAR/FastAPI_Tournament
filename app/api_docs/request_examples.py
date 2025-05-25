from fastapi import Body

example_create_match = Body(
    openapi_examples={
        "normal": {
            "summary": "Стандартный матч",
            "value": {
                "team1": "Cyber Warriors",
                "team2": "Digital Gladiators",
                "match_date": "2024-09-05",
                "winner": "Cyber Warriors"
            }
        },
        "no_winner": {
            "summary": "Матч без победителя",
            "value": {
                "team1": "Virtual Knights",
                "team2": "Pixel Samurai",
                "match_date": "2024-09-10"
            }
        }
    }
)