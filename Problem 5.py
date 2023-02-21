import random

def fruit_machine():
    symbol = ["Cherry", "Bell", "Lemon", "Orange", "Star", "Skull"]
    credit = 1
    while credit >= 0.2:
        print(f"You have {round(credit,2)} credits remaiining")
        roll = input("Do you want to roll the fruit machine or quit?")
        if roll.lower() == "quit":
            break
        credit -= 0.2
        result = [random.choice(symbol) for _ in range(3)]
        print(" ".join(result))
        if result.count(result[0]) == 3:
            if result[0] == "Bell":
                credit += 4.8
                print("You win £5!")
            else:
                credit += -0.8
                print("You won £1")
        elif result.count(result[0]) == 2:
            if result[0] == "Skull":
                credit -= 0.6
                print("You won £1!")
            else:
                credit += 0.3
                print("You won 50p")
        elif result.count("Skull") == 3:
            credit = 0
            print("You lost your money")
    print(f"You have {round(credit,2)} credits remaining")

fruit_machine()
