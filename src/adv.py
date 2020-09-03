from room import Room
from player import Player
from item import Item

import sys

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", 'outside'),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", 'foyer'),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", 'overlook'),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", 'narrow'),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! I think there might be something here!""", 'treasure'),
}

# print(room['outside'])
# Link rooms together




room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('Jazmine' , room['outside'])




# make items for the rooms

gold = Item('Gold' , 'A treat for all your hard work')
machete = Item('Machete' , 'A tool left by another adventurer')
sword = Item('Sword' , ' this sword is made from dragon bones')
bow = Item('Bow and Arrow' , 'Those skilled find this to be an advantage')
treasure_chest = Item('Treasure Chest', 'You have found the ultimate prize!')

items = [gold , machete, sword, bow, treasure_chest]


room['narrow'].items.append(str(gold))
room['outside'].items.append(str(machete))
room['outside'].items.append(str(sword))
room['outside'].items.append(str(bow))
room['treasure'].items.append(str(treasure_chest))





# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

items = [gold , machete, sword, bow, treasure_chest]
directions = ['n', 's', 'e', 'w']

#    def get_items(item):
#         if item in ['gold ', 'machete', 'sword', 'bow', 'treasure_chest']



print(player.room)




while True:
    print(player)
    command = input("What would you like to do?: ")

    if command in directions:
        player.move(command)
    
    elif command == 'q':
        print('Your quest has ended')
        break




    if player.room.location == 'narrow' and command == 'get gold':
        player.on_take(gold)
        room['narrow'].items.remove(str(gold))
        
    elif player.room.location == 'outside' and command == 'get sword':
        player.on_take(sword)
        room['outside'].items.remove(str(sword))
    elif player.room.location == 'outside' and command == 'get bow and arrow':
        player.on_take(bow)
        room['outside'].items.remove(str(bow))
    elif player.room.location == 'outside' and command == 'get machete':
        player.on_take(machete)
        room['outside'].items.remove(str(machete))
    elif player.room.location == 'treasure' and command == 'get treasure chest':
        player.on_take(treasure_chest)
        room['treasure'].items.remove(str(treasure_chest))
    elif player.room.location == 'narrow' and command == 'drop gold':
        player.on_drop(gold)
        room['narrow'].items.append(str(gold))
        
    elif player.room.location == 'outside' and command == 'drop sword':
        player.on_drop(sword)
        room['outside'].items.append(str(sword))
    elif player.room.location == 'outside' and command == 'drop bow and arrow':
        player.on_drop(bow)
        room['outside'].items.append(str(bow))
    elif player.room.location == 'outside' and command == 'drop machete':
        player.on_drop(machete)
        room['outside'].items.append(str(machete))
    elif player.room.location == 'treasure' and command == 'drop treasure chest':
        player.on_drop(treasure_chest)
        room['treasure'].items.append(str(treasure_chest))
        
        
    


