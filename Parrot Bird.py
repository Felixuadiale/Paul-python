class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age

blue=parrot('Blue',10)
wool=parrot('Wool',15)
print('Blue is a',blue.species)
print(blue.name,' is',blue.age,'years old')