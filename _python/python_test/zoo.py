class Zoo:
    def __init__(self, zname):
        # self.animalist = []
        self.zname = zname
    # def add_tiger(self, name):
    #     self.animalist.append( Tiger(name) )
    # def add_lion(self, name):
    #     self.animalist.append( Lion(name) )
    # def add_rabbit(self, name):
    #     self.animalist.append( Rabbit(name) )
    # def print_all_info(self):
    #     print("-"*30, self.zname, "-"*30)
    #     for animal in self.animalist:
    #         animal.display_info()

class Animal:
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness
    def feed(self):
        self.health+=10
        self.happiness+=10
        return self
    def display_info(self):
        print(f"Name: {self.name} | Age: {self.age} | Health: {self.health} | Happiness: {self.happiness}")

class Lion(Animal):
    def __init__(self, name, age=10, health=100, happiness=80):
        super().__init__(name, age, health, happiness)

class Tiger(Animal):
    def __init__(self, name, age=8, health=120, happiness=100):
        super().__init__(name, age, health, happiness)

class Rabbit(Animal):
    def __init__(self, name, age=1, health=20, happiness=120):
        super().__init__(name, age, health, happiness)



Simba = Lion("Simba")
ShereKhan = Tiger("Shere Khan")
Arnab = Rabbit("Arnab")

zoo1 = Zoo("Yazeed's Zoo")
# zoo1.add_lion("Simba")
# zoo1.add_tiger("Shere Khan")
# zoo1.add_rabbit("Arnab")

print("-"*30, zoo1.zname, "-"*30)
Simba.feed().feed().display_info()
ShereKhan.feed().feed().display_info()
Arnab.feed().feed().display_info()

# zoo1.print_all_info()
