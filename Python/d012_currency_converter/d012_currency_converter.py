import json
import requests

currency_to = input("Enter the symbol for the currency you'd like to convert money to: ")
amount = input(f"Enter the amount of EUR you'd like to convert to {currency_to}, or leave "
                "blank if you'd just like the conversion factor: ")


api_access_key = "API_KEY"

currency_to = currency_to.strip().upper()
amount = float(amount.strip())

if amount == "":
    amount = 1

url = (f"http://data.fixer.io/api/latest?access_key={api_access_key}&"
        f"symbols={currency_to}&format=1")
print(url)

response = requests.get(url)

value = response.json()["rates"][currency_to]

print(float(value) * amount)


