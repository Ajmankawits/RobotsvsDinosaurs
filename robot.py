class Robot:
    def __init__(self, name, Weapon):
        self.name = name
        self.health = 100
        self.weapon = Weapon
    
    def robot_attack(self, dinosaur):
        if self.health > 0:
             dinosaur.health -= self.weapon.attack_power
             print(f'{dinosaur.type} health is now {dinosaur.health}')
             return dinosaur.health 

            
               

                
    
    
