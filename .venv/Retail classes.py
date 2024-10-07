class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def apply_discount(self, percentage):
        self.price -= self.price * (percentage / 100)

    def restock(self, amount):
        self.quantity += amount

    def sell(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            print(f"{amount} units of {self.name} sold.")
        else:
            print(f"Not enough stock for {self.name}.")

# Managing a small inventory of products
product1 = Product(1, "Laptop", 1200.0, 5)
product2 = Product(2, "Mouse", 150, 250)

# Restock and apply discount
product1.restock(10)
product2.apply_discount(15)

# Sell a product
product1.sell(3)
product2.sell(60)  # This will trigger a "Not enough stock" message
