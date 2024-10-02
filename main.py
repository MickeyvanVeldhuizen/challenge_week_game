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
        elif i == king_position:
            map += "k"
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
def movement(direction, player_position, line_length):
    if direction == "north":
        player_position -= line_length
        if player_position < 0:
            player_position += line_length
            return "out of bounds"
    elif direction == "east":
        player_position += 1
        if player_position % line_length == 0:
            player_position -= 1
            return "out of bounds"
    elif direction == "south":
        player_position += line_length
        if player_position > line_length ** 2:
            player_position -= line_length
            return "out of bounds"
    elif direction == "west":
        player_position -= 1
        if player_position % line_length == line_length - 1:
            player_position += 1
            return "out of bounds"
    else:
        return "invalid input"
    return player_position

# deze functie print de ending die je hebt behaald
def print_ending(ending_number):
    if ending_number == 0:
        print("Heb je wel wat gedaan?")
    if ending_number == 1:
        print("Je bent arm")
    if ending_number == 2:
        print("Je bent rijk")
    if ending_number == 3:
        print("Je hebt niks uit je huis gehaald")

# deze functie bepaalt welke ending je hebt
def ending_check(player_inventory, house_inventory):
    if player_inventory == []:
        ending_number = 1
    if house_inventory == []:
        ending_number = 2
    if player_inventory == ["fish", "sword"] and house_inventory == ["meat", "brick"]:
        ending_number = 3
    return ending_number


print("""In the kingdom of Pythoria, an era of peace has been shattered by a wave of treachery.
A band of ruthless knights, once loyal to the crown, has turned against their king.
Alongside them are fierce dragons that have been awakened from their ancient slumber.
Together, they have stolen the kingdom's wealth, plunging the realm into chaos and despair. 
The King, desperate to restore balance, has called upon you, a brave adventurer, to recover the stolen treasures.
The more gold you return, the greater your reward will be.

With courage in your heart, you set out on a perilous journey to reclaim the riches taken by the enemy. 
But beware—both knights and dragons stand in your way, each more dangerous than the last. 
Only the clever, the bold, and the persistent can hope to succeed.
      
(You should visit the king first.)""")

# dit zijn alle variabelen die in de code worden gebruikt
line_length = 9
move_limit = 100
king_position = line_length // 2
player_position = king_position + line_length
house_position = (line_length ** 2) - (line_length // 2) - 1
npc_positions = [8, 19]
map = set_map(player_position, npc_positions)
print_map(map, line_length)
can_move = True
player_inventory = ["fish", "sword"]
house_inventory = ["meat", "brick"]
empty_inventory = False
empty_house = False
ending_number = 0
player_gold = 0
player_health = 10



# dit is de grote game loop hierbinnen speelt heel het spel zich af (dit wordt nog niet echt gebruikt naast dat het een loop is)
while can_move:
    # dit is de basis keuze: bewegen
    direction = input("Where do you want to go? (North, East, South, West)").lower()
    movement_input = movement(direction, player_position, line_length)
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
        print_ending(ending_check(player_inventory, house_inventory))
    if player_position == king_position:
        if input("Talk to the king? (Yes, No)").lower() == "yes":
            print("""Brave adventurer, our kingdom is in peril.
Our coffers have been emptied, our people live in fear.
The knights who once protected these lands have betrayed us, and the dragons who once slumbered have awoken.
The gold they’ve taken must be returned. As much as you can carry, as much as you can find—bring it back to me.
For every coin you return, a greater reward awaits.
Go now, and may fortune guide your path.""")
    # dit is een check om te kijken of de player bij zijn huis is
    if player_position == house_position:
        # dit zorgt voor het verwerken van "item storage"
        house_input = input("You are at your house, do you want to store or take any items? (Store, Take, No)").lower()
        if player_inventory != []:
            empty_inventory = False
        if empty_inventory and house_input == "store":
            print("Your inventory is empty.")
        # deze while loop is na de keuze van wat je wilt doen bij je huis hier heb je voor "store" gekozen
        while house_input == "store" and not empty_inventory:
            if player_inventory != []:
                empty_inventory = False
                print("What do you want to store?")
                print("Your current inventory is:")
                # dit print de player inventory uit
                for item in player_inventory:
                    print(item)
                store_item = input("Store what? (Either type the name of an item or type \"Nevermind\")").lower()
                if store_item == "nevermind":
                    house_input = "no"
                    continue
                # dit checkt of je het item hebt dat is ingevuld en verplaatst dit gelijk
                if store_item in player_inventory:
                    for item in player_inventory:
                        if item == store_item:
                            player_inventory.remove(item)
                            house_inventory.append(item)
                            print(f"{item} has been stored in your house.")
                else:
                    print("You dont have that item.")
            else:
                print("Your inventory is empty.")
                empty_inventory = True
                continue
            # een vraag of je meer wil "storen"
            store_more = input("Store anything else? (Yes, No)").lower()
            if store_more == "yes":
                house_input = "store"
            if store_more == "no":
                house_input = "no"
        # dit is hetzelfde als "storen" maar dan voor "taken"
        while house_input == "take" and not empty_house:
            if house_inventory != []:
                empty_house = False
                print("What do you want to Take?")
                print("The houses current inventory is:")
                for item in house_inventory:
                    print(item)
                take_item = input("Take what? (Either type the name of an item or type \"Nevermind\")").lower()
                if take_item == "nevermind":
                    house_input = "no"
                    continue
                if take_item in house_inventory:
                    for item in house_inventory:
                        if item == take_item:
                            house_inventory.remove(item)
                            player_inventory.append(item)
                            print(f"{item} has been taken from your house.")
                else:
                    print("That item is not in your house.")
            else:
                print("The house is empty.")
                empty_house = True
                continue
            take_more = input("Take anything else? (Yes, No)").lower()
            if take_more == "yes":
                house_input = "take"
            if take_more == "no":
                house_input = "no"