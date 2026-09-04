import requests

import config


class RateClient:

    cache = {}

    def __init__(self, base="USD"):
        self.base = base
        self.calls = 0

    def get_rates(self):
        url = config.EXCHANGE_API_BASE + self.base
        r = requests.get(url)
        self.calls = self.calls + 1
        data = r.json()
        return data["rates"]

    def convert_to_usd(self, amount, currency):
        if currency in self.cache.keys():
            rate = self.cache[currency]
        else:
            rates = self.get_rates()
            rate = rates[currency]
            self.cache[currency] = rate
        return amount * rate


def get_country_name(code):
    r = requests.get(config.COUNTRY_API_BASE + code)
    if r.status_code == 200:
        return r.json()[0]["name"]["common"]
    else:
        return "UNKNOWN"


def get_country_names(codes):
    names = []
    for c in codes:
        names.append(get_country_name(c))
    return names
