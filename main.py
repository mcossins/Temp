import critter
import goblin
import dragon
import time

name = input("Name) ")
species=0
while int(species) not in range(1,3):
    species = input("Species) 1 for dragon, 2 for goblin ")
if int(species) == 1:
    newCritter = dragon.dragon(name)
else:
    newCritter = goblin.goblin(name)

while not newCritter.endCondition:
    action = input("What would you like " +newCritter.name+" to do?")
    if action == "eat":
        response = 0
        while response not in ["1","2"]:
            response = input("Feed "+newCritter.name+" humans (1) or goats (2)")
            if response == "1":
                food = critter.human()
            elif response == "2":
                food = critter.goat()
            newCritter.eat(food)
    elif action == "sleep":
        newCritter.sleep()
    elif action == "exercise":
        newCritter.exercise()


