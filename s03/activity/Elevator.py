Floors = ["ground", "1st", "2nd", "3rd", "4th", "5th",
             "6th", "7th", "8th", "9th", "10th",
             "11th", "12th", "13th", "14th", "15th", "Exit"]
currentFloor = 0

while (True):
    userInput = int(input(f"Which floor you want to go to? (0 - 15) "))
    userInput = 0 if userInput < 0 else userInput
    userInput = 15 if userInput > 15 else userInput


    while currentFloor != userInput:
        currentFloor = currentFloor + 1 if currentFloor < userInput else currentFloor - 1
        print("----------------------------")
        print("|                          |")
        print("|                          |")
        print(f" You're here at {Floors[currentFloor]} floor.")
        print("|                          |")
        print("|                          |")
        print("----------------------------")

        if currentFloor == userInput:
            print("---------------------------------------")
            print("|                                     |")
            print(f"You reached your destination {Floors[currentFloor]} floor.")
            print("|                                     |")
            print("---------------------------------------")

    userInput = str(input("Do you want to continue? (y / n) "))
    if userInput == "y":
        continue
    else:
        break
