class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()

        
    def add_ability(self, ability):
        self.abilities.append(ability)

        return self.abilities

    def attack(self):
        for ability in self.abilities:
            ability.attack()
    
    def take_damage(self, damage):
        self.current_health.update()

    def is_alive(self):
        if self.current_health > 0:
            self.is_alive == True
