import requests
from bs4 import BeautifulSoup


class CurrencyConverter:
    def __init__(self):
        url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'html.parser')
        data = soup.prettify()
        self.rates = {}
        for currency in data:
            if currency['cc'] == 'USD':
                self.rates[currency['cc']] = float(currency['rate'])

    def convert(self, amount):
        return amount / self.rates['USD']


if __name__ == '__main__':
    converter = CurrencyConverter()
    amount = float(input('Введіть кількість валюти: '))
    print(f'Кількість доларів США: {converter.convert(amount)}')