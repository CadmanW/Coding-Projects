# lab1 - student
# updated: 9/12/2024
# name: Cadman
# date: Warren


# create 3 variables for pokemon 1
# pokemon 1 name - set this to the string Pikachu
# pokemon 1 hp - this will be set to 100 so that Pikachu can have 100 points of health
# pokemon 1 attack - this will be set to 20 and will be the max, non-critical attack that Pikachu can do

pokemon_1_name = "pikachu"
pokemon_1_hp = 100
pokemon_1_attack = 20

# create 3 variables for pokemon 2
# pokemon 2 name - set this to the string Charmander
# pokemon 2 hp - this will be set to 90 so that Charmander can have 90 points of health
# pokemon 2 attack - this will be set to 25 and will be the max, non-critical attack that Charmander can do

pokemon_2_name = "charmander"
pokemon_2_hp = 90
pokemon_2_attack = 25

# create a variable named crit_multiplier and set it to 1.5 

crit_multiplier = 1.5

# calculating damage output
# create a variable called damage and set it equal to pokemon 1 attack - 5
# then set pokemon 2's hp to itself - damage. 
# this will look something like pokemon 2 hp = pokemon 2 hp - damage

damage = pokemon_1_attack - 5
pokemon_2_hp -= damage

# print the sentence: <pokemon 1 name> attacks <pokemon 2 name> for <damage> damage.
# print this next sentence: <pokemon 2 name>'s HP is now <pokemon 2 hp>.
# note: 
# you can do this by using print() and inside the () you can set multiple strings and variables as the arguments. You can also do
# something like the below:
# print(f"{variable_name} the rest of my string, but wait there's {another_variable}")
# you can also do this: print(variable_name, " the rest of my string, but wait there's", another_variable) 
# the about has comma separated strings and variables.

print(f"{pokemon_1_name} attacks {pokemon_2_name} for {damage} damage.")
print(f"{pokemon_2_name}'s HP is now {pokemon_2_hp}")

# create a variable name crit_damage and set it to damage * crit_multiplier
# then set pokemon 2's hp to itself - damage.

crit_damage = damage * crit_multiplier
pokemon_2_hp -= crit_damage

# print the sentence: <pokemon 1 name> attacks <pokemon 2 name> for <crit_damage> damage.
# print this next sentence: <pokemon 2 name>'s HP is now <pokemon 2 hp>.
# note: 
# you can do this by using print() and inside the () you can set multiple strings and variables as the arguments. You can also do
# something like the below:
# print(f"{variable_name} the rest of my string, but wait there's {another_variable}")
# you can also do this: print(variable_name, " the rest of my string, but wait there's", another_variable) 
# the about has comma separated strings and variables.

print(f"{pokemon_1_name} attacks {pokemon_2_name} for {crit_damage} damage.")
print(f"{pokemon_2_name}'s HP is now {pokemon_2_hp}")