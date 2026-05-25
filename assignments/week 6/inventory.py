import time

inventory = []


items_in_island = [
    {"name": "Torch", "type": "tool", "description": "Signals for help.", "location": "cave"},
    {"name": "Coconut", "type": "food", "description": "Restores a small amount of health.", "location": "jungle"},
    {"name": "Wooden arrow", "type": "tool", "description": "Fight off aggressive creatures.", "location": "ruins"},
    {"name": "Fishing rod", "type": "tool", "description": "Fills up food supplies.", "location": "ocean"},
    {"name": "Boat", "type": "tool", "description": "Abandon the island", "location": "ocean"}
]

current_location = "start"


def show_room_items():
    visible_items = [item for item in items_in_island if item["location"] == current_location]

    print(r"""Here is what you have in front of you:
    ------------------------------------------""")
    if visible_items:
        print("ITEMS AVAILABLE HERE:")
        for item in visible_items:
            print(f"- {item['name']}")
    else:
        print("There are no items on the ground here.")
    print("    -------------------------------------------")


def pick_up(item_name):
    for item in items_in_island:
        if item["name"].lower() == item_name.lower() and item["location"] == current_location:
            inventory.append(item)
            items_in_island.remove(item)
            print(f"You picked up the {item['name']}.")
            return
    print(f"There is no '{item_name}' here to pick up.")


def drop(item_name):
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            item["location"] = current_location
            items_in_island.append(item)
            inventory.remove(item)
            print(f"You dropped the {item['name']}.")
            return
    print(f"You don't have a '{item_name}' in your inventory.")


def use(item_name):
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            print(f"You used the {item['name']}: {item['description']}")
            return
    print(f"You need to pick up the '{item_name}' before you can use it!")


def show_inventory():
    if inventory:
        print(r"""Your Current Inventory:
    ------------------------------------------""")
        for item in inventory:
            print(f"- {item['name']}: {item['description']}")
        print("    -------------------------------------------")
    else:
        print("Your inventory is empty.")


def examine(item_name):
    all_visible_items = items_in_island + inventory
    for item in all_visible_items:
        if item["name"].lower() == item_name.lower():
            print(f"{item['name']}: {item['description']}")
            return
    print(f"You don't see a '{item_name}' anywhere.")


def game_loop():
    global current_location

    print("Welcome to the Inventory Game!")
    print(
        "Welcome to the Hidden Island! You have been stranded after your ship sank into the sea. Choose your actions wisely to survive!")
    print("Type 'help' for a list of commands.")

    while True:
        if current_location == "start":
            print("\nYou are standing on the shoreline. Where do you want to head? (north/south/east/west)")
        else:
            print(f"\n[Location: {current_location.upper()}]")

        command = input("> ").strip().lower()


        match command.split():
            case ["help"]:
                print(
                    "Commands: inventory, look, pickup [item], drop [item], use [item], examine [item], north, south, east, west, quit")
            case ["inventory"]:
                show_inventory()
            case ["look"]:
                show_room_items()


            case ["pickup", *item_words]:
                item_name = " ".join(item_words)
                pick_up(item_name)
            case ["drop", *item_words]:
                item_name = " ".join(item_words)
                drop(item_name)
            case ["use", *item_words]:
                item_name = " ".join(item_words)
                use(item_name)
            case ["examine", *item_words]:
                item_name = " ".join(item_words)
                examine(item_name)

            # NAVIGATION
            case ["north"] | ["go", "north"]:
                current_location = "jungle"
                print("You are in the jungle.")
                time.sleep(2)
                print(
                    "You hear intense growling behind you. You slowly turn around and realise there is a tiger staring at you. What do you do?")

            case ["south"] | ["go", "south"]:
                current_location = "cave"
                print("A dark cave lies before you.")
                time.sleep(2)
                print("You decide to explore it. Maybe use something from your inventory to light it up a bit.")

            case ["east"] | ["go", "east"]:
                current_location = "ocean"
                print("The sea looks so calm and peaceful.")
                time.sleep(2)
                print(
                    "It would be wise to try and catch some fish for dinner tonight. Or are you in the mood to escape?")

            case ["west"] | ["go", "west"]:
                current_location = "ruins"
                print("You found some old ruins.")
                time.sleep(2)
                print(
                    "Questions start to build up in your mind. How long have they been here? What happened to the people or creatures that resided in it? Are they cursed?")

            case ["quit"]:
                print("Thanks for playing!")
                break
            case _:
                print("Unknown command. Type 'help' to see available commands.")


if __name__ == "__main__":
    game_loop()