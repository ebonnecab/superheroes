import random
class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []

        
    def add_ability(self, ability):
        new_ability = self.abilities.append(ability)
        return new_ability


    def attack(self):
        total = 0
        for ability in self.abilities:
           total += ability.attack()
        return total
            
    
    def take_damage(self, damage):
        remaining_health = self.current_health - damage
        self.current_health = remaining_health
        print(remaining_health)


    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False

    def fight(self, opponent):
     '''Runs a loop to attack opponent until someoe dies'''
     while self.is_alive() and opponent.is_alive():
        damage = self.attack() 
        opponent.take_damage(damage)
        self.take_damage(damage)

    def add_weapon(self, weapon):
        '''
        This method will append the weapon object passed in as an argument to the list of abilities that already exists -- self.abilities.
        This means that self.abilities will be a list of abilities and weapons.
        '''
        weaponry = self.abilities.append(weapon)
        return weaponry
  

    
    def add_armor(self, armor):
        '''
        This method will add the armor object that is passed in to the list of armor objects definied in the initializer as self.armors.
        '''
        armory = self.armors.append(armor)
        return armory

class Ability:
    def __init__ (self, name, max_attack):
        '''Initialize starting values'''
        self.name = name
        self.max_attack = max_attack
        
    def attack(self):
        '''Returns attack value between 0 and full attack'''
        return random.randint(0, self.max_attack)

class Weapon(Ability):
    def attack(self):
        '''returns a random value between one half to full attack power'''
        return random.randint(self.max_attack//2, self.max_attack)

class Team:
    def init(self, team_name):
        '''Instantiate resources.'''
        self.name = team_name
        self.heroes = []

    def add_hero(self, Hero):
        '''Add hero object to heroes list.'''
        new_hero = self.heroes.append(Hero)
        return new_hero

    def remove_hero(self, name):
        '''Removes hero from hero list.'''
        delete_hero = self.heroes.remove(name)
        return delete_hero

    def view_heroes(self):
        '''Prints out all heroes to console.'''
        hero_index = print(self.heroes.index())
        return hero_index
        
class Arena:
    def __init__(self):
      self.team_one = None
      self.team_two = None

    def create_ability(self):
        '''
        This method will let user create an ability,
        prompt them for necessary info,
        return the new ability object.
        '''
        print("Time to give your hero some abilities!")
        ability_input= input("Name your special ability: ")
        max_input = input("What is the max damage of your ability: ")
        ability = Ability(ability_input, max_input)
        return ability
        
    def create_weapon(self):
        '''
        This method will let user create a weapon.
        prompt them for necessary info,
        return new weapon
        '''
        pass
    def create_armor(self):
        '''
        This method lets user create armor,
        prompt them for necessary info,
        return new armor object
        '''
        pass
    def create_hero(self):
        '''
        This method lets user create a hero,
        user should specify if they want armor, weapons, and abilities,
        return new hero object
        '''
        hero_input = input("Name your Hero!: ")
        user_hero = Hero(hero_input)
        hero.add_ability(self.create_ability())
        hero.add_armor(self.create_armor())
        hero.add_weapon(self.create_weapon())
        return user_hero
    def build_team_one(self):
        '''
        This method will let user create team one,
        prompt them for number of heroes,
        call self.hero() for every hero the user wants to add,
        add created hero to team one
        '''
        pass
    def build_team_two(self):
        '''
        This method will let user create team two,
        prompt them for number of heroes,
        call self.hero() for every hero the user wants to add,
        add created hero to team two
        '''
        pass
    def team_battle(self):
        '''
        This method battes with both teams,
        call the attack method in team objects for functionality
        '''
        pass
    def show_stats(self):
        '''
        This method prints out battle stats, kill/death ratio,
        winning team, surviving heros
        '''
        pass

if __name__ == "__main__":
        hero = Hero("Wonder Woman")
        print(hero.attack())
        ability = Ability("Divine speed", 300)
        hero.add_ability(ability)
        print(hero.attack())
        new_ability = Ability("Super Human Strength", 800)
        hero.add_ability(new_ability)
        print(hero.attack())
        hero2 = Hero("Jodie Foster")
        ability2 = Ability("Science", 800)
        hero2.add_ability(ability2)
        hero.fight(hero2)
        

        
