from player import Player
from room import Room
from roomitems import RoomItems

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'finishing': Room('End room', "You are done, great job in finishing!")

}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['finishing']
#
# Main1
#


# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])
directions = ['n', 's', 'e', 'w']
room['outside'].items.append(RoomItems('Knife', 'Shinny and sharp'))
room['treasure'].items.append(RoomItems('Gold', 'Worth a lot of money'))

# Write a loop that:
while True:
    # * Prints the current room name
    current = player.current_room
    print(f'{player.current_room}\n')
    print(f'The room has the following items:\n')
    for item in current.items:
        print(f'{item}\n')

    # * Prints the current description (the textwrap module might be useful here). strip, removes whitespace, lower allows upper and lower,[0] so its not a list
    user_input = input(
        'Please input a direction to go.\n'
        '\nFor north use `n`, For south use `s`, for east `e` and for west use `w` to quit hit `q` '
        'or get or drop an item Hit i for player inventory\n')
    # just using for char
    if user_input == 'q':
        break
    if user_input.lower() == 'i':
        if not player.items:
            print('You have no items\n')
        else:
            for item in player.items:
                print(f'{item}\n')
                #for prints out the item not the whole list


    split_input = user_input.split()

    # for items
    if len(split_input) == 1:
        if user_input in directions:
            # see if we can go that way
            player.move_direction(user_input)

    elif len(split_input) == 2:
        item_names = split_input[1]
        if split_input[0].lower() == 'get':
            item = current.get_item(item_names)
            if item:
                item.on_take()
                current.remove_item(item)
                player.items.append(item)


            else:
                print('No item exists')
        elif split_input[0].lower() == 'drop':
            item = player.get_item(item_names)
            if item:
                item.on_drop()
                player.remove_item(item)
                current.items.append(item)

    else:
        print('bad command')
        continue

# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
