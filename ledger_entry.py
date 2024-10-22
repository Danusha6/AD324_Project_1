from linked_deque import LinkedDeque 
from stock_purchase import StockPurchase 

class LedgerEntry: 
    def __init__(self, stock_symbol): 
        self.stock_symbol = stock_symbol 
        self.purchases = LinkedDeque() 
        
    def add_purchase(self, new_purchase): 
        self.purchases.add_to_back(new_purchase) 
        
    def remove_purchase(self): 
        if not self.purchases.is_empty(): 
            return self.purchases.remove_front() 
        return None 
    
    def get_total_shares(self): 
        total_shares = 0 
        current = self.purchases.front 
        while current: 
            total_shares += 1 # Assuming 1 share per entry, adjust if needed 
            current = current.next_node 
        return total_shares 
    
    def get_average_cost(self): 
        total_cost = 0 
        total_shares = 0 
        current = self.purchases.front 
        while current: 
            total_cost += current.data.cost_per_share * current.data.shares
            total_shares += current.data.shares
            current = current.next_node 

        return total_cost / total_shares if total_shares > 0 else 0 
    
    def sell_shares(self, shares_sold, sell_price_per_share):
        total_sale_amount = 0
        shares_to_sell = shares_sold

        while shares_to_sell > 0 and not self.purchases.is_empty():
            purchase = self.purchases.get_front()

            if purchase.shares <= shares_to_sell:
                total_sale_amount += purchase.shares * sell_price_per_share
                shares_to_sell -= purchase.shares
                self.purchases.remove_front()
            else:
                total_sale_amount += shares_to_sell * sell_price_per_share  
                purchase.shares -= shares_to_sell
                shares_to_sell = 0  
        
        if shares_to_sell > 0:
                print(f"Warning: Not enough shares to sell for {self.stock_symbol}. {shares_to_sell} unsold.")
        
        return total_sale_amount        
    
    def __str__(self): 
        purchase_details = []
        current = self.purchases.front
        while current:
            purchase_details.append(f"{current.data.shares} shares @ {current.data.cost_per_share:.2f}")
            current = current.next_node
        return f"{self.stock_symbol}: " + ", ".join(purchase_details)

