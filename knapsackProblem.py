class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        
    # @property    
    def ratio(self):
        return self.value / self.weight
        
def knapsack(items, capacity):
    items.sort(key=lambda item: item.ratio(), reverse=True)
    
    total_value = 0
    
    for item in items:
        if capacity == 0:
            break
        
        if item.weight <= capacity:
            capacity -= item.weight
            total_value += item.value
            
        else:
            fraction = capacity / item.weight
            total_value += item.value * fraction
            capacity = 0
            
    return total_value        
    
    
items = [Item(25, 18), Item(24, 15), Item(15, 10)]
capacity = 20
print("knapsack profit is: ", knapsack(items, capacity))
    
    
        