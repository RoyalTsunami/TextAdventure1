
import define
stick = False

while True:
    Play = input("""Would you like to play TextAdventures 1? (yes/no) """).lower().strip()
    if Play == "yes":
        print("Welcome to TextAdventures 1!\n"
              "You awaken in a dusty room.\n"
              "Groggy and confused, you can't recall how you got here.\n"
              "You look around and saw a single door in front of you."
              )
        movement = input("Would you like to open the door or continue looking around? "
                         "(open the door/look around) ").lower().strip()
        if movement == "open the door":
            define.showHallWay1()
        elif movement == "look around":
            define.showIntroRoom()
        else:
            print("Invalid choice, please type 'open the door' or 'look around'. Try again.")
            break

    elif Play == "no":
        print("Aww, that's too bad...!")

    else:
        print("Invalid choice, please answer with 'yes' or 'no'.")


