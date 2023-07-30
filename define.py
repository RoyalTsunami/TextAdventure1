rope = False
key = False


def showIntroRoom():
    global rope
    print(
        "You look around the room to see cobwebs embracing the corners and "
        "dusty books resting on sagging shelves.\n"
        "Sunlight filters through cracked windows, "
        "illuminating motes dancing in the air. \n"
    )
    if not rope:
        print("In the dimmest corner, a bundle of rope catches your eye.")
        movement = input("Would you like to pick up the rope? (yes/no) ").lower().strip()

        if movement == "yes":
            rope = True
            print("You pick up the rope and left the room.")
            showHallWay1()
        elif movement == "no":
            print("What could a rope do anyways? You ignored it and left the room.")
            showHallWay1()
        else:
            print("Invalid choice, please answer with 'yes' or 'no'. Try again.")

    else:
        print("There is nothing of interest in this room. You proceed to leave.")
        showHallWay1()


def showHallWay1():
    print("You find yourself at the beginning of a hallway.\n"
          "There are two doors, "
          "one of which leads to the room you woke up in.")
    movement = input("Would you like to go back to where you started, "
                     "explore the other room,\n"
                     "or continue down the hallway? (back/explore/continue)").lower().strip()
    if movement == "back":
        showIntroRoom()
    elif movement == "explore":
        showNextRoom()
    elif movement == "continue":
        showHallWay2()
    else:
        print("Invalid choice, please type 'back', 'explore', or 'continue'. Try again.")


def showNextRoom():

    global key
    print(
        "You enter the room to find a single empty vase sitting on a table.\n"
    )
    if not key:
        print("Maybe you should check to see if the vase is truly empty.")
        movement = input("Would you like to search the vase? (yes/no) ").lower().strip()

        if movement == "yes":
            print("As you approached the vase, you catch a glimpse of a shadow dancing on the walls,\n"
                  "but as quickly as it appeared, it vanished into thin air. An eerie chill crept down your spine.")
            movement = input("Would you still like to search the vase? (yes/no) ").lower().strip()
            if movement == "yes":
                print("You brush aside the feeling of uneasiness and proceed forward.\n"
                      "You find a golden key sitting at the bottom of the vase and picked it up.\n"
                      "The room is now empty. You leave the room.")
                key = True
                showHallWay1()
            elif movement == "no":
                print("Feeling a sense of uneasiness, you quickly left the room.\n")
                showHallWay1()
            else:
                print("Invalid choice, please type 'back', 'explore', or 'continue'. Try again.")

        elif movement == "no":
            print("Nothing could possibly be inside a vase. You proceed to leave the room.")
            showHallWay1()

        else:
            print("Invalid choice, please answer with 'yes' or 'no'. Try again.")

    else:
        print("A growing sense of discomfort crept over me as I entered the room.\n"
              "You proceed to leave, eager to escape the eerie atmosphere.")
        showHallWay1()


def showHallWay2():
    print("You find yourself at the end of a hallway.\n"
          "There are three doors. ")
    movement = input("Would you like to open door 1, 2, 3,"
                     "or walk back up the hallway? (1/2/3/back)").lower().strip()
    if movement == "back":
        showHallWay1()
    elif movement == "1":
        showRoom1()
    elif movement == "2":
        showExit1()
    elif movement == "3":
        showRoom2()
    else:
        print("Invalid choice, please type '1', '2', '3', or 'back'. Try again.")


def showRoom1():
    print("You opened the door and it leads to another room. As you stepped inside,\n"
          "your heart skipped a beat as the floor beneath you creaked and shifted ever so slightly.\n")
    movement = input("Would you like to continue going inside the room? (yes/no) ").lower().strip()
    if movement == "yes":
        print("You steeled yourself and entered the room anyways.\n"
              "With a sudden jolt, the floor gave way beneath you and you plummeted to the bottom.\n"
              "You landed on the sharp edge of a debris and your fate was sealed by the unforgiving injury.\n"
              "You lost."
              )
    elif movement == "no":
        print("You decided against entering, recognizing the perilous state of the unstable floor,\n"
              "and opting for safety rather than risking a potentially dangerous venture.")
        showHallWay2()
    else:
        print("Invalid choice, please answer with 'yes' or 'no'. Try again.")


