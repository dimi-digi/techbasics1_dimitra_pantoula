from datetime import datetime
import time


DEBUG = True


def game_sleep(seconds):
    """Bypasses time.sleep if DEBUG is active to accelerate testing."""
    if not DEBUG:
        time.sleep(seconds)


def intro_frodo():
    print(
        r"""you are starting in the Shire                                         __
                 ,-_                  (`  ).
                 |-_'-,              (     ).
                 |-_'-'           _(        '`.
        _        |-_'/        .=(`(      .     )
       /;-,_     |-_'        (     (.__.:-`-_.'
      /-.-;,-,___|'          `(       ) )
     /;-;-;-;_;_/|\_ _ _ _ _   ` __.:'   )
        x_( __`|_P_|`-;-;-;,|        `--'
        |\ \    _||   `-;-;-'
        | \`   -_|.      '-'
        | /   /-_|_ `
        |/   ,'-_|  \
        /____|'-_|___\
 _..,____]__|_\-_'|_|___,.._
'                          ``'--,..,.
"""
    )
    game_sleep(2)
    print(
        r"""It is a beautiful sunny morning, birds are chirping and you can hear the sound of the water streaming down gently
    .
      \ | /
    '-.;;;.-'
   -==;;;;;==-
    .-';;;'-.
      / | \
     '
"""
    )
    game_sleep(2)
    print(
        "Everyone is working on their daily chores, but there is an uplifting atmosphere in the air"
    )
    return 10  # Points awarded for choosing Frodo


def intro_legolas():
    print(
        r""" You are in Mirkwood!                 [\
                  |\)
                  |
                  Y\
                 T  \
                J    \
               Y/T`-._\
               /[|   ]|
               | |    |
   _
  (,,)
             /||.| /\ |
            /_|||| || |
  L/\       | \| | '` |_ _ {|
 /v^v/\/\   `|  Y | [
/ ,'./  \.` |[   |
,'     `    |
--   -----.-(] [ |
   Y Y  --;`~T   |
  Y  YY   ;'~~l  |
 Y  Y Y   ;\~~/\{|
     --   ;\~~~\/|
    _    _; \~~( Y``
   (^)  (^)`._~ /
    Y    Y    `'--..,-'
      --           _
          __   -  (^)  (^)
      _
"""
    )
    game_sleep(2)
    print("You have just got back from hunting orcs around the castle all morning")
    game_sleep(2)
    print(
        "The sky looks strangely dark, the forest gives off sinister vibes and everyone has been warned off not to wander the forest alone"
    )
    return 15  # Points awarded for choosing Legolas


def intro_gandalf():
    print(
        r"""You are in Minas Tirith
                      / \\\
                      |n| |
                    )(|_|-'X
                   /  \\Y// \
                   |A | | |A|
                   |  | | |_|
            )(__X,,|__|MEB;;;-,)(,
           /  \\\;;;;;;;;;;;;/    \
           |A | |            | U  |
         )_|  | |____)-----( |    |
        ///|__|-'////       \\|___)=(__X
       /////////////         \\///   \/ \
       |           |  U    U |//     \u|
       |   )_,-,___|_)=(     | |  U  |_|_X
       |  ///   \\|//   \    | |  __ |/// \
     )_')(//     \Y/     >---)=( /  \\|  | |-----------------..,
    //// ,\ u   u |   u /////   \\|  ||__|A|----------------..,, \,
   |  | .. |      |    ///// ,-, \\__||--------------------..,, \, \,
---'--'_::_|______'----| u | | | |-----------------------..,, \, \, \,
                       |___|_|_|_|----------------------..,, \, \, \ \n                            `--------------------------..,, \, \, \ \\
                                                       \, \, \, \ \ \
                                                         \, \, \, \ \\
                                                           \, \, \, \ \
                                                             \, \, \ \
                                                               \, \ \
                                                                 \ \
                                                                  \
"""
    )
    game_sleep(2)
    print(
        "You rushed from Rohan to advise King Denethor to protect the city and raise an army against Sauron's dark forces"
    )
    game_sleep(2)
    print(
        "The people of Minar Tirith have no suspected the threat yet and everyone is continuing their day as usual"
    )
    return 20  # Points awarded for choosing Gandalf


