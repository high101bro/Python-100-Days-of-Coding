
class Animal:
    def __init__(self):
        self.number_of_eyes = 2

    def thinking(self):
        print(f"Contemplating life")

    def breath(self):
        print(f"Inhale, exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print("doing this underwater")
    def swim(self):
        print(f"Moving through the water")

fish = Fish()
# Note how the second class inherited to the other attribute and methods from the other class

# Has the Animal attributes for eyes
print(fish.number_of_eyes)

# Has the Animal method for thinking
fish.thinking()

# Note than you can modify a method's behavior
fish.breath()
fish.swim()

