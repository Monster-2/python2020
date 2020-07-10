#Program for an elevator. Just made for fun.

class Elevator():
    def __init__(self, floors):
        self.floors = floors
        self.position = 0
        self.door = 'closed'
        
    def status(self):
        print('Floor: ' + str(self.position))
        print('Door: ' + self.door)
        
    def move_to(self, floor_nr):
        if floor_nr > self.floors:
            print('This elevator cannot reach this floor')
        elif self.door != 'closed':
            print('Close the door please')
        else:
            self.position = floor_nr
            print('Floor: ' + str(self.position))
            print('Door: ' + self.door)
        
    def open_door(self):
        self.door = 'open'
        print('Floor: ' + str(self.position))
        print('Door: ' + self.door)
    
    def close_door(self):
        self.door = 'closed'
        print('Floor: ' + str(self.position))
        print('Door: ' + self.door)
