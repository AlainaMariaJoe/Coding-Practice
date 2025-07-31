class Dog:    
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed 
    def bark(self):
        print(f"Woof! I'm {self.name} and I run at {self.speed} km/h")

def fastest_dog(*dogs):
    fastest = dogs[0]
    for i in range(1, len(dogs)):
        if dogs[i].speed > fastest.speed:
            fastest = dogs[i]
    return f"{fastest.name} is the Fastest Dog running at {fastest.speed} km/h"

dog1 = Dog("Rio", 30)
dog2 = Dog("Killer", 40)
dog3 = Dog("Jango", 35)

dog1.bark()
dog2.bark()
dog3.bark()

print(fastest_dog(dog1, dog2, dog3))
