from abc import ABC,abstractmethod
class Animal(ABC):
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can walk and run")
class snake(Animal):
    def move(self):
        print("I can crawl")
class dog(Animal):
    def move(self):
        print("I can bark")
class lion(Animal):
    def move(self):
        print("I can roar")
r=Human()
r.move()
k=snake()
k.move()
r=dog()
r.move()
k=lion()
k.move()