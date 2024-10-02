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
    if direction == "north" or direction == "n":
        player_position -= line_length
        if player_position < 0:
            player_position += line_length
            return "out of bounds"
    elif direction == "east" or direction == "e":
        player_position += 1
        if player_position % line_length == 0:
            player_position -= 1
            return "out of bounds"
    elif direction == "south" or direction == "s":
        player_position += line_length
        if player_position > line_length ** 2:
            player_position -= line_length
            return "out of bounds"
    elif direction == "west" or direction == "w":
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



print("""x = Player
k = King
h = House
n = NPC
o = Empty land
      
      
You start with nothing in your inventory, however there are some starter items in your house.""")

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
npc_positions = {8 : "Knight",
                  19 : "Dragon"}
map = set_map(player_position, npc_positions)
print_map(map, line_length)
can_move = True
player_inventory = ["fish"]
house_inventory = ["meat", "brick", "sword"]
empty_inventory = False
empty_house = False
ending_number = 0
player_gold = 0
player_health = 10
start_over = False
game_loop = True

while game_loop:
    while not start_over:
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
                npc = npc_positions[player_position]
                print(f"A {npc} has appeared!")
                npc_decision = input("What would you like to do? (Fight, Talk, Run)").lower()
                in_interaction = True
                while in_interaction:
                    if npc == "Dragon":
                        if npc_decision == "fight":
                            in_interaction = False
                            have_sword = False
                            have_brick = False
                            for item in player_inventory:
                                if item == "sword":
                                    have_sword = True
                                elif item == "brick":
                                    have_brick = True
                            if have_sword:
                                print("""With a sword gleaming in your hand and unshakable resolve, you charge at the dragon.

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
You’ve done it. Against all odds, you’ve won.""")
                                print("You've earned 10 gold!")
                                player_gold += 10
                                del npc_positions[19]
                            elif have_brick:
                                print("""Armed with nothing but a brick and reckless courage, you rush toward the dragon.

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

Before you can react, fire consumes you.""")
                                print("You died.")
                                print("You got the \"Reckless courage\" ending. (What were you thinking?)")
                                can_move = False
                                if input("Try again? (Yes, No)").lower() == "yes":
                                    start_over = True
                                else:
                                    exit()
                            else:
                                print("""With nothing but your fists and a heart full of reckless courage, you charge at the dragon.

As the distance between you closes, you notice the dragon’s eyes lock onto you.
But it’s too late for him to react. You know you’ll land this hit.
You know it’s going to work.

With each step, your resolve hardens. You gather all your strength, your fist drawn back, ready to strike.
And then—you’re there.

You swing with everything you have, driving your punch into the dragon’s side.
...
It feels like slamming into a brick wall.

What did you expect? It’s a dragon.

The beast stares down at you, its massive maw opening slowly.
Sparks flicker to life around its fangs, and in that instant, you realize the truth.
This was never a fight you could win.

In a flash, flames engulf you..""")
                                print("You died.")
                                print("You got the \"Reckless courage\" ending. (What were you thinking?)")
                                can_move = False
                                if input("Try again? (Yes, No)").lower() == "yes":
                                    start_over = True
                                else:
                                    exit()
                        elif npc_decision == "talk":
                                in_interaction = False
                                print("""With nothing but your voice and a desperate hope for peace, you approach the dragon.

Its colossal form towers above you, eyes glowing like embers in the dark. You swallow hard, but you keep walking, your hands raised in a gesture of surrender.
You have no weapon, only words.

'We don’t have to do this,' you say, your voice trembling but steady.
The dragon’s gaze shifts to you, a low rumble escaping its throat.

You take a deep breath, trying to sound calm.
'Maybe we can find another way,' you plead. 'I’m not here to fight.'

For a moment, the dragon does nothing. Its massive head tilts slightly, as if considering your words. Hope flickers in your chest.
Maybe—just maybe—it understands.

But then, the dragon snorts, a cloud of smoke billowing from its nostrils.
Its eyes narrow, and a deep, guttural growl reverberates through the air.

You freeze as realization dawns.

It doesn’t care.

Before you can even react, the dragon’s jaws snap open, and you see the telltale flicker of flames within its maw.

Your words were meaningless.

In an instant, a torrent of fire surges toward you, and your last thought is that you never stood a chance.""")   
                                print("You died.")
                                print("You got the \"Dragon whisperer\" ending. (Did you think that would work?)")
                                can_move = False
                                if input("Try again? (Yes, No)").lower() == "yes":
                                    start_over = True
                                else:
                                    exit()
                        elif npc_decision == "run":
                            in_interaction = False
                            continue
                        else:
                            print("Invalid input.")

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
    else:
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
        npc_positions = {8 : "Knight",
                        19 : "Dragon"}
        map = set_map(player_position, npc_positions)
        print_map(map, line_length)
        can_move = True
        player_inventory = ["fish"]
        house_inventory = ["meat", "brick", "sword"]
        empty_inventory = False
        empty_house = False
        ending_number = 0
        player_gold = 0
        player_health = 10
        start_over = False
