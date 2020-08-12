from room import Room

# Declare all the rooms


outside = Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons")
foyer = Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""")

overlook = Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")

narrow =  Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""")

treasure = Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")



# Link rooms together

outside.n_to = foyer
foyer_to = outside
foyer.n_to = overlook
foyer.e_to = narrow
overlook.s_to = foyer
narrow.w_to = foyer
narrow.n_to = treasure
treasure.s_to = narrow

#
# Main1
#

# Make a new player object that is currently in the 'outside' room.
new_player_object = room
user_input = input('Please input a direction to go. For north use `n`, For south use `s`, for east `e` and for west use `w`'
                   'to quit hit `q` ')

# Write a loop that:
while
#
# * Prints the current room name
if room == 'foyer' :
    print('You are in the foyer')
if room == 'treasure':
    print('You are in the treasure room')
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
