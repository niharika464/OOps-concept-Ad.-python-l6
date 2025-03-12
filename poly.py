class rabbit:
    def __init__(self,name, age):
        self.name=name
        self.age=age
    def info(self):
        print("hey! I'm a rabbit...")
        print(f"My name is {self.name} and my age is {self.age}")
    def quality(self):
        print("I run fast....")

class turtle:
    def __init__(self,name, age):
        self.name=name
        self.age=age
    def info(self):
        print("hey! I'm a turtle...")
        print(f"My name is {self.name} and my age is {self.age}")
    def quality(self):
         print("I run slow....")       

rt=rabbit("bunny",5)
tl=turtle("pikachu",4)     

for pets in(rt,tl):
     pets.info()
     pets.quality()