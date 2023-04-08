class Engine:
    def __init__(self, horsepower, cylinders):
        self.horsepower = horsepower
        self.cylinders = cylinders

    def start(self):
        print("Двигун запущено")

    def stop(self):
        print("Двигун зупинено")


class Body:
    def __init__(self, color, style):
        self.color = color
        self.style = style

    def open_door(self):
        print("Двері відкриті")

    def close_door(self):
        print("Двері закриті")


class Car(Engine, Body):
    def __init__(self, horsepower, cylinders, color, style):
        Engine.__init__(self, horsepower, cylinders)
        Body.__init__(self, color, style)
        self.current_speed = 0

    def accelerate(self, speed):
        self.current_speed += speed
        print(f"Автомобіль рухається зі швидкістю {self.current_speed} км/год")

    def brake(self):
        self.current_speed = 0
        print("Автомобіль зупинився")