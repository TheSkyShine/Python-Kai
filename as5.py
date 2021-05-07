import random
import math

from gamelib import *

class ZombieCharacter(ICharacter):
    def __init__(self, obj_id, health, x, y, map_view):
        ICharacter.__init__(self, obj_id, health, x, y, map_view)

    def selectBehavior(self):
        prob = random.random()

        # If health is less than 50%, then heal with a 10% probability
        if prob < 0.1 and self.getHealth() < self.getInitHealth() * 0.5:
            return HealEvent(self)

        # Pick a random direction to walk 1 unit (Manhattan distance)
        x_off = random.randint(-1, 1)
        y_off = random.randint(-1, 1)

        # Check the bounds
        map_view = self.getMapView()
        size_x, size_y = map_view.getMapSize()
        x, y = self.getPos()
        if x + x_off < 0 or x + x_off >= size_x:
            x_off = 0
        if y + y_off < 0 or y + y_off >= size_y:
            y_off = 0

        return MoveEvent(self, x + x_off, y + y_off)

class PlayerCharacter(ICharacter):
    def __init__(self, obj_id, health, x, y, map_view):
        ICharacter.__init__(self, obj_id, health, x, y, map_view)
        
        self.obj_id = obj_id
        self.health = health
        self.x = x
        self.y =  y
        self.map_view = map_view
        
        self.zombie_near = False
        self.in_corner = False
        
        # Inital moving parameters
        self.x_off = 1
        self.y_off = 1
        
        
    def selectBehavior(self):
        


        
        # gets map size, current coordinates, and corner coordinates
        map_view = self.getMapView()
        size_x, size_y = map_view.getMapSize()
        x, y = self.getPos()
        corner_coord_x = [0,size_x-1]
        corner_coord_y = [0,size_y-1]
        
        
        if len(self.getScanResults()) > 0:
            self.zombie_near = True

        print('ZOMBIE NEARRR??')
        print(self.zombie_near)
        
        # determines if player is in a corner yet
        if x in corner_coord_x and y in corner_coord_y:
            self.in_corner = True
        
        
        # First action, heal if less than 50% init health
        if self.getHealth() < self.getInitHealth()*0.5:
            self.check = 10
            return HealEvent(self)
        
        
        # if not in a corner immediatly runs towards a corner
        elif self.in_corner == False:

        # Checks to make sure the player doesnt move out of bounds
            if x + self.x_off < 0 or x + self.x_off >= size_x:
                 self.x_off = 0
            if y + self.y_off < 0 or y + self.y_off >= size_y:
                 self.y_off = 0  
                 
            return MoveEvent(self, x + self.x_off, y + self.y_off)
    
        # if the player is in the corner and no zombies are nearby, they start scanning for zombies
        elif self.in_corner == True and self.zombie_near == False:
            return ScanEvent(self)
        
        # if there is a zombie nearby, player moves to a different corner depneding on their position.
        # move event is returned to make self.incorner condition false
        elif self.zombie_near == True:
            if x == size_x-1 and y == size_y-1:
                self.x_off = -1
                self.y_off = 0
            elif x == 0 and y == size_y-1:
                self.x_off = 0
                self.y_off = -1
            elif x == 0 and y == 0:
                self.x_off = 1
                self.y_off = 0
            elif x == size_x-1 and y == 0:
                self.x_off = 0
                self.y_off = 1
                
            # Checks to make sure the player doesnt move out of bounds
            elif x + self.x_off < 0 or x + self.x_off >= size_x:
                 self.x_off = 0
            elif y + self.y_off < 0 or y + self.y_off >= size_y:
                self.y_off = 0  
        
                 
            return MoveEvent(self, x + self.x_off, y + self.y_off)
            
                
        else:
            pass

            
        
            
            
        
        

        
            
            
