# Write a class to hold player information, e.g. what room they are in
# currently.
# from room import Room
from roomitems import RoomItems
from typing import List
class Player:
    def __init__(self, current_room):
        self.current_room = Room = current_room
        #self.current_item = current_item
        self.items = []
    def move_direction(self, user_input):
        to = user_input + '_to'
        # see if current room has _to

        #hasattr python method
        if hasattr(self.current_room, to):
            #getattr moves to the room
            self.current_room = getattr(self.current_room, to)
        else:
            print('You cant go that way!\n')

    def get_item(self, item_name: str):
        for item in self.items:
            if item.item_name.lower() == item_name.lower():
                return item

        return None

    def remove_item(self, item: RoomItems):
        self.items.remove(item)

    def player_item(self, item_name: str):
        print (f'{item_name}')