# Lab 5
# name: Cadman Warren
# 11/17/24

import random

# Pokemon and their items declaration 
poke1_dictionary = {"Name":"Groudon", "HP":100, "AP":20}
poke1_list = [3,2]

poke2_dictionary = {"Name":"Kyogre", "HP":90, "AP":25}
poke2_list = [2,2]

turnCounter = 1

def welcome():
    print("Welcome to Pokemon Ruby!")
    print("#" * 50)

def playing():
    while poke1_dictionary["HP"] > 0 and poke2_dictionary["HP"] >0 :
        playinput = input("Would you like to start a battle? (y/n): ").lower()

        if playinput == 'y':
            play = True

        elif playinput == 'n':
            play = False
        
        return play

# Prints optinos
def printOptions():
    print("Option 1: Attack")
    print("Option 2: Pass")
    print("Option 3: Item")
    choice = input("Choose an option to continue: ")
    return choice


def calcDamage(ap,crit=1):
    # Returns attack power minus a rand integer between 1 and 5 times 1
    return (ap - random.randint(1,5)) * crit
    
# applies the damage to the health and check if the pokemon fainted
def applyDamage(hp, damage): 
    hp = hp - damage

    if hp <= 0:
        hp = 0

    return hp

def printOutcome(attacker, defender, damage, defender_hp):
    print(f"{attacker} attacks {defender} for {damage} damage.")
    print(f"{defender}'s HP is now {defender_hp}.")

###########
# Didn't exactly understand the given parameters and arguements in the document stuck to what I did understand

def attack(attackingPokemon, defendingPokemon, crit_multiplier=1):
 # IMPORTANT: Modify the below to use the dictionaries passed
    damage = calcDamage(attackingPokemon["AP"], crit_multiplier)
    defendingPokemon["HP"] = applyDamage(defendingPokemon["HP"], damage)
    printOutcome(attackingPokemon["Name"], defendingPokemon["Name"], damage,
    defendingPokemon["HP"])

def useItem(pokemon, items):
    while True: 
        print(f"1. Use potion items [{items[0]}]")
        print(f"2. Use attack_up items [{items[1]}]")
        print("3. Cancel")

        # Gets user input
        itemChoice = input("Choose an option to continue: ")

        # If they chose "1" and have the item
        if itemChoice == "1" and items[0] > 0:
            # Increases health by 10 and subtracts one items
            pokemon["HP"] += 10
            items[0] -= 1
            print(f"{pokemon["Name"]}'s HP was increased by 10 to {pokemon["HP"]}")
            break

        elif itemChoice == "2" and items[1] > 0:
            # Increases Attack by 10 and subtracts 1 item
            pokemon["AP"] += 10
            items[1] -= 1
            print(f"{pokemon["Name"]}'s AP was increased by 10 to {pokemon["AP"]}")
            break
        elif itemChoice == "3":
            break

def battle():
    turn = 0
    welcome()

    while True:
        turn += 1

        print("-"*50)
        print(f"Turn {turn}")

        # Attacker 1 turn 
        while True:
            print(f"{poke1_dictionary["Name"]}'s turn!")
            choice = printOptions()


            if choice == "1":
                attack(poke1_dictionary,poke2_dictionary,1)
                break
            elif choice == "2":
                print(f"{poke1_dictionary["Name"]} passes turn")
                break

            elif choice == "3":
                useItem(poke1_dictionary,poke1_list)
                break
            
            else:
                print("Not an option!")


        if poke2_dictionary["HP"] <= 0:
            print(f"{poke2_dictionary['Name']} fainted")
            break

        # Attacker 2 turn 
        while True:
            print(f"{poke2_dictionary["Name"]}")
            choice = printOptions()

            if choice == "1":
                attack(poke2_dictionary, poke1_dictionary, 1)
                break
            elif choice == "2":
                print(f"{poke2_dictionary["Name"]} passes turn")
                break

            elif choice == "3":
                useItem(poke2_dictionary,poke2_list)
                break
            
            else:
                print("Not an option!")


        if poke1_dictionary["HP"] <= 0:
            print(f"{poke1_dictionary['Name']} fainted")
            break

def main(): 
    while playing():
        battle()




if __name__ == "__main__":
    main()