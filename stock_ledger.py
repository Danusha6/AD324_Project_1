from ledger_entry import LedgerEntry 
from stock_purchase import StockPurchase 

class StockLedger: 
    def __init__(self): 
        self.ledger = {}  # Initializes an empty dictionary to store stocks by their symbol as keys and LedgerEntry objects as values.
        
    def buy(self, stock_symbol, shares_bought, price_per_share): 
        # Checks if the stock symbol is already in the ledger; if not, creates a new LedgerEntry.
        if stock_symbol not in self.ledger: 
            self.ledger[stock_symbol] = LedgerEntry(stock_symbol) 
        # Creates a StockPurchase instance and adds it to the relevant LedgerEntry.
        purchase = StockPurchase(stock_symbol, shares_bought, price_per_share) 
        self.ledger[stock_symbol].add_purchase(purchase) 
        
    def sell(self, stock_symbol, shares_sold, sell_price_per_share): 
        # Checks if the stock symbol exists in the ledger.
        if stock_symbol in self.ledger: 
            # Calls sell_shares on the LedgerEntry, calculating the total sale amount and printing it.
            total_sale_amount = self.ledger[stock_symbol].sell_shares(shares_sold, sell_price_per_share)
        else:
            # Prints a message if there are no shares of the given symbol to sell.
            print(f"No shares of {stock_symbol} to sell")
            
    def sell_optimal(self, stock_symbol, shares_sold, sell_price_per_share): 
        # Checks if the stock symbol exists in the ledger.
        if stock_symbol in self.ledger: 
            # Calls sell_optimal on the LedgerEntry to sell shares in a way that optimizes profit.
            total_sale_amount = self.ledger[stock_symbol].sell_optimal(shares_sold, sell_price_per_share)
            print(f"Optimally sold {shares_sold} shares of {stock_symbol} for a total of ${total_sale_amount:.2f}")
        else:
            # Prints a message if there are no shares of the given symbol to sell.
            print(f"No shares of {stock_symbol} to sell")    
                
    def display_ledger(self): 
        # Iterates over all LedgerEntry objects in the ledger and prints each one.
        for symbol, entry in self.ledger.items(): 
            print(entry)
