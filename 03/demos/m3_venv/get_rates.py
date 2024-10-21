"""
Fetches the latest exchange rate from Euro to USD and prints it.

This script sends a GET request to the Exchange Rates API to retrieve the 
latest exchange rate from Euro to USD. The response is parsed and the 
exchange rate is printed.

Modules:
    requests: To send HTTP requests.
    box: To convert the JSON response to a Python object.

Usage:
    Run the script to fetch and print the latest exchange rate from Euro to USD.

Example:
    $ python get_rates.py
    1 Euro is 1.12 dollars.

Attributes:
    response (requests.Response): The response object from the GET request.
    b (Box): The parsed JSON response as a Box object.
"""

import requests
from box import Box

response = requests.get(
    "https://api.exchangeratesapi.io/latest?symbols=USD")
b=Box(response.json())
#print("1 Euro is ", b.rates.USD, " dollars.")
print(b)
