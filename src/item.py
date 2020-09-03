# items to be placed in each room 
from room import Room 
class Item:
    def __init__(self, item_name , item_description):
        self.item_name = item_name
        self.item_description = item_description


    def __str__(self):
        string = ""
        string += f'{self.item_name} : {self.item_description}'
        return string

    def on_take(self):
        print(f"You have picked up a {self.item_name}")
        

    def on_drop(self):
        print(f"You have dropped a {self.item_name}")