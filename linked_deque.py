class DLNode: 
    def __init__(self, data=None, previous_node=None, next_node=None): 
        self.data = data 
        self.previous_node = previous_node 
        self.next_node = next_node 

class LinkedDeque: 
    def __init__(self): 
        self.front = None 
        self.back = None 
        self.size = 0 

    def add_to_back(self, new_entry): 
        new_node = DLNode(new_entry) 
        if self.is_empty(): 
            self.front = self.back = new_node 
        else: 
            new_node.previous_node = self.back 
            self.back.next_node = new_node 
            self.back = new_node 
        self.size += 1 

    def add_to_front(self, new_entry): 
        new_node = DLNode(new_entry) 
        if self.is_empty(): 
            self.front = self.back = new_node 
        else: 
            new_node.next_node = self.front 
            self.front.previous_node = new_node 
            self.front = new_node 
        self.size += 1 

    def remove_front(self): 
        if self.is_empty(): 
            raise IndexError("Deque is empty") 
        data = self.front.data 
        if self.front == self.back: 
            self.front = self.back = None 
        else: 
            self.front = self.front.next_node 
            self.front.previous_node = None 
        self.size -= 1 
        return data 
    
    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.front.data
    
    def remove_back(self): 
        if self.is_empty(): 
            raise IndexError("Deque is empty") 
        data = self.back.data 
        if self.front == self.back: 
            self.front = self.back = None 
        else: 
            self.back = self.back.previous_node 
            self.back.next_node = None 
        self.size -= 1 
        return data 
    
    def is_empty(self): 
        return self.size == 0 
    
    def display(self): 
        current = self.front 
        while current: 
            print(current.data) 
            current = current.next_node
