
#Simple class
class Armor():

    def __init__(self, type, weight):
        self.type = type
        self.weight = weight
    def protect(self):
        print(f"{self.type.title()} weighs {self.weight} kg")

if __name__ == "__main__":
    armor = Armor("cuirass", 30)
    armor.protect()