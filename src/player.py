# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, current_room):
       self.current_room = current_room

    def move_direction(self, user_input):
        to = user_input + '_to'
        # see if current room has _to
        #hasattr python method
        if hasattr(self.current_room, to):
            #getattr moves to the room
            self.current_room = getattr(self.current_room, to)
        else:
            print('You cant go that way!\n')