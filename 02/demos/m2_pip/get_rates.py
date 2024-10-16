"""
This script fetches the latest exchange rates for USD from the ExchangeRate-API.

Modules:
    requests: To make HTTP requests.

Usage:
    Run the script to print the latest exchange rates for USD in JSON format.

Example:
    $ python get_rates.py

Functions:
    None

Attributes:
    response (requests.Response): The response object containing the exchange rates data.
"""

import requests

response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
print(response.text)
