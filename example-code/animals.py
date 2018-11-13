class Tiger ():
    '''A tiger has a name and age and favorite food'''
    def __init__(self, name, age):
        self.name = name
        self.age = age

tony = Tiger("Tony", 66)
print("{} is {} years old.".format(tony.name, tony.age)) 
