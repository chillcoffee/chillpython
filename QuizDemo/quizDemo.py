#dictionary = {key: value,key:value}
def play():
    capitals = {
        "Philippines": "Manila",
        "Japan": "Tokyo",
        "Germany": "Berlin",
        "Russia": "Moscow",
        "US": "Washington DC"
    }

    for key, value in capitals.items():
        print(f"\nWhat is the capital of {key}?")
        player_ans = input(f"Your answer: ")

        if player_ans == capitals[key]:
            print("Correct")
        else:
            print("Wrong")
score = 0
play()
player_name = "Dodong Pogi"
score = 10
with open("score.txt", "a") as scorefile:
    scorefile.write(f"{player_name} | {score} \n")

