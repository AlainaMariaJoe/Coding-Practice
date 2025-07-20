'''Class Cat'''
class Cat:
    species = "mammal"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f"Meow, my name is {self.name} and I am {self.age}")

# Function to find the oldest cat
def oldest_cat(*cats):
    oldest = cats[0]
    for i in range(1, len(cats)):
        if cats[i].age > oldest.age:
            oldest = cats[i]
    return f"{oldest.name} is the oldest cat having age {oldest.age}"

cat1 = Cat("Ruby", 6)
cat2 = Cat("Puss", 4)
cat3 = Cat("Sussy", 2)

cat1.talk()
cat2.talk()
cat3.talk()

print(oldest_cat(cat1, cat2, cat3))