from ledger_entry import LedgerEntry 
from stock_purchase import StockPurchase 

class StockLedger: 
    def __init__(self): 
        self.ledger = {} 
        
    def buy(self, stock_symbol, shares_bought, price_per_share): 
        if stock_symbol not in self.ledger: 
            self.ledger[stock_symbol] = LedgerEntry(stock_symbol) 
        purchase = StockPurchase(stock_symbol, shares_bought, price_per_share) 
        self.ledger[stock_symbol].add_purchase(purchase) 
            
    def sell(self, stock_symbol, shares_sold, sell_price_per_share): 
        if stock_symbol in self.ledger: 
            total_sale_amount = self.ledger[stock_symbol].sell_shares(shares_sold, sell_price_per_share)
            print(f"Sold {shares_sold} shares of {stock_symbol} for a total of ${total_sale_amount:.2f}")
        else:
            print(f"No shares of {stock_symbol} to sell")    
                
    def display_ledger(self): 
        for symbol, entry in self.ledger.items(): 
            print(entry)