def intro_arwen():
    print(
        r""" You are in Rivendell                     |>>>                        |>>>
                    |                           |
                _  _|_  _                   _  _|_  _
               | |_| |_| |                 | |_| |_| |
               \  .      /                 \ .    .  /
                \    ,  /                   \    .  /
                 | .   |_   _   _   _   _   _| ,   |
                 |    .| |_| |_| |_| |_| |_| |  .  |
                 | ,   | .    .     .      . |    .|
                 |   . |  .     . .   .  ,   |.    |
     ___----_____| .   |.   ,  _______   .   |   , |---~_____
_---~            |     |  .   /+++++++\    . | .   |         ~---_
                 |.    | .    |+++++++| .    |   . |              ~-_
              __ |   . |   ,  |+++++++|.  . _|__   |                 ~-_
     ____--`~    '--~~__ .    |++++ __|----~    ~`---,              ___^~-__
-~--~                   ~---__|,--~'                  ~~----_____-~'   `~----~
                               ____                                         

"""
    )
    game_sleep(2)
    print(
        "You are surrounded by nine Nazguls. Frodo is slowly dying from his Morgul blade wound"
    )
    game_sleep(2)
    print(
        "You start chanting a spell in Elvish and speaking to the river gods. Congratulations!The river gods heard your call and run over the evil Nazguls."
    )
    game_sleep(2)
    return 25  # Points awarded for choosing Arwen


def navigate_middle_earth():
    direction1 = input(
        "\nChoose the direction you are heading to (north/south/east/west): "
    ).lower()
    if direction1 == "north":
        print("You are in Hobbiton")
        game_sleep(2)
        print(
            "It's a beautiful sunny day. Birds are chirping, butterflies are chasing each other playfully and the tree branches are dancing to the gentle breeze. You can sense the coming of spring in the air "
        )
        game_sleep(2)
        print(
            "Bilbo is chilling outside smoking his pipe, creating different shapes and enjoying the sunny weather"
        )
        game_sleep(2)
        print(
            "His birthday is coming up, but he is lately acting very mysterious.Gandalf is suspecting something and has advised you to keep an eye on Bilbo and report back to him when he arrives"
        )
        return "action", 15
    elif direction1 == "south":
        print(
            "You are Woodland Realm. A largely underground city carved into stone halls beneath a hill. Massive doors, often hidden or guarded, lead into a network of long, torch-lit corridors, cavernous halls with carved pillars and storerooms filled with wine and treasure."
        )
        game_sleep(2)
        print("Thranduil, the King of the Silvan elves is sitting on his throne")
        game_sleep(2)
        print(
            "You have crossed into my halls without leave. Few do so by accident… and fewer still without consequence."
        )
        print(
            "He is cautious and suspicious of strangers entering the forest. You can feel that he is proud of the Realm but his presence still kind of scares you."
        )
        return "action", 20
    elif direction1 == "east":
        print("You are in the fortress of Dol Guldur")
        game_sleep(2)
        print(
            "It rises like rotting crown of stone on a barren hill. Broken towers claw upward at unnatural angles. Walls are cracked, blackened, and uneven—as if grown rather than built.Narrow windows glow faintly with a sickly green or dull red light.Nothing looks maintained, yet nothing fully collapses either—it lingers"
        )
        game_sleep(2)
        print(
            "Sauron is gathering his forces there. The darkness is preparing to cover the land of Middle Earth once again."
        )
        game_sleep(2)
        print("A war is brewing up. The skies have become darker and the air is poisoned.")
        return "action", 35
    elif direction1 == "west":
        print(
            "You are in the goblins' dungeon. The air is heavy and wrong. A constant dim haze or fog clings to the ground. Light struggles to exist—everything is muted, gray, or greenish. Shadows feel thicker than they should, pooling in corners. You get the sense that sound is swallowed quickly, making everything eerily quiet."
        )
        game_sleep(2)
        print(
            "Gollum is near you. You can hear him cracking the bones of the fish he catches. Be cautious and try not to make him mad"
        )
        game_sleep(2)
        print(
            "You hear it saying: “What’s thisss? What’s thisss creeping in the dark, eh? Not fish… not nice fish…”"
        )
        return "action", 25
    else:
        print("invalid input")
        return "action", 0


