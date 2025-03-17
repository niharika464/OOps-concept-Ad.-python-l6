class dog:
    def __init__(self,name, age):
        self.name=name
        self.age=age
    def info(self):
        print("hey! I'm a dog...")
        print(f"My name is {self.name} and my age is {self.age}")
    def quality(self):
        print("I bark....")

class cat:
    def __init__(self,name, age):
        self.name=name
        self.age=age
    def info(self):
        print("hey! I'm a cat...")
        print(f"My name is {self.name} and my age is {self.age}")
    def quality(self):
         print("I meow...")       

dg=dog("puppy",5)
ct=cat("kitty",4)     

for pets in(dg,ct):
     pets.info()
     pets.quality()