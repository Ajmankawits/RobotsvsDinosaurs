from weapon import Weapon 
from dinosaur import Dinosaur
class Robot:
    def __init__(self, name):
        self.robot_name = name
        self.robot_health = 1000
        self.robot_weapon = Weapon("Railgun", 50)
    
    def robot_attack(self,dinosaur):
       pass