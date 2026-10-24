import requests



pokemon1 = response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
pokemon2 = response = requests.get("https://pokeapi.co/api/v2/pokemon/charizard")
pokemon3 = response = requests.get("https://pokeapi.co/api/v2/pokemon/mewtwo")
pokemon4 = response = requests.get("https://pokeapi.co/api/v2/pokemon/gengar")
pokemon5 = response = requests.get("https://pokeapi.co/api/v2/pokemon/geodude")

# Pokemon 1
p_name1 = pokemon1.json()['name']
p_height1 = pokemon1.json()['height']
p_weight1 = pokemon1.json()['weight']

# Pokemon 2
p_name2 = pokemon2.json()['name']
p_height2 = pokemon2.json()['height']
p_weight2 = pokemon2.json()['weight']

# Pokemon 3
p_height2name3 = pokemon3.json()['name']
p_height3 = pokemon3.json()['height']
p_weight3 = pokemon3.json()['weight']

# Pokemon 4
p_name4 = pokemon4.json()['name']
p_height4 = pokemon4.json()['height']
p_weight4 = pokemon4.json()['weight']

# Pokemon 5
name5 = pokemon5.json()['name']
height5 = pokemon5.json()['height']
weight5 = pokemon5.json()['weight']


def menu_game():
    
    print("== Guessing Game ==")
    print("1. Start")
    print("1. ")
    


def start_game():
    pass



start_game()

