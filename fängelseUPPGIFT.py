cell_door = "locked"


# Space Prison Escape elr ngt vafan vet jag

def cell_room():
    """Starting room - the prison cell."""
    print("\n--- PRISON CELL ---")
    print("You wake up in a cramped, metallic cell aboard the space station Blackstar.")
    print("The walls are covered with electronic locks and security screens.")
    print("You know you must escape before the next security check.")

    while True:
        print("\nWhat do you want to do?")
        print("1. Examine the bed")
        print("2. Check the cell door")
        print("3. Look around the cell")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == 1:
            print("")
            # Fortsättning av val vilket leder till öppnande av dörren
        elif choice == 2:
            print("You look around the cell door, giving it a quick tug\nhowever it's not budging at all")
            return
        elif choice == 3:
            print("")
        else:
            print("Error: Incorrect Command")

def start():
    print("\n--- START ---")

def menu():
    print("\n--- MENU ---")
    menu_choice = input("")

def hallway1():
    print("\n--- Hallway 1 ---")
    print("")

def Security_room():
    print("\n--- Security room ---")
    print("")

def Logistics():
    print("\n--- Logistics ---")
    print("")

def Hallway2():
    print("\n--- Hallway 2 ---")
    print("")


cell_room()