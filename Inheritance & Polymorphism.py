'''
Use the 'pass' keyword for subclass if no additional changes are needed

By adding __init__() to the subclass, the subclass NO LONGER INHERITS/OVERRIDES superclass's constructor
To access superclass's method and constructor, use super().__init__(parameters) for constructor and super.method() for method
'''

class Mammal:
    def __init__(self, species, sex, size, locomotion):
        self.species = species
        self.sex = sex
        self.size = size
        self.locomotion = locomotion

    def give_birth(self):
        print(f"A {self.sex} {self.species} is giving birth! Holy shit!")


class Human(Mammal):
    def __init__(self, species, sex, size, locomotion, name, status):
        super().__init__(species, sex, size, locomotion)
        self.name = name
        self.status = status

    def talk(self, message):
        print(f"A {self.sex} {self.species} named {self.name} says {message}")\


borger = Mammal("borger", "male", "small", "None")
borger.give_birth()

Karen = Human("human", "female", "Medium", "Bipedal", "Karen", "Low-life")
Karen.talk("where is your manager?")