class Stack:
    def __init__(self, items=[], limit=100):
        self.items = items.copy()  # Use a copy to avoid modifying the input list
        self.limit = limit         # Set the stack's size limit

    def isEmpty(self):
        return len(self.items) == 0  # True if stack is empty, False otherwise

    def push(self, item):
        if len(self.items) >= self.limit:  # Check if stack is full
            return False                   # Return False if no room (permissive approach)
        self.items.append(item)            # Add item to the top
        return True                        # Return True to indicate success

    def pop(self):
        if self.isEmpty():        # Check if stack is empty
            return None           # Return None if nothing to pop
        return self.items.pop()   # Remove and return the top item

    def peek(self):
        if self.isEmpty():        # Check if stack is empty
            return None           # Return None if nothing to peek
        return self.items[-1]     # Return the top item without removing it
    
    def size(self):
        return len(self.items)    # Return the current number of items

    def full(self):
        return len(self.items) >= self.limit  # True if stack is at or above limit

    def search(self, target):
        for i in range(len(self.items) - 1, -1, -1):  # From top (end) to bottom
            if self.items[i] == target:
                return len(self.items) - 1 - i    # Distance from top
        return -1  