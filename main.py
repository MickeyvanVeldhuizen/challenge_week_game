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
    if direction == "up" or direction == "u":
        player_position -= line_length
        if player_position < 0:
            player_position += line_length
            return "out of bounds"
    elif direction == "right" or direction == "r":
        player_position += 1
        if player_position % line_length == 0:
            player_position -= 1
            return "out of bounds"
    elif direction == "down" or direction == "d":
        player_position += line_length
        if player_position > line_length ** 2:
            player_position -= line_length
            return "out of bounds"
    elif direction == "left" or direction == "l":
        player_position -= 1
        if player_position % line_length == line_length - 1:
            player_position += 1
            return "out of bounds"
    else:
        return "invalid input"
    return player_position


text = [
# 0
"""x = Player
k = King
h = House
n = NPC
o = Empty land
      
      
You start with nothing in your inventory, however there are some starter items in your house.""",
# 1
"""In the kingdom of Pythoria, an era of peace has been shattered by a wave of treachery.
A band of ruthless knights, once loyal to the crown, has turned against their king.
Alongside them are fierce dragons that have been awakened from their ancient slumber.
Together, they have stolen the kingdom's wealth, plunging the realm into chaos and despair. 
The King, desperate to restore balance, has called upon you, a brave adventurer, to recover the stolen treasures.
The more gold you return, the greater your reward will be.

With courage in your heart, you set out on a perilous journey to reclaim the riches taken by the enemy. 
But beware—both knights and dragons stand in your way, each more dangerous than the last. 
Only the clever, the bold, and the persistent can hope to succeed.
      
(You should visit the king first.)""",
# 2
"""With a sword gleaming in your hand and unshakable resolve, you charge at the dragon.

Its eyes narrow as it spots you, but you’re already too close.
You know this is it.
You know you’re going to strike true.

Each step brings you closer to the towering beast, your heart pounding in rhythm with your footsteps.
Your grip tightens on the hilt, the weight of the sword reassuring in your hand.
And then—you swing.

The blade slices through the air, meeting the dragon’s scales with a sharp, ringing impact.
...
For a split second, nothing happens.

Then, the dragon roars in agony.

Your strike has pierced through its thick hide, and you can feel the blade sink deep into its flesh.
The dragon staggers back, fiery eyes wide with shock.

You press forward, unwilling to give it a chance to recover. With a final, powerful strike, you drive the sword home, and the dragon’s roar fades into a gurgling rasp as it collapses before you.

What did you expect? You came here to win.

The dragon lies defeated at your feet, its massive body still and lifeless.
You’ve done it. Against all odds, you’ve won.""",
# 3
"""Armed with nothing but a brick and reckless courage, you rush toward the dragon.

The dragon’s massive eyes lock onto you, but you’re already too close.
You know this is going to work.
You know you’re going to hit it.

With every step, your grip tightens around the brick, the weight of it somehow comforting in your hand.
This is your moment. You raise the brick high, ready to bring it down with everything you’ve got.
And then—you strike.

The brick meets the dragon’s scales.
...
It’s like smashing a pebble against a mountain.

What did you expect? It’s a dragon.

The dragon’s gaze shifts to you, slow and deliberate.
Its jaws begin to open, sparks dancing between its teeth.
For a fleeting moment, you realize how foolish this all was.
There was never a chance.

Before you can react, fire consumes you.""",
# 4
"""Armed with nothing but a brick and reckless courage, you rush toward the dragon.

The dragon’s massive eyes lock onto you, but you’re already too close.
You know this is going to work.
You know you’re going to hit it.

With every step, your grip tightens around the brick, the weight of it somehow comforting in your hand.
This is your moment. You raise the brick high, ready to bring it down with everything you’ve got.
And then—you strike.

The brick meets the dragon’s scales.
...
It’s like smashing a pebble against a mountain.

What did you expect? It’s a dragon.

The dragon’s gaze shifts to you, slow and deliberate.
Its jaws begin to open, sparks dancing between its teeth.
For a fleeting moment, you realize how foolish this all was.
There was never a chance.

Before you can react, fire consumes you.""",
# 5
"""Armed with nothing but a brick and reckless courage, you rush toward the dragon.

The dragon’s massive eyes lock onto you, but you’re already too close.
You know this is going to work.
You know you’re going to hit it.

With every step, your grip tightens around the brick, the weight of it somehow comforting in your hand.
This is your moment. You raise the brick high, ready to bring it down with everything you’ve got.
And then—you strike.

The brick meets the dragon’s scales.
...
It’s like smashing a pebble against a mountain.

What did you expect? It’s a dragon.

The dragon’s gaze shifts to you, slow and deliberate.
Its jaws begin to open, sparks dancing between its teeth.
For a fleeting moment, you realize how foolish this all was.
There was never a chance.

Before you can react, fire consumes you.""",
# 6
"""Brave adventurer, our kingdom is in peril.
Our coffers have been emptied, our people live in fear.
The knights who once protected these lands have betrayed us, and the dragons who once slumbered have awoken.
The gold they’ve taken must be returned. As much as you can carry, as much as you can find—bring it back to me.
For every coin you return, a greater reward awaits.
Go now, and may fortune guide your path.""",
# 7
"""The King gazes at you in astonishment, his eyes wide with disbelief.
'You have slain a dragon?' he exclaims, his voice filled with admiration.
'Your bravery is beyond measure — our kingdom owes you a debt that can never be repaid.""",
# 8
"""With a slab of fresh meat in your hands and a heart pounding with uncertainty, you approach the dragon.

Its fiery eyes lock onto you, but you’re already too close to turn back now.

Step by step, you close the distance between yourself and the towering beast, your every movement slow and deliberate. The dragon’s nostrils flare, catching the scent of the offering. And then—you extend the meat.

The dragon pauses.

For a tense moment, it seems as if nothing will happen. But then, its massive jaws snap shut around the meat, devouring it in a single bite.

The air feels different. The tension breaks.

The dragon, no longer eyeing you as an enemy, lets out a low, rumbling growl and turns its gaze toward the distant mountains. As it flies away, you notice a glimmer of gold where it once stood.

With peace restored, you collect the treasure and turn back toward the village, your mission a success.""",
# 9
"""The King stares at you in stunned disbelief as you recount the tale. 
'You... tamed the dragon?' he murmurs, awe filling his voice. 
'I called upon you to defeat beasts, yet you have shown wisdom beyond any warrior. 
The kingdom is in your debt—our greatest threat has been quelled, not through force, but through cunning."""
]



