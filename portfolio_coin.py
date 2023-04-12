import coin

class PortfolioCoin:
    def __init__(self, price_paid, amount_owned, coin):
        self._price_paid_per_coin = price_paid
        self._amount_owned = amount_owned
        self._coin = coin
    
    def get_coin(self):
        return self._coin
    
    def get_price_paid_per_coin(self):
        return self._price_paid_per_coin
    
    def get_amount_owned(self):
        return self._amount_owned
    
    def set_coin(self, coin): # Coin
        self._coin = coin
    
    def set_price_paid_per_coin(self, price): # float
        self._price_paid_per_coin = price
    
    def get_total_price_paid(self): # float
        return self._price_paid_per_coin * self._amount_owned
    
    def get_current_value(self): # float
        return self._coin.get_price() * self._amount_owned
    
    def get_current_gain_loss(self): # float
        return (self._coin.get_price() * self._amount_owned) - (self._price_paid_per_coin * self._amount_owned)
    
    def __eq__(self, other): # Coin: bool
        if self._coin == other._coin and self._amount_owned == other._amount_owned:
            return True
        
    def __str__(self):
        return f"{self._amount_owned} {self._symbol} coins were purchased at {self._price_paid_per_coin} per coin.\n{self._symbol}: {self._name} is trading at {self._price}\n{self.get_name()} is a {self.description()}."
    
    
if __name__ == "__main__":
    coin1 = PortfolioCoin(5, 10, "BC")
    coin1.set_description("test")

    print(coin1)
