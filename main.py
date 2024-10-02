# deze function maakt de map op basis van waar de player is en waar de npcs zijn
def set_map(player_position, npc_positions):
    map = []
    for i in range(line_length ** 2):
        if i == player_position:
            map += "x"
        elif i in npc_positions:
            map += "n"
        elif i == house_position:
            map += "h"
        else:
            map += "o"
    return map

# deze functie print de map in een grid waardoor dit beter te lezen is
def print_map(map_list, line_length):
    line = ""
    for char in map_list:
        line += char
        line += " "
        if len(line) == line_length * 2:
            print(line)
            line = ""

# deze functie zorgt voor het verwerken van de movement input
def movement(direction, player_position):
    if direction == "north":
        player_position -= 5
        if player_position < 0:
            player_position += 5
            return "out of bounds"
    elif direction == "east":
        player_position += 1
        if player_position % 5 == 0:
            player_position -= 1
            return "out of bounds"
    elif direction == "south":
        player_position += 5
        if player_position > 25:
            player_position -= 5
            return "out of bounds"
    elif direction == "west":
        player_position -= 1
        if player_position % 5 == 4:
            player_position += 1
            return "out of bounds"
    else:
        return "invalid input"
    return player_position

# dit zijn alle variabelen die in de code worden gebruikt
line_length = 5
move_limit = 100
player_position = (line_length ** 2) - (line_length // 2) - 1
house_position = (line_length ** 2) - (line_length // 2) - 1
npc_positions = [8, 19]
map = set_map(player_position, npc_positions)
print_map(map, line_length)
can_move = True
player_inventory = ["fish", "sword"]
house_inventory = ["meat", "brick"]
empty_inventory = False

# dit is de grote game loop hierbinnen speelt heel het spel zich af (dit wordt nog niet echt gebruikt naast dat het een loop is)
while can_move:
    # dit is de basis keuze: bewegen
    direction = input("Where do you want to go? (North, East, South, West)").lower()
    movement_input = movement(direction, player_position)
    if movement_input == "out of bounds":
        print("Cant go that way!")
    elif movement_input == "invalid input":
        print("Invalid input, try again. (North, East, South, West)")
    else:
        player_position = movement_input
    # hier wordt de map met de nieuwe player position geprint
    print_map(set_map(player_position, npc_positions), line_length)
    # dit is een check of er een npc op dezelfde tile is als de player
    if player_position in npc_positions:
        print("Someone is here!")
    # dit is een check om te kijken of de player bij zijn huis is
    if player_position == house_position:
        # dit zorgt voor het verwerken van "item storage"
        store_items_input = input("You are at your house, do you want to store or take any items? (Store, Take, No)").lower()
        if player_inventory != []:
            empty_inventory = False
        if empty_inventory and store_items_input == "store":
            print("Your inventory is empty.")
        while store_items_input == "store" and not empty_inventory:
            if player_inventory != []:
                empty_inventory = False
                print("What do you want to store?")
                print("Your current inventory is:")
                for item in player_inventory:
                    print(item)
                store_item = input("Store what? (Either type the name of an item or type \"Nevermind\")").lower()
                if store_item in player_inventory:
                    for item in player_inventory:
                        if item == store_item:
                            player_inventory.remove(item)
                            house_inventory.append(item)
                            print(f"{item} has been stored in your house.")
            else:
                print("Your inventory is empty.")
                empty_inventory = True
                continue
            store_more = input("Store anything else? (Yes, No)").lower()
            if store_more == "yes":
                store_items_input = "store"
            if store_more == "no":
                store_items_input = "no"



