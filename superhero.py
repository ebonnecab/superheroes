class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()

        
    def add_ability(self, ability):
        self.abilities.append(ability)


    def attack(self):
        total = 0
        for ability in self.abilities:
           total += ability.attack()
        return total
            
    
    def take_damage(self, damage):
        self.current_health -= damage

    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False

    def fight(self, opponent):
        while self.is_alive == True:
        
           pass


if __name__ == "__main__":
        hero = Hero("Wonder Woman")
        print(hero.attack())

class Ability:
    def __init__ (self, name, attack_strength):
        '''Initialize starting values'''
        pass
    def attack(self):
        '''Returns attack value between 0 and full attack'''
        pass
