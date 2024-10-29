class DLNode: 
    def __init__(self, data=None, previous_node=None, next_node=None): 
        # Initialize a doubly linked node with data and pointers to previous and next nodes
        self.data = data 
        self.previous_node = previous_node 
        self.next_node = next_node 

class LinkedDeque: 
    def __init__(self): 
        # Initialize an empty deque with front and back pointers and size counter
        self.front = None 
        self.back = None 
        self.size = 0 

    def add_to_back(self, new_entry): 
        # Add a new entry to the back of the deque
        new_node = DLNode(new_entry) 
        if self.is_empty(): 
            # If the deque is empty, set front and back to the new node
            self.front = self.back = new_node 
        else: 
            # Link the new node to the back of the deque
            new_node.previous_node = self.back 
            self.back.next_node = new_node 
            self.back = new_node  
        self.size += 1

    def add_to_front(self, new_entry): 
        # Add a new entry to the front of the deque
        new_node = DLNode(new_entry)  
        if self.is_empty(): 
            # If the deque is empty, set front and back to the new node
            self.front = self.back = new_node 
        else: 
            # Link the new node to the front of the deque
            new_node.next_node = self.front 
            self.front.previous_node = new_node 
            self.front = new_node  
        self.size += 1 

    def remove_front(self): 
        # Remove and return the entry at the front of the deque
        if self.is_empty(): 
            raise IndexError("Deque is empty") 
        data = self.front.data  
        if self.front == self.back: 
            # If there's only one node, set front and back to None
            self.front = self.back = None 
        else: 
            # Move the front pointer to the next node
            self.front = self.front.next_node 
            self.front.previous_node = None 
        self.size -= 1 
        return data  
    
    def get_front(self):
        # Return the data at the front of the deque without removing it
        if self.is_empty():
            raise IndexError("Deque is empty") 
        return self.front.data 
    
    def remove_back(self): 
        # Remove and return the entry at the back of the deque
        if self.is_empty(): 
            raise IndexError("Deque is empty") 
        data = self.back.data  
        if self.front == self.back: 
            # If there's only one node, set front and back to None
            self.front = self.back = None 
        else: 
            # Move the back pointer to the previous node
            self.back = self.back.previous_node 
            self.back.next_node = None  
        self.size -= 1  
        return data 
    
    def is_empty(self): 
        # Check if the deque is empty
        return self.size == 0 
    
    def display(self): 
        # Print all entries in the deque from front to back
        current = self.front 
        while current: 
            print(current.data)  
            current = current.next_node  