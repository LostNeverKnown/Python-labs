import random

def menu():
    print("ROCK(1), PAPER(2), SCISSORS(3), or end game (q or quit)")
    print("")
    choice = input("Input: ")
    return choice

def computer(choice, random_computer, name):
    if random_computer == choice:
        print("No one is the winner this time")
    elif random_computer == "1":
        if choice == "2":
            print(f"{name.capitalize()} is the winner this time")
        else:
            print("Computer is the winner")

    elif random_computer == "2":
        if choice == "3":
            print(f"{name.capitalize()} is the winner this time")
        else:
            print("Computer is the winner")

    else:
        if choice == "1":
            print(f"{name.capitalize()} is the winner this time")
        else:
            print("Computer is the winner")
            
    if random_computer == "1":
        print("Computer has ROCK")
    elif random_computer == "2":
        print("Computer has PAPER")
    else:
        print("Computer has SCISSORS")
    print("")

def game():
    print("Welcome to the Game: ROCK-PAPER-SCISSORS!")
    name = input("Enter your name challenger: ")
    choice = 1
    while choice != 0:
        random_computer = random.randint(1,3)
        random_computer = str(random_computer)

        print(f"{name.capitalize()}, what is your choice?")
        choice = menu()

        if choice == "q" or choice == "quit":
            choice = 0
        elif choice == "1" or choice == "2" or choice == "3":
            computer(choice, random_computer, name)
        else:
            print("Wront input! Try again!")
            print("")

if __name__ == "__main__":
    game()