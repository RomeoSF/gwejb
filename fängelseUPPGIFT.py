cell_door = "locked"
current_room = None

# Space Prison Escape elr ngt vafan vet jag

def cell_room():
    global cell_door, current_room
    current_room = cell_room
    """Starting room - the prison cell."""
    print("\n--- PRISON CELL ---")
    print("You wake up in a cramped, metallic cell aboard the space station Blackstar.")
    print("The walls are covered with electronic locks and security screens.")
    print("You know you must escape before the next security check.")

    while True:
        print("\nWhat do you want to do?\n")
        print("1. Examine the bed")
        print("2. Check the cell door")
        print("3. Look around the cell")
        print("4. Open menu")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            print("You find a piece of wire under the stained cushions.\nMaybe it's useful for the door?")
            cell_door = "unlocked"
            
        elif choice == "2":
            if cell_door == "unlocked":
                hallway1()
                break
            else:
                print("You look around the cell door giving it a quick tug,\nhowever it's not budging at all")
        elif choice == "3":
            print("You scouer the cell looking for anything useful.\nYou find nothing of use, just plain walls and your bed.")
        elif choice == "4":
            menu()
            break
        else:
            print("Error: Incorrect Command")

def start():
    global current_room
    current_room = start
    print("\n--- START MENU ---")
    print("Welcome to Space Prison Escape!")
    print("You are a prisoner aboard the space station Blackstar.")
    print("Your mission is to escape the station before the next security check.")
    print("Good luck!")
    print("\n1. Start your escape")
    print("2. Exit")

    while True:
        choice = input("Enter your choice (1-2): ")

        if choice == "1":
            cell_room()
            break
        elif choice == "2":
            print("Exiting game. Goodbye!")
            break
        else:
            print("Error: Incorrect Command")

def menu():
    global current_room
    print("\n--- MENU ---")
    print("1. Resume game")
    print("2. Return to start menu")

    while True:
        choice = input("Enter your choice (1-2): ")

        if choice == "1":
            current_room()
            break
        elif choice == "2":
            start()
            break
        else:
            print("Error: Incorrect Command")

def hallway1():
    global current_room
    current_room = hallway1
    print("\n--- Hallway 1 ---")
    print("")

def Security_room():
    global current_room
    current_room = Security_room
    print("\n--- Security room ---")
    print("")

def Logistics():
    global current_room
    current_room = Logistics
    print("\n--- Logistics ---")
    print("")

def Hallway2():
    global current_room
    current_room = Hallway2
    print("\n--- Hallway 2 ---")
    print("")

start()
