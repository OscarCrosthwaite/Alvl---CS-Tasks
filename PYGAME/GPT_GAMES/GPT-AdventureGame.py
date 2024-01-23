class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        self.items = []

    def add_paths(self, paths):
        self.paths.update(paths)

    def add_item(self, item):
        self.items.append(item)


class GameMap:
    def __init__(self, start_room):
        self.rooms = {}
        self.start_room = start_room

    def add_room(self, room):
        self.rooms[room.name] = room

    def next_room(self, room_name):
        return self.rooms.get(room_name)

    def opening_room(self):
        return self.next_room(self.start_room)


central_corridor = Room("Central Corridor",
                        "You are in the central corridor. There are doors to your left and right.")
armory = Room("Armory",
              "You are in the armory. You see a bunch of weapons.")
bridge = Room("Bridge",
              "You are at the bridge. It's the control center of the spaceship.")
escape_pod = Room("Escape Pod",
                  "You're at the escape pod. Choose one of the pods to escape.")

# Define the paths/connections between rooms
central_corridor.add_paths({"left": armory, "right": bridge})
armory.add_paths({"right": central_corridor})
bridge.add_paths({"left": central_corridor})
bridge.add_paths({"down": escape_pod})
escape_pod.add_paths({})

# Add items to rooms
armory.add_item("Laser Gun")
bridge.add_item("Access Card")

# Create the game map and set the starting room
game_map = GameMap("Central Corridor")
game_map.add_room(central_corridor)
game_map.add_room(armory)
game_map.add_room(bridge)
game_map.add_room(escape_pod)


def play_game():
    current_room = game_map.opening_room()
    inventory = []

    while True:
        print("\n" + current_room.description)

        # Display items in the room
        if current_room.items:
            print("You see: " + ', '.join(current_room.items))

        next_move = input("What do you do? ").lower()

        if next_move == "quit":
            print("Thanks for playing!")
            break

        if next_move in current_room.paths:
            current_room = current_room.paths[next_move]
        else:
            print("Invalid choice. Try again!")

        # Check for items in the room and add them to inventory
        if "take" in next_move and "item" in next_move:
            item = next_move.split()[-1]
            if item in current_room.items:
                inventory.append(item)
                current_room.items.remove(item)
                print(f"You have taken {item}.")

        # Check for specific actions or puzzles
        if current_room.name == "Escape Pod" and "access card" in inventory:
            print("Congratulations! You escaped successfully.")
            break


play_game()