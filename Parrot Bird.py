class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sing(self,song):
        return f'{self.name} sings {song}'
    def dance(self):
        return f'{self.name} is now dancing'

blue=parrot('Blue',10)
wool=parrot('Wool',15)
print('Blue is a',blue.species)
print(blue.name,' is',blue.age,'years old')
print(blue.sing('hAPPY'))
print(blue.dance)