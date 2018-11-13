class Tiger ():
    '''A tiger has a name and age and favorite food'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.favorite_food = "catnip"
    def __str__(self):
        return "{} is {} years old.".format(self.name, self.age)
    def eat(self, food):
        print("{} eats {}.".format(self.name, food))
        if food == self.favorite_food:
            print("Yum! Give me more " + food)


tony = Tiger("Tony", 66)
print(tony)
hobbes = Tiger("Hobbes", 55)
print(hobbes)
hobbes.eat("fish")
tony.favorite_food = "Frosted Flakes"
print("{}'s favorite food is {}.".format(tony.name, tony.favorite_food))
tony.eat(tony.favorite_food)

