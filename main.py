import random

starting_food = 100
starting_money = 1000

starting_customers = 50

food_prices = {
    'apple': 2,
    'banana': 1,
    'orange': 3,
    'bread': 4,
    'milk': 2,
    'eggs': 3,
    'cheese': 5
}

class Store:
    def __init__(self):
        self.food = starting_food
        self.money = starting_money
        self.customers = starting_customers

    def buy(self, item, quantity):
        if item in food_prices:
            cost = food_prices[item] * quantity
            if cost > self.money:
                print('Недостаточно денег!')
            elif quantity > self.food:
                print('Недостаточно еды!')
            else:
                self.money -= cost
                self.food -= quantity
                self.customers += random.randint(1, 10)
                print('Успешно куплено!')

store = Store()

for i in range(365):
    item = random.choice(list(food_prices.keys()))

    quantity = random.randint(1, 10)

    store.buy(item, quantity)

    print('День', i+1)
    print('Еда:', store.food)
    print('Деньги:', store.money)
    print('Клиенты:', store.customers)