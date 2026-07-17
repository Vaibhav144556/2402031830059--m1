# Multilevel Inheritance

class A:
    def hello(self):
        print("Hello this is class A")

class B(A):
    def hi(self):
        print("Hi this is class B")

class C(B):
    def bye(self):
        print("Bye this is class C")

obj = C()

obj.hello()  
obj.hi()
obj.bye()       
