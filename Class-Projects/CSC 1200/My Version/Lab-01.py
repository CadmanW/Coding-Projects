# Starting Variables
pokemonOne = {
    "name": "Pikachu",
    "hp": 100,
    "ap": 20
}

pokemonTwo = {
    "name": "Charmander",
    "hp": 90,
    "ap": 25
}

critMultiplier = 1.5

# Calculating Damage
damage = pokemonOne["ap"] - 5
pokemonTwo["hp"] -= damage

# Printing Damage Output
print(f"{pokemonOne["name"]} attacks {pokemonTwo["name"]} for {damage} damage.")
print(f"{pokemonTwo["name"]}'s HP is now {pokemonTwo["hp"]}.")

# Calculate Critical Damage
critDamage = damage * critMultiplier
pokemonTwo["hp"] -= critDamage

# Printing Critical Damage Output
print(f"{pokemonOne["name"]} attacks {pokemonTwo["name"]} for {critDamage} critical damage.")
print(f"{pokemonTwo["hp"]}'s HP is now {pokemonTwo["hp"]}")