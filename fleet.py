from weapon import Weapon 
from robot import Robot


class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()
  
    
    def create_fleet(self):
        weapon1 = Weapon("Railgun", 8)
        weapon2 = Weapon("Plasma Rifle", 16)
        weapon3 = Weapon("Hellbore", 50)
        
        robot1 = Robot("Hunter-Killer", weapon1)
        robot2 = Robot("Mega-Warform", weapon2)
        robot3 = Robot("Bolo", weapon3)

        self.robots.append(robot1)
        self.robots.append(robot2)
        self.robots.append(robot3)