def act_in_middle_earth():
    action = input(
        "\nChoose an action (read/fight/go back/potion/ring/moth): "
    ).lower()

    if action == "read":
        print("You are reading a book under a tree.")
        game_sleep(2)
        print("Goodbye traveller!")
        return False, 5
    elif action == "fight":
        print("You are fighting off some orcs with your sword!")
        game_sleep(2)
        print("Goodbye traveller!")
        return False, 50
    elif action == "go back":
        print("You are back in Hobbiton.")
        game_sleep(2)
        print("Goodbye traveller!")
        return False, 10
    elif action == "potion":
        print(
            "You are helping Radagast the Brown to heal some animals in the forest."
        )
        game_sleep(2)
        print("Goodbye traveller!")
        return False, 30
    elif action == "ring":
        print(
            "You notice something shiny in the bottom of the river. Something pulls you to it. You haven't seen anything like it."
        )
        game_sleep(2)
        print("Goodbye traveller!")
        return False, 45
    elif action == "moth":
        print(
            "You are asking for help from Lady Galadriel, because you are in danger. A giant hawk is sent to your aid and rescues you."
        )
        game_sleep(2)
        print("Goodbye traveller!")
        return False, 40
    else:
        print("Invalid action. The darkness creeps closer...")
        return "action", -5



location = "start"
game_running = True
score = 0

print("Welcome to the Lord of the Rings game!")

while game_running:

    if location == "start":

        prompt = "Choose your character (Frodo/Legolas/Gandalf/Arwen) or type 'exit': "
        if DEBUG:
            prompt = "Choose your character (Frodo/Legolas/Gandalf/Arwen), 'skip' to end, or type 'exit': "

        character = input(prompt).lower()

        if character == "exit":
            print("Goodbye traveller!")
            break
        elif DEBUG and character == "skip":
            print("Skipping to the end of your adventure...")
            score = 100
            break
        elif character == "frodo":
            score += intro_frodo()
            location = "direction1"
        elif character == "legolas":
            score += intro_legolas()
            location = "direction1"
        elif character == "gandalf":
            score += intro_gandalf()
            location = "direction1"
        elif character == "arwen":
            score += intro_arwen()
            location = "direction1"
        else:
            print("Unknown hero! Middle-earth doesn't recognize you. Try again.")
            location = "start"

    elif location == "direction1":
        location, points = navigate_middle_earth()
        score += points

    elif location == "action":
        result, points = act_in_middle_earth()
        score += points

        if result == False:
            game_running = False
        elif result == "start":
            location = "start"
        else:
            location = "direction1"


if score > 0 or location != "start":
    print("\n==============================")
    print(f"Adventure concluded! Final Score: {score}")
    player_name = input("Enter your name for the record scroll: ").strip()

    if not player_name:
        player_name = "Anonymous Wanderer"

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    with open("geek.txt", "a") as file:
        file.write(f"--- Adventurer Record ---\n")
        file.write(f"Name: {player_name}\n")
        file.write(f"Timestamp: {current_time}\n")
        file.write(f"Score Achieved: {score}\n")
        file.write(f"-------------------------\n\n")


print("File written successfully\n")

print("=== PAST ADVENTURER RECORDS ===")
with open("geek.txt", "r") as f:
        for line in f:
            line = line.replace("\n", "") # remove line breaks from the file
            print(line)