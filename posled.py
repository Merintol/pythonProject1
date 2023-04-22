import random


class Encoder:
    def __init__(self, num):
        self.__num = num

    def __str__(self):
        return str(self.__num)

    def __encrypt(self):
        # інкапсульований метод для шифрування числа
        self.__num = (self.__num * random.randint(1, 10)) % 100

    def get_result(self):
        # метод, який виконує шифрування та випадкову математичну операцію
        self.__encrypt()
        return self.__num + random.randint(1, 10)