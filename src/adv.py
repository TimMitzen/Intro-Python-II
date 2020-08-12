from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


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
# Main1
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])
directions = ['n', 's' , 'e', 'w']


# Write a loop that:
while True:

# * Prints the current room name
    print(f'{player.current_room}\n')
# * Prints the current description (the textwrap module might be useful here). strip, removes whitespace, lower allows upper and lower,[0] so its not a list
    user_input = input('Please input a direction to go. For north use `n`, For south use `s`, for east `e` and for west use `w` to quit hit `q` \n').strip().lower().split()[0]
    # jus using for char
    user_input = user_input[0]

    if user_input in directions:
        #see if we can go that way
        player.move_direction(user_input)

    if user_input == 'q':
        break
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
