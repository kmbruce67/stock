class StockControl:
    def __init__(self):
        self.products = {}

    def add_product(self):
        product_id = input("Enter product ID: ")
        quantity = int(input("Enter quantity: "))
        self.products[product_id] = self.products.get(product_id, 0) + quantity
        print(f"Added {quantity} units of product {product_id}.")

    def remove_product(self):
        product_id = input("Enter product ID to remove: ")
        quantity = int(input("Enter quantity to remove: "))
        if product_id in self.products and self.products[product_id] >= quantity:
            self.products[product_id] -= quantity
            if self.products[product_id] == 0:
                del self.products[product_id]
            print(f"Removed {quantity} units of product {product_id}.")
        else:
            print("Not enough stock or product not found.")

    def show_stock(self):
        print("Products in stock:")
        for product_id, quantity in self.products.items():
            print(f"Product ID: {product_id}, Quantity: {quantity}")

    def show_moving_products(self):
        product_id = input("Enter product ID to check movement: ")
        quantity = int(input("Enter quantity to check movement: "))
        if product_id in self.products and self.products[product_id] >= quantity:
            print(f"Product ID: {product_id} is moving, Quantity: {quantity}")
        else:
            print("Product not found or not enough stock to move.")

# Main program
stock_control = StockControl()

while True:
    print("\nStock Control System")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Show Stock")
    print("4. Show Moving Products")
    print("5. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        stock_control.add_product()
    elif choice == '2':
        stock_control.remove_product()
    elif choice == '3':
        stock_control.show_stock()
    elif choice == '4':
        stock_control.show_moving_products()
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
