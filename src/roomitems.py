from typing import List

class RoomItems:
    def __init__(self, item_name, item_description):
        self.item_name = item_name
        self.item_description = item_description
        self.items = []

    def __str__(self):
        return f'{self.item_name}: {self.item_description}'




    def on_take(self):
       print(f'you picked up a {self.item_name}')

    def on_drop(self):
        print(f'You dropped a {self.item_name}')

    def player_item(self):
        print(f'{self.items}')





