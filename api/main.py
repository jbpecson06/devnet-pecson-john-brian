# Pecson, John Brian

import random
import requests

while True:
    print("\n=== Pokemon Guessing Game ===")
    print("1. Start Game")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        pokemon_ids = [25, 6, 150, 94, 74]
                    # Pikachu
                    # Charizard
                    # Mewtwo
                    # Gengar
                    # Geodude

        number = random.choice(pokemon_ids)

        url = "https://pokeapi.co/api/v2/pokemon/" + str(number)
        data = requests.get(url).json()

        name = data["name"]

        print("\nWho's that PokeMon?")
        print("Height:", data["height"])
        print("Weight:", data["weight"])
        print("Abilities:")
        for ability in data["abilities"]:
            print("-", ability["ability"]["name"])

        attempt = 3

        while attempt > 0:
            guess = input("\nEnter Pokemon name: ").lower()

            if guess == name:
                print("Nice!")
                break
            else:
                attempt = attempt - 1
                print("Wrong answer!")
                print("Attempt left:", attempt)

        if attempt == 0:
            print("\nGame Over!")
            print("The Pokemon was:", name)

    elif choice == "2":
        print("Exit.")
        break

    else:
        print("Invalid!")