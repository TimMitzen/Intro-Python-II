# Implement a class to hold room information. This should have name and
# description attributes.
from typing import List
from roomitems import RoomItems
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items: List[RoomItems] = []


    def __str__(self):
        return  f'{self.name}: {self.description}'

    def get_item(self, item_name: str):
        for item in self.items:
            if item.item_name.lower() == item_name.lower():
                return item

        return None

    def remove_item(self, item: RoomItems):
        self.items.remove(item)