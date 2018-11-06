class Dog:
    greeting = "Woof!"

    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.greeting)

if __name__ == "__main__":
    my_dog = Dog("Spot")
    print(my_dog.name)

    my_other_dog = Dog("Annie")
    print(my_other_dog.name)

my_first_dog = Dog("Lucky")
my_second_dog = Dog("Wyatt")

print(my_first_dog.name)
print(my_second_dog.name)

my_first_dog.bark()
my_second_dog.bark()