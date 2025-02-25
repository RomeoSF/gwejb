import random

cell_door = "locked"
current_room = None
sec_code = random.randint(1000, 9999)

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
            print("You examine the bed, it's filthy and uncomfortable.\nAll you have is a thin blanket and a pillow.")
            choice = input("Do you want to check under the pillow? (y/n): ").lower()
            if choice == "y":
                print("You find a piece of wire under the stained pillow.\nMaybe it's useful for the door?")
                cell_door = "unlocked"
            elif choice == "n":
                print("You decide to leave the pillow alone.")
            else:
                print("Error: Incorrect Command")
            
        elif choice == "2":

            if cell_door == "unlocked":
                print("\nYou use the piece of wire and your saliva to fry the electronic lock.\nIt opens with a loud creaking sound.")
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
    print("You are in a dimly lit hallway. There are doors leading to different rooms.\n'Jesus fucking christ, this hallway smells like a fucking sewer.' you think to yourself.")
    
    while True:
        print("\nWhat do you want to do?\n")
        print("1. Enter the break room")
        print("2. Go back to your cell")
        print("3. Go to the scrubber room")
        print("4. Open menu")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            break_room()
            break
        elif choice == "2":
            cell_room()
            break
        elif choice == "3":
            scrubber_room()
        elif choice == "4":
            menu()
            break
        else:
            print("Error: Incorrect Command")

def break_room():
    global current_room
    current_room = break_room
    print("\n--- Break room ---")
    print("You are in the break room. There are some tables and chairs scattered around.")
    
    while True:
        print("\nWhat do you want to do?\n")
        print("1. Search the room")
        print("2. Go to the security room")
        print("3. Go back to the hallway")
        print("4. Open menu")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            print("You search the room but find nothing useful.")
        elif choice == "2":
            print("You try to open the door to the security room, but it's locked.\nTheres a keypad next to the door.")
            choice = input("Do you want to try to enter the code? (y/n): ").lower()
            if choice == "y":
                code = input("Enter the 4-digit code: ")
                if code == str(sec_code):
                    Security_room()
                    break
                else:
                    print("The code is incorrect.")
            elif choice == "n":
                print("You decide to leave the door alone.")
            else:
                print("Error: Incorrect Command")
        elif choice == "3":
            hallway1()
            break
        elif choice == "4":
            menu()
            break
        else:
            print("Error: Incorrect Command")

def Security_room():
    global current_room
    current_room = Security_room
    print("\n--- Security room ---")
    print("You are in the security room. There are monitors showing different parts of the station.")
    
    while True:
        print("\nWhat do you want to do?\n")
        print("1. Search the room")
        print("2. Go back to the break room")
        print("3. Open menu")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            print("You search the room but find nothing useful.")
        elif choice == "2":
            break_room()
            break
        elif choice == "3":
            menu()
            break
        else:
            print("Error: Incorrect Command")

def Logistics():
    global current_room
    current_room = Logistics
    print("\n--- Logistics ---")
    print("")

def Hallway2():
    global current_room
    current_room = Hallway2

def escape_pod_launchers():
    global current_room
    current_room = escape_pod_launchers

def scrubber_room():
    global current_room
    current_room = scrubber_room

start()