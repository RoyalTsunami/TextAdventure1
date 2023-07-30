
import define

while True:
    choice = None
    while choice is None:
        Play = input("""Would you like to play TextAdventures 1? (yes/no) """).lower().strip()
        if Play == "yes":
            choice = "yes"
            print("Welcome to TextAdventures 1!\n"
                  "You awaken in a dusty room.\n"
                  "Groggy and confused, you can't recall how you got here.\n"
                  "You look around and saw a single door in front of you."
                  )
            define.playGame()

        elif Play == "no":
            choice = "no"
            print("Aww, that's too bad...!")

        else:
            print("Invalid choice, please answer with 'yes' or 'no'.")


