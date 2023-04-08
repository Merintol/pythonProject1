class Animal:
    def __init__(self, name, age, color):
        self.name = Lion
        self.age = 10
        self.color = yellow

    def eat(self):
        print(f"{self.name} їсть.")

    def sleep(self):
        print(f"{self.name} спить.")


class Pet(Animal):
    def __init__(self, name, age, color, owner):
        super().__init__(name, age, color)
        self.owner = Alex

    def play(self):
        print(f"{self.name} грається зі своїм власником {self.owner}.")


class Dog(Pet):
    def __init__(self, name, age, color, owner, breed):
        super().__init__(name, age, color, owner)
        self.breed = gordaya

    def bark(self):
        print(f"{self.name} гавкає.")

    def play_fetch(self):
        print(f"{self.name} грається з м'ячиком.")


class Cat(Pet):
    def __init__(self, name, age, color, owner, eye_color):
        super().__init__(name, age, color, owner)
        self.eye_color = blue

    def purr(self):
        print(f"{self.name} муркоче.")

    def play_with_string(self):
        print(f"{self.name} грається зі стрічкою.")


class WildAnimal(Animal):
    def __init__(self, name, age, color, habitat):
        super().__init__(name, age, color)
        self.habitat = forest

    def roam_free(self):
        print(f"{self.name} гуляє в дикій природі у своєму природному середовищі {self.habitat}.")


class Lion(WildAnimal):
    def __init__(self, name, age, color, habitat, mane_color):
        super().__init__(name, age, color, habitat)
        self.mane_color = orange

    def roar(self):
        print(f"{self.name} реве, а його грива {self.mane_color}.")


class Bear(WildAnimal):
    def __init__(self, name, age, color, habitat, weight):
        super().__init__(name, age, color, habitat)
        self.weight = 100

    def hibernate(self):
        print(f"{self.name} зимує і їсть в своїй барлозі, зваживши {self.weight} кілограмів.")