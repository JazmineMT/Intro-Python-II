# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.bag = []
    
    def __str__(self):
        string = f"Item(s) in your bag:"
        if len(self.bag) < 1:
            string += " None"
        else:    
            for i in self.bag:   
                string += f'\n{i}\n'

        return string
    def move(self, direction):
        if direction in ['n', 's', 'e', 'w']:
            next_room = self.room.get_direction(direction)
            if next_room is not None:
                self.room = next_room
                print(self.room)
            else:
                print("There is nothing to behold that way!")


    def on_take(self, item):
        item.on_take()
        self.bag.append(item)
    def on_drop(self, item):
        item.on_drop()
        self.bag.remove(item)

    