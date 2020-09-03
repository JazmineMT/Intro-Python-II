# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, description,location):
        self.name = name
        self.description = description
        self.items = []
        self.location = location
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        string = f"You are currently in the: {self.name}\n{self.description}\n Item(s) in room:"
        if len(self.items) < 1:
            string += " None"
        else:    
            for i in self.items:   
                string += f'\n{i}\n'

        return string

    def get_direction(self, direction):
        if direction == 'n':
            return self.n_to
        if direction == 's':
            return self.s_to
        if direction == 'e':
            return self.e_to
        if direction == 'w':
            return self.w_to
        else:
            return None

    def remove_item(self,item):
        self.items.remove(item)
    def add_item(self,item):
        self.items.append(item)
    

   