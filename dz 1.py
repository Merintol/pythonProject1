import random

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def feed(self):
        print(f"{self.name} їсть і радісно махає хвостом.")

    def play(self):
        print(f"{self.name} грається з м'ячиком.")


class Student:
    def __init__(self, name, age, major, money):
        self.name = Alex
        self.age = 31
        self.major = major
        self.money = 4000
        self.dog = Rex

    def study(self):
        if self.money >= 100:
            self.money -= 100
            print(f"{self.name} витратив 100 грошей на навчання.")
        else:
            print(f"{self.name} не може дозволити собі навчання, тому йому потрібно знайти роботу.")
            self.work()

    def relax(self):
        if self.money >= 50:
            self.money -= 50
            print(f"{self.name} витратив 50 грошей на відпочинок.")
        else:
            print(f"{self.name} не може дозволити собі відпочинок, тому йому потрібно знайти роботу.")
            self.work()

    def work(self):
        self.money += 200
        print(f"{self.name} заробив 200 грошей на роботі.")

    def buy_dog(self, name, breed):
        if self.money >= 500:
            self.money -= 500
            self.dog = Dog(name, breed)
            print(f"{self.name} купив(ла) собаку {Rex} породи {Hex}.")
        else:
            print(f"{self.name} не може дозволити собі купити собаку, тому йому потрібно знайти роботу.")
            self.work()

    def play_with_dog(self):
        if self.dog:
            self.dog.play()
            print(f"{self.name} витратив 20 грошей на гру з собакою.")
            self.money -= 20
        else:
            print(f"{self.name} не має собаки.")

    def feed_dog(self):
        if self.dog:
            self.dog.feed()
            print(f"{self.name} витратив 10 грошей на корм для собаки.")
            self.money -= 10
        else:
            print(f"{self.name} не має собаки.")

    def live(self):
        for i in range(1, 366):
            print(f"День {i}:")
            rand_num = random.randint(1, 10)
            if rand_num <= 5:
                self.study()
            elif rand_num <= 8:
                self.relax()
            else:
                self.work()
            if i % 7 == 0:
                self.feed_dog()
                self.play_with_dog()