class Animal:
	def speak(self):
		print("Animals Sounds")

class Dog(Animal):
	def speak(self):
		print("Bark")

class Cat(Dog):
	def speak(self):
		print("Meow")
	
obj = Cat()
# obj.speak()

objects = [Cat(),Dog(),Animal()]

for i in objects:
	i.speak()