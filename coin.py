class Coin:
    def __init__(self, symbol, name, price):
            self._symbol = symbol
            self._name = name
            self._price = price
            self._description = ""

    def get_symbol(self):
            return self._symbol

    def get_name(self):
            return self._name

    def get_price(self):
            return self._price

    def set_description(self, desc):
            self._description = desc

    def get_description(self):
            return self._description

    def __str__(self):
        return (f"{self._symbol}: {self._name} is trading at {self._price:.10f}\n{self._description}")

    def __eq__(self, other):
        if self._symbol == other._symbol and self._name == other._name:
            return True
    
if __name__ == "__main__":
    coin1 = Coin("SHIB", "Shiba Inu", 100)
    coin1.set_description("Shiba Inu is a decentralized dog-themed cryptocurrency, with a loyal following from the ShibArmy, that aims to revolutionize against centralization.")
    print(coin1)
    coin2 = Coin("BC", "Bruh Coin", 200)
    coin2.set_description("Bruh Coin got Bruh in it")
    print(coin2)