def showRoom2():

    print(
        "You opened the door to reveal a grand piano bathed in gentle sunlight by the window.\n"
        "Despite its apparent abandonment, the piano stood as a magnificent centerpiece in pristine condition."
    )
    movement = input("Would you like to observe the piano more closely,\n"
                     "approach the window, or leave. (piano/window/leave) ").lower().strip()

    if movement == "piano":
        playPiano()

    elif movement == "window":
        showExit2()

    elif movement == "leave":
        showHallWay2()

    else:
        print("Invalid choice, please answer with 'piano', 'window', or 'leave'. Try again.")


def showRoom22():
    movement = input("Would you like to observe the piano,\n"
                     "approach the window, or leave. (piano/window/leave) ").lower().strip()

    if movement == "piano":
        playPiano()

    elif movement == "window":
        showExit2()

    elif movement == "leave":
        showHallWay2()

    else:
        print("Invalid choice, please answer with 'piano', 'window', or 'leave'. Try again.")


def playPiano():
    print("You approached the piano and took a seat in front of its elegant frame.")
    movement = input("Would you like to play the piano? (yes/no) ").lower().strip()
    if movement == "yes":
        print("Fingers delicately grazing the ivory keys, you began to play the piano, \n"
              "breathing life into the forgotten instrument as its enchanting melody filled the abandoned room.\n"
              "As the final notes resonated in the air, you felt a deep sense of satisfaction wash over you.\n"
              "You stood up from the seat.")
        showRoom22()
    elif movement == "no":
        print("Despite the temptation to play, I decided against it, \n"
              "preserving the solemn ambiance of the abandoned room\n"
              "You stood up from the seat.")
        showRoom22()
    else:
        print("Invalid choice, please answer with 'yes' or 'no'. Try again.")


def showExit2():
    print("You made your way to the window and gazed down.\n"
          "It seems that this window is situated right above a cliff.\n"
          "You could possibly use this window as a means of escape.")
    if rope:
        movement = input("Would you like to attempt to escape? (yes/no) ").lower().strip()
        if movement == "yes":
            movement = input("Would you like to use the rope or to just jump down? (rope/jump) ").lower().strip()
            if movement == "rope":
                print("You extend the rope you found and carefully secured one end.\n"
                      "You descended from the window and reached the bottom of the cliff safely.\n"
                      "You finally escaped, only to find yourself surrounded by an unfamiliar forest!\n"
                      "Anyways, you win TextAdventures 1!")

            elif movement == "jump":
                print("You embraced your inner action hero and threw the rope aside.\n"
                      "You leaped out of the window, expecting a heroic landing, but instead broke both your legs.\n"
                      "You look around for help but find yourself surrounded by an unfamiliar forest.\n"
                      "Without any ways to move, you died due to blood loss.")

            else:
                print("Invalid choice, please answer with 'rope' or 'jump'. Try again.")

        elif movement == "no":
            print("The window seems too high up. You'll surely sustain an injury.\n"
                  "Maybe there is another safer way to escape.\n"
                  "You step away from the window.")
            showRoom22()

        else:
            print("Invalid choice, please answer with 'yes' or 'no'. Try again.")

    else:
        movement = input("Would you like to attempt to escape? (yes/no) ").lower().strip()
        if movement == "yes":
            print("You decided that this could be your only chance of escape and took a leapt of faith.\n"
                  "As you hit the ground, a sharp pain shot through your legs.\n"
                  "The impact seemed to have given you multiple fractures.\n"
                  "You look around for help but find yourself surrounded by an unfamiliar forest.\n"
                  "Without any ways to move, you died due to blood loss.")

        elif movement == "no":
            print("The window seems too high up. You'll surely sustain an injury.\n"
                  "Maybe there is another safer way to escape.\n"
                  "You step away from the window.")
            showRoom22()

        else:
            print("Invalid choice, please answer with 'yes' or 'no'. Try again.")


def showExit1():
    print("You reached out to open the door but found it locked.\n")
    if key:
        movement = input("You remember that you picked up a key.\n"
                         "Would you like to use it? (yes/no) ").lower().strip()
        if movement == "yes":
            print("You used the key and it opened the lock.\n"
                  "It reveals a path to an unfamiliar forest. But that's not the point here.\n"
                  "You have finally escaped this place! You win!")

        elif movement == "no":
            print("Curiosity kills the cat, you thought.\n"
                  "Who knows what weird traps may be behind this door, am I right?\n"
                  )
            showHallWay2()

        else:
            print("Invalid choice, please answer with 'yes' or 'no'. Try again.")

    else:
        print("Maybe there is a key somewhere here that could open the door.")
        showHallWay2()