print(text[0])

print(text[1])

# dit zijn alle variabelen die in de code worden gebruikt
line_length = 9
king_position = line_length // 2
player_position = king_position + line_length
house_position = (line_length ** 2) - (line_length // 2) - 1
npc_positions = {19 : "Dragon"}
map = set_map(player_position, npc_positions)
print_map(map, line_length)
can_move = True
player_inventory = [""]
house_inventory = ["meat", "brick", "sword"]
empty_inventory = False
empty_house = False
ending_number = 0
player_gold = 0
player_health = 10
start_over = False
game_loop = True
first_time_king = True
dragon_tamer = False

# dit is de grote game loop hier binnen speelt het spel zich af
while game_loop:
    while not start_over:
        while can_move:
            # dit is de basis keuze: bewegen
            direction = input("Where do you want to go? (Up, Right, Down, Left)").lower()
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
                npc = npc_positions[player_position]
                print(f"A {npc} has appeared!")
                in_interaction = True
                while in_interaction:
                    npc_decision = input("What would you like to do? (Fight, Talk, Run)").lower()
                    if npc == "Dragon":
                        have_sword = False
                        have_brick = False
                        have_meat = False
                        for item in player_inventory:
                            if item == "sword":
                                have_sword = True
                            elif item == "brick":
                                have_brick = True
                            elif item == "meat":
                                have_meat = True
                        if npc_decision == "fight":
                            in_interaction = False
                            if have_sword:
                                print(text[2])
                                print("You've earned 10 gold!")
                                player_gold += 10
                                del npc_positions[19]
                            elif have_brick:
                                print(text[3])
                                print("You died.")
                                print("You got the \"Reckless courage\" ending. (What were you thinking?)")
                                can_move = False
                                if input("Try again? (Yes, No)").lower() == "yes":
                                    start_over = True
                                else:
                                    exit()
                            else:
                                print(text[4])
                                print("You died.")
                                print("You got the \"Reckless courage\" ending. (What were you thinking?)")
                                can_move = False
                                if input("Try again? (Yes, No)").lower() == "yes":
                                    start_over = True
                                else:
                                    exit()
                        elif npc_decision == "talk":
                            if not have_meat:
                                in_interaction = False
                                print(text[5])   
                                print("You died.")
                                print("You got the \"Dragon whisperer\" ending. (Did you think that would work?)")
                                can_move = False
                                if input("Try again? (Yes, No)").lower() == "yes":
                                    start_over = True
                                else:
                                    exit()
                            elif have_meat:
                                in_interaction = False
                                dragon_tamer = True
                                print(text[8])
                                print("You've earned 10 gold!")
                                player_gold += 10
                                del npc_positions[19]
                        elif npc_decision == "run":
                            in_interaction = False
                            continue
                        else:
                            print("Invalid input.")
                            continue

            if player_position == king_position:
                if input("Talk to the king? (Yes, No)").lower() == "yes":
                    if first_time_king:
                        print(text[6])
                        first_time_king = False
                    else:
                        end_game_input = input("Do you want to turn in your gold? (Yes, No)(This will end the game.)").lower()
                        if end_game_input == "yes":
                            if player_gold == 10 and not dragon_tamer:
                                print(text[7])
                                print("You got the \"Dragon killer\" ending. (You have slain a dragon!)")
                                can_move = False
                                if input("Try again? (Yes, No)").lower() == "yes":
                                    start_over = True
                                else:
                                    exit()
                            
                            elif player_gold == 10 and dragon_tamer:
                                print(text[9])
                                print("You got the \"How to tame a dragon?\" ending. (Snacks over swords!)")
                                can_move = False
                                if input("Try again? (Yes, No)").lower() == "yes":
                                    start_over = True
                                else:
                                    exit()

                            elif player_gold < 10:
                                print("Did you even do anything?")
                                print("You got the \"Speedrun?\" ending. (Did you even play the game?)")
                                can_move = False
                                if input("Try again? (Yes, No)").lower() == "yes":
                                    start_over = True
                                else:
                                    exit()
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
    else:
        print(text[7])

        # dit zijn alle variabelen die in de code worden gebruikt
        line_length = 9
        move_limit = 100
        king_position = line_length // 2
        player_position = king_position + line_length
        house_position = (line_length ** 2) - (line_length // 2) - 1
        npc_positions = {19 : "Dragon"}
        map = set_map(player_position, npc_positions)
        print_map(map, line_length)
        can_move = True
        player_inventory = [""]
        house_inventory = ["meat", "brick", "sword"]
        empty_inventory = False
        empty_house = False
        ending_number = 0
        player_gold = 0
        player_health = 10
        start_over = False
        first_time_king = True
        dragon_tamer = False
