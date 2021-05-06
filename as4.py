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
        self.everyother = False
        

    def selectBehavior(self):
        
        x_off = 1
        y_off = 1
        
        # if self.scan_results == True:
        #     self.zombie_near = True
        
        if self.getHealth() < self.getInitHealth()*0.5:
            return HealEvent(self)
        elif self.everyother == False:
            map_view = self.getMapView()
            size_x, size_y = map_view.getMapSize()
            x, y = self.getPos()
            if x + x_off < 0 or x + x_off >= size_x:
                x_off = 0
            if y + y_off < 0 or y + y_off >= size_y:
                y_off = 0
            self.everyother = True
            return MoveEvent(self, x + x_off, y + y_off)
        #elif 
        else:
            self.everyother = False
            return ScanEvent(self)
                
            
                
            
        
 
        
    
        # determining if we got attacked or not
        # elif self.decrementHealth() > self.getHealth()*0.1:
        #     return ScanEvent(self)
        
        
            
            
