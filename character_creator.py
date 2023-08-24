import dice as d

# temporary character class
# need better code
class character:
    def __init__(self, name, age, strength, agility):
        self.name = name
        self.age = age
        self.strength = strength
        self.agility = agility

    def __str__(self):
        return f"{self.name}"


character_list = list()

# temporary function to test char creation
def create_character(random=False):
    if random:
        name        = "Pedro"
        age         = d.dice_roller(30)+15
        strength    = d.dice_roller(10)
        agility     = d.dice_roller(10)
    else:
        name        = input("Character name: ")
        age         = input("Character age: ")
        strength    = input("Character strength: ")
        agility     = input("Character agility: ")

    char = character(name, age, strength, agility)
    return char

char_choice = input("Create random character? y/n\n")

if char_choice == "y":
    character_list.append(create_character(True))
    

for x in character_list:
    print(x)
    print(f'Age: {x.age}; Strength: {x.strength}; agility: {x.agility}')