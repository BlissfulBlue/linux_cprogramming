"""This module defines the Market class.

The Market class holds a list of Coin objects, which each represent a cryptocurrency.
The list is populated with the top 50 currencies/coins from coinranking.com.

Author: Mona Rizvi
Honor Code: My work complies with the JMU Honor Code and instructions for this assignment.
"""
from coin import Coin
import requests
import json
import os
import time

YOUR_API_KEY = "coinranking54edbfad435cfdf381b4784bfd27457f3f225a2af9ea9779"


class Market:
    """The Market class populates and holds a list of cryptocurrencies/coins.

    It can read the data directly from the API or from a saved JSON file.
    It takes the data from the API or file and creates a list of Coin objects.

    Attributes:
        _coins_dict (dict): this dictionary holds the coins after reading from the API or file.
        _coins (list): the list of Coin objects
    """

    def __init__(self):
        if not os.path.exists("savecoins.json"):
            # if no save file exists, call the API
            print("Calling API")
            self.fetch_coins_from_API()
        else:
            # if the file exists, spare a lot of API calls
            # print("Loading data from file")
            fp = open("savecoins.json", "r")
            self._coins_dict = json.load(fp)
            self._load_coin_list()

    def _fetch_coin_description(self, uuid):
        # API endpoint for a single coin
        url = "https://api.coinranking.com/v2/coin/" + uuid
        qparams = {'x-access-token': YOUR_API_KEY}
        result = requests.get(url, params=qparams)
        coin_info = result.json()

        return coin_info['data']['coin']['description']

    def _load_coin_list(self):
        # transform the dictionary into a list of Coin objects
        self._coins = []

        for d in self._coins_dict['coins']:
            c = Coin(d['symbol'], d['name'], float(d['price']))
            c.set_description(d['description'])
            self._coins.append(c)

    def fetch_coins_from_API(self):
        # API endpoint for the top coins list
        # Requesting a 30 day sparkline
        url = "https://api.coinranking.com/v2/coins?timePeriod=30d"

        # coinranking coins API requires only an API key (free on the site)
        parameters = {'x-access-token': YOUR_API_KEY}

        # make the request, passing the parameters, and get the return in JSON from this API
        r = requests.get(url=url, params=parameters)

        # Extract the json data into dictionary
        coinranking = r.json()

        # The coin_list returned is a list of dictionaries
        coin_list = coinranking['data']['coins']

        # load the just-read data into the coin dictionary for saving
        print("Loading coin data .", end="")
        self._coins_dict = {'coins': []}
        for d in coin_list:
            cd = {}
            cd['symbol'] = d['symbol']
            cd['name'] = d['name']
            cd['price'] = d['price']
            #cd['uuid'] = d['uuid']
            #cd['sparkline'] = d['sparkline']
            cd['description'] = self._fetch_coin_description(d['uuid'])
            self._coins_dict['coins'].append(cd)
            time.sleep(0.5)
            print('.', end="")
        print()
        fp = open("savecoins.json", "w")
        json.dump(self._coins_dict, fp)
        fp.close()
        self._load_coin_list()

    def get_coins(self):
        return self._coins
    
    def get_coin(self, symbol):
        for c in self._coins:
            if c.get_symbol() == symbol:
                return c
        return None

    def __str__(self):
        retstr = ""
        for coin in self._coins:
            retstr += str(coin) + '\n'
        return retstr

    def cheap_coin(self):
        cheap = self._coins[0]
        for coin in self._coins:
            if coin.get_price() < cheap.get_price():
                cheap = coin
        return cheap
    
    def expensive_coin(self):
        costly = self._coins[0]
        for coin in self._coins:
            if coin.get_price() > costly.get_price():
                costly = coin
        return costly
    
    def coin_list_to_str(self, cl):
        retstr = ""
        for coin in cl:
            retstr += str(coin) + '\n'
        return retstr
    
    def coins_begin_with(self, letters):
        ret = []
        for coin in self._coins:
            symbol = coin.get_symbol()
            if symbol[0] == letters:
                ret.append(coin)
        return ret
    
    def coins_named_coin(self):
        ret = []
        for coin in self._coins:
            name = coin.get_name()
            if name[1] == identity:
            # if "coin" in name.lower():
                ret.append(coin)
        return ret
    
    def coins_less_than(self, value):
        ret = []
        for coin in self._coins:
            if coin < value:
                ret.append(coin)
        return ret
    
    def average_price(self):
        price_sum = 0
        for coin in self._coins:
            price_sum += coin.get_price
        avg = price_sum / len(self._coins)
        return avg
    
    def max_cheap_coin(self, value):
        cheapCoin = self.coins_less_than(value)
        costly = cheapCoin[0]
        for coin in cheapCoin:
            if coin.get_price() > costly.get_price():
                costly = coin
        return costly
    
    def how_many_for(self, symbol, cash):
        coin = self.get_coin(symbol)
        return cash / coin.get_price()

if __name__ == "__main__":
    market = Market()
    print(market.cheap_coin())
    print(market.expensive_coin())
    print()
    beginning_letter = market.coins_begin_with("D")
    print(market.coin_list_to_str(beginning_letter)) # find a coin symbol that starts with D
    print()
    cl = market.coin_list_named_coin()
    print(market.coin_list_to_str(cl))
    lessl = market.coins_less_than(1.0)
    print(market.coin_list_to_str(lessl))
    print()
    print(market.average_price())
    print()
    print(market.max_cheap_coin(1.0)) # most expensive cheap coin under $1
    print()
    print(market.how_many_for("SAND", 500.0))
