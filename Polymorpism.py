class india():
    def capital(self):
        print("New Delhi is the capital of india")
    def language(self):
        print("Hindi is the most widely spoken language of India")
    def type(self):
        print("India is a developing country")

class usa():
    def capital(self):
        print("Washington,D.C is the capital of USA")
    def language(self):
        print("English is the most widely spoken language of USA")
    def type(self):
        print("USA is a developing country")
obj_ind=india()
obj_usa=usa()
for country in (obj_ind,obj_usa):
    country.capital()
    country.language()
    country.type()