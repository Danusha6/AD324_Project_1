from linked_deque import LinkedDeque 
from stock_purchase import StockPurchase 

class LedgerEntry: 
    def __init__(self, stock_symbol): 
        # Initialize with a stock symbol and a deque to store purchases
        self.stock_symbol = stock_symbol 
        self.purchases = LinkedDeque() 
        
    def add_purchase(self, new_purchase): 
        # Adds a new purchase to the back of the deque
        self.purchases.add_to_back(new_purchase) 
        
    def remove_purchase(self): 
        # Removes the oldest purchase from the front of the deque if it's not empty
        if not self.purchases.is_empty(): 
            return self.purchases.remove_front() 
        return None 
    
    def get_total_shares(self): 
        # Calculates the total number of shares for this stock symbol
        total_shares = 0 
        current = self.purchases.front 
        while current: 
            total_shares += 1
            current = current.next_node 
        return total_shares 
    
    def get_average_cost(self): 
        # Calculates the average cost per share across all purchases
        total_cost = 0 
        total_shares = 0 
        current = self.purchases.front 
        while current: 
            # Accumulate total cost and number of shares
            total_cost += current.data.cost_per_share * current.data.shares
            total_shares += current.data.shares
            current = current.next_node 

        # Return average cost if there are shares, otherwise return 0
        return total_cost / total_shares if total_shares > 0 else 0 
    
    def sell_shares(self, shares_sold, sell_price_per_share):
        # Sell a specified number of shares at a given sell price per share
        total_sale_amount = 0
        shares_to_sell = shares_sold

        # Process sale while there are shares to sell and purchases left
        while shares_to_sell > 0 and not self.purchases.is_empty():
            purchase = self.purchases.get_front()

            if purchase.shares <= shares_to_sell:
                # If purchase has equal or fewer shares than required, sell all from this purchase
                total_sale_amount += purchase.shares * sell_price_per_share
                shares_to_sell -= purchase.shares
                self.purchases.remove_front()
            else:
                # If purchase has more shares than required, sell partial amount and update purchase
                total_sale_amount += shares_to_sell * sell_price_per_share  
                purchase.shares -= shares_to_sell
                shares_to_sell = 0  
        
        # If not enough shares were available to meet the sell request
        if shares_to_sell > 0:
            print(f"Warning: Not enough shares to sell for {self.stock_symbol}. {shares_to_sell} unsold.")
        
        return total_sale_amount        
    
    def __str__(self): 
        # String representation of all purchase details for this stock symbol
        purchase_details = []
        current = self.purchases.front
        while current:
            # Format each purchase with number of shares and cost per share
            purchase_details.append(f"{current.data.shares} shares @ {current.data.cost_per_share:.2f}")
            current = current.next_node
        return f"{self.stock_symbol}: " + ", ".join(purchase_details)