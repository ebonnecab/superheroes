class Tiger ():
    '''A tiger has a name and age and favorite food'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return "{} is {} years old.".format(self.name, self.age)


tony = Tiger("Tony", 66)
print(tony)
hobbes = Tiger("Hobbes", 55)
print(hobbes)
