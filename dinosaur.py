class Dinosaur:
    def __init__(self, type, attack_power):
        self.type = type
        self.attack = attack_power
        self.health = 100
       
    
    def dinosaur_attack(self, robot):
        if self.health > 0:
            robot.health = robot.health - self.attack
            print(f'{robot.name} health is now {robot.health}')
            return robot.health
        
        
          