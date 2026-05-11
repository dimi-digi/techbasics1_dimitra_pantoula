import time

location = "start"
time.sleep(10)



while True:
  if location == "start":
    print("Welcome to the Lord of the rings game!")
    character = str(input("choose your character: "))

  if character == "Frodo":
    print(r"""you are starting in the Shire                                         __
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
""")
    time.sleep(2)
    print(r"""It is a beautiful sunny morning, birds are chirping and you can hear the sound of the water streaming down gently
    .
      \ | /
    '-.;;;.-'
   -==;;;;;==-
    .-';;;'-.
      / | \
     '
""")
    time.sleep(2)
    print("Everyone is working on their daily chores, but there is an uplifting atmosphere in the air")

  elif character == "Legolas":
    print(r""" You are in Mirkwood!                 [\
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
""")
    time.sleep(2)
    print("You have just got back from hunting orcs around the castle all morning")
    time.sleep(2)
    print("The sky looks strangely dark, the forest gives off sinister vibes and everyone has been warned off not to wander the forest alone")
    time.sleep(2)

  elif character == "Gandalf":
    print(r"""You are in Minas Tirith
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
""")
    time.sleep(2)
    print("You rushed from Rohan to advise King Denethor to protect the city and raise an army against Sauron's dark forces")
    time.sleep(2)
    print("The people of Minar Tirith have no suspected the threat yet and everyone is continuing their day as usual")
    location = "direction1"

  direction1 = str(input("choose the direction you are heading too:"))
  if direction1 == "north":
    print("You are in Hobbiton")
    time.sleep(2)
    print("It's a beautiful sunny day. Birds are chirping, butterflies are chasing each other playfully and the tree branches are dancing to the gentle breeze. You can sense the coming of spring in the air ")
    time.sleep(2)
    print("Bilbo is chilling outside smoking his pipe, creating different shapes and enjoying the sunny weather")
    time.sleep(2)
    print("His birthday is coming up, but he is lately acting very mysterious.Gandalf is suspecting something and has advised you to keep an eye on Bilbo and report back to him when he arrives")
    location = "action"
  elif direction1 == "south":
    print("You are Woodland Realm. A largely underground citycarved into stone halls beneath a hill. Massive doors, often hidden or guarded, lead into a network of long, torch-lit corridors, cavernous halls with carved pillars and storerooms filled with wine and treasure.")
    time.sleep(2)
    print("Thranduil, the King of the Silvan elves is sitting on his throne")
    time.sleep(2)
    print("You have crossed into my halls without leave. Few do so by accident… and fewer still without consequence.")
    print("He is cautious and suspicious of strangers entering the forest. You can feel that he is proud of the Realm but his presence still kind of scares you.")
    location = "action"
  elif direction1 == "east":
    print("You are in the fortress of Dol Guldur")
    time.sleep(2)
    print("It rises like rotting crown of stone on a barren hill. Broken towers claw upward at unnatural angles. Walls are cracked, blackened, and uneven—as if grown rather than built.Narrow windows glow faintly with a sickly green or dull red light.Nothing looks maintained, yet nothing fully collapses either—it lingers")
    time.sleep(2)
    print("Sauron is gathering his forces there. The darkness is preparing to cover the land of Middle Earth once again.")
    time.sleep(2)
    print("A war is brewing up. The skies have become darker and the air is poisoned.")
    location = "action"
  elif direction1 == "west":
    print("You are in the goblins' dungeon. The air is heavy and wrong. A constant dim haze or fog clings to the ground. Light struggles to exist—everything is muted, gray, or greenish. Shadows feel thicker than they should, pooling in corners. You get the sense that sound is swallowed quickly, making everything eerily quiet.")
    time.sleep(2)
    print("Gollum is near you. You can hear him cracking the bones of the fish he catches. Be cautious and try not to make him mad")
    time.sleep(2)
    print("You hear it saying: “What’s thisss? What’s thisss creeping in the dark, eh? Not fish… not nice fish…”")
  else:
    print("invalid input")

  action = str(input("choose an action:"))
  if action == "read":
    print("You are reading a book under a tree")
    time.sleep(2)
    print("Goodbye traveller!")
    break
  elif action == "fight":
    print("You are fighting off some orcs with your sword")
    time.sleep(2)
    print("Goodbye traveller!")
    break
  elif action == "go back":
    print("You are back in Hobbiton")
    time.sleep(2)
    print("Goodbye traveller!")
  elif action == "potion":
    print("You are helping Radagast the Brown to heal some animals in the forest")
    time.sleep(2)
    print("Goodbye traveller!")
    break



 
