class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hi, I am {self.name}")

p1 = Person("Ali", 20)
p1.greet()
