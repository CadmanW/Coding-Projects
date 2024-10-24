# lab4 - student
# updated: 2/8/2024
# name: Cadman Warren
# date: 10/24/2024

# import the random module
import random

## functions

# PLACE ALL FUNCTIONS HERE
def welcome():
    print("Welcome to the Python Pokemon Battle Simulator!")
    print("#" * 50)

def calcDamage(ap, crit=1):
    return (ap - random.randint(1, 5)) * crit

def applyDamage(hp, damage):
    hp -= damage

    if hp <= 0:
        hp = 0

    return hp

def printOutcome(attacker, defender, damage, defender_hp):
    print(f"{attacker} attacks {defender} for {damage} damage.")
    print(f"{defender}'s HP is now {defender_hp}.")
    print()

def printOptions():
    print("Press 1 for Attack")
    print("Press 2 for Pass")

    choice = input("Press 1 or 2 to continue:\n")

    return int(choice)

def playing():
    while True:
        userInput = input("Would you like to start a battle? (y/n): ").lower()

        if userInput == "y":
            play = True
        elif userInput == "n":
            play = False

        return play

def battle():
    # print welcome message
    # <code>
    welcome()

    # pokemon 1 information: name, hit points, attack points
    pokemon_1_name = 'Pikachu'
    pokemon_1_hp = 100  # Hit Points
    pokemon_1_ap = 20   # Attack Points

    # pokemon 2 information: name, hit points, attack points
    pokemon_2_name = 'Charmander'
    pokemon_2_hp = 90
    pokemon_2_ap = 25

    # multiplier for when a critical hit is landed
    crit_multiplier = 1.5

    # set the amount of turns in a variable
    # <code>
    turn = 0

    # for loop to simulate a full battle with turns. use variable for the amount of turns for range
    while True:
        turn += 1

        print("-" * 50) 
        print(f"Turn {turn}")

        ###### attacker 1 turn
        while True:
            print(f"{pokemon_1_name}'s turn!")
            # getting choice for pokemon 1
            choice = printOptions()

            # pokemon_1 attacks pokemon_2
            if choice == 1:
                damage = calcDamage(pokemon_1_ap, crit_multiplier)
                pokemon_2_hp = applyDamage(pokemon_2_hp, damage)
                printOutcome(pokemon_1_name, pokemon_2_name, damage, pokemon_2_hp)
                break

            elif choice == 2:
                print(f"{pokemon_1_name} passes turn")
                break
            
            else:
                print("Not an option!")

        if pokemon_2_hp <= 0:
            print(f"{pokemon_2_name} fainted")
            break

        ###### attacker 2 turn
        while True:
            print(f"{pokemon_2_name}'s turn!")

            # getting choice for pokemon 2
            choice = printOptions()

            # pokemon_2 attacks pokemon_1
            if choice == 1:
                damage = calcDamage(pokemon_2_ap)
                pokemon_1_hp = applyDamage(pokemon_1_hp, damage)
                printOutcome(pokemon_2_name, pokemon_1_name, damage, pokemon_1_hp)
                break
            
            elif choice == 2:
                print(f"{pokemon_1_name} passes turn")
                break
            
            else:
                print("Not an option!")

        if pokemon_1_hp <= 0:
            print(f"{pokemon_1_name} fainted")
            break

        

def main():
    while playing():
        battle()



##################### initiate main
# initiate main this way, as was explained in class
if __name__ == "__main__":
    main()