class StockPurchase: 
    def __init__(self, stock_symbol, shares, cost_per_share): 
        # Initialize a stock purchase with the given stock symbol, number of shares, and cost per share
        self.stock_symbol = stock_symbol  
        self.shares = shares              
        self.cost_per_share = cost_per_share 

    def __str__(self): 
        # Return a string representation of the stock purchase for easy reading
        return f"{self.stock_symbol} @ ${self.cost_per_share} for {self.shares} shares"
