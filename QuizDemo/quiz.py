country_dict = {
    "Philippines": "Manila",
    "Japan": "Tokyo",
    "Germany": "Berlin",
    "Russia": "Moscow",
    "US": "Washington DC"
}

for country_key in country_dict:
    print(f"\nWhat is the capital of {country_key}?")
    correct_answer = country_dict[country_key]

    player_answer = input(f"Your answer: ")
    if player_answer == correct_answer:
        print("Correct")
    else:
        print("Wrong")

score = 10
player_name = "Ruffa"
with open("score.txt", 'a') as file:
    file.write(f"{player_name} | {score} \n")