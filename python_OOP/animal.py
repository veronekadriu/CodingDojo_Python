# This class creates an Animal class and give it the below attributes and methods. It extends the Animal class to two child classes, Dog and Dragon
class Animal:
    def __init__(self,name,health):
        self.name= name
        self.health = health
    
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print(self.name, "'s health is: ", self.health  )
        return self

class Dog(Animal):
    def __init__(self, name, health):
        health = 150
        super(Dog, self).__init__(name,health)

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name, health):
        health = 170
        super(Dragon, self).__init__(name,health)

    def fly(self):
        self.health -= 10
        return self
    
    def display_health(self):
        super(Dragon, self).display_health()
        print("Iam a Dragonnnnn....")
        return self

cat = Animal("Kitty", 100).walk().walk().walk().run().run().display_health()

dog = Dog("Rexy", 150).walk().walk().walk().run().run().pet().display_health()

dragon = Dragon("TRex", 170).fly().display_health()

# cat.fly().pet().display_health() it does not work

# dog.fly() it does not work either





    
