import time

class Food:
    def applyFood(self, critter):
        critter.foodQuantity += self.foodQuantity
class human(Food):
    def __init__(self):
        self.foodQuantity = 5
class goat(Food):
    def __init__(self):
        self.foodQuantity = 3



class Critter:
    EXERCISENOISE = 1
    EATNOISE = 2
    SLEEPNOISE = 3
    DEADNOISE = 4
    WINNOISE = 5

    def __init__(self, name):
        self.foodQuantity = 5
        self.name = name
        self.exerciseLevel = 0
        self.energy = 3
        self.endCondition = False

    def sleep(self):
        print(self.name + " is sleeping")
        for i in range(0,5):
            self.noise(self.SLEEPNOISE)
            time.sleep(1)
        self.foodQuantity -= 1
        self.energy +=3
        if self.foodQuantity == 0:
            self.die()

    def eat(self, food):
        print(self.name + " is eating")
        self.noise(self.EATNOISE)
        food.applyFood(self)
        if self.foodQuantity > 10:
            self.die()

    def exercise(self):
        print(self.name + " is exercising")
        self.noise(self.EXERCISENOISE)
        self.foodQuantity-=2
        self.energy -=1
        self.exerciseLevel +=1
        if self.foodQuantity <= 0 or self.energy == 0:
            self.die()
        elif self.exerciseLevel == 5:
            self.win()

    def die(self):
        print(self.name+" died")
        self.noise(self.DEADNOISE)
        self.endCondition = True

    def win(self):
        print(self.name + " won!")
        self.noise(self.WINNOISE)
        self.endCondition = True

    def noise(self, action):
        pass
