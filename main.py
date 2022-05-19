from webbrowser import get
import requests
import json

url = 'https://limitless-harbor-83714.herokuapp.com/api/GetPizza'
data = requests.get(url)
#print(data.text)

pizzas = json.loads(data.text)

for pizzamodel in pizzas:
    pizza = pizzamodel['fields']
    print(pizza['nom'])
