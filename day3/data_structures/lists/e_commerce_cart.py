class Cart:
    def __init__(self):
        self.products = []
    
    def add(self, item):
        self.products.append(item)
    
    def remove(self, item):
        self.products.remove(item)
    
    def search(self, item):
        if item in self.products:
            return True
        else:
            return False
    
    def sort_items(self):
        self.products.sort()
        
    def size(self):
        return len(self.products)

    def clear(self):
        self.products.clear()
    
    def display(self):
        print('-'*30)
        print('YOUR CART')
        print('-'*30)
        print(f'Total Number of items: {self.size()}')
        
        self.sort_items()
        print(f'Items: ')
        for item in self.products:
            print(item, end=', ')


items = ['Laptop', 'Headphones', 'Mouse', 'Keyboard', 'Mouse Pad', 'Laptop Stand']
my_cart = Cart()
for item in items:
    my_cart.add(item)

my_cart.display()
