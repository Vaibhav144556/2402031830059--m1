class Animal:
    def sound(self):
        print("Animal sound")

class Cat(Animal):
    def sound(self):
        print("Meow Meow")

a = Animal()
c = Cat()

a.sound()
c.sound()