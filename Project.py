import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Define the Product class
start_time = datetime.now()

#product class
class Product:
    def __init__(self, name, price, stock, min_stock, expiry_date):
        self.name = name
        self.price = price
        self.stock = stock
        self.min_stock = min_stock
        self.expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d")  # Store expiry as datetime object

    def is_below_threshold(self):
        #Check if stock is below the min 
        return self.stock <= self.min_stock

    def is_expired(self):
        #Check if the product is expired
        return datetime.now() > self.expiry_date

    def update_stock(self, quantity):
        #Update the stock after selling or restocking
        self.stock += quantity

# Define the Inventory class
class Inventory:
    def __init__(self):
        self.products = []  # List of Product objects
        self.sales_history = []  # Sales records
        self.min_stock = []  # Reorder records
        self.daily_sales = []  # Daily sales tracking

    def add_product(self, product):
        #Add a product to the inventory
        self.products.append(product)
        print(f"Product {product.name} added to inventory with expiry date {product.expiry_date.date()}.")

    def remove_product(self, name):
        #Remove a product from the inventory
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"Product {name} removed from inventory.")
                return
        print(f"Product {name} not found in inventory.")

    def sell_product(self, name, quantity):
        #Sell a product and update stock and sales history
        for product in self.products:
            if product.name == name:
                if product.is_expired():
                    print(f"Product {name} has expired and cannot be sold.")
                    return
                if product.stock >= quantity:
                    product.update_stock(-quantity)
                    sale_amount = quantity * product.price
                    sale_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    self.sales_history.append((name, quantity, sale_amount, sale_time))
                    self.daily_sales.append((sale_time, sale_amount))
                    print(f"Sold {quantity} units of {name}. Sale amount: Rs{sale_amount:.2f}")
                    return
                else:
                    print(f"Insufficient stock for {name}. Available stock: {product.stock}")
                    return
        print(f"Product {name} not found in inventory.")


    def plot_inventory(self):
        #Plot inventory levels over time using Matplotlib."""
        product_names = [product.name for product in self.products]
        product_stocks = [product.stock for product in self.products]

        # Plot inventory levels
        plt.figure(figsize=(10, 6))
        bars = plt.bar(product_names, product_stocks, color='pink')
        plt.title('Inventory Levels')
        plt.xlabel('Product Name')
        plt.ylabel('Stock Quantity')
        plt.xticks(rotation=45)

        # Adding text on top of each bar
        for bar in bars:
            height = bar.get_height()
            # Add value text above the bars
            plt.text(bar.get_x() + bar.get_width() / 2, height + 1, f'{height}', ha='center', va='bottom', fontsize=10, color='black')

        plt.tight_layout()
        plt.show()

    def generate_sales_report(self):
        #Generate a sales report showing all sales."""
        print("\nSales Report:")
        if not self.sales_history:
            print("No sales have been made yet.")
        else:
            total_sales = 0
            for name, quantity, sale_amount, sale_time in self.sales_history:
                print(f"Product: {name}, Quantity Sold: {quantity}, Sale Amount: Rs{sale_amount:.2f}, Time: {sale_time}")
                total_sales += sale_amount
            print(f"Total Sales: Rs.{total_sales:.2f}")

    def generate_daily_sales_report(self):
        #Generate a daily sales report."""
        print("\nDaily Sales Report:")
        if not self.daily_sales:
            print("No sales data available for today.")
        else:
            daily_total = 0
            for sale_time, sale_amount in self.daily_sales:
                print(f"Time: {sale_time}, Sale Amount: Rs{sale_amount:.2f}")
                daily_total += sale_amount
            print(f"Total Sales for Today: Rs.{daily_total:.2f}")

# Example usage of Inventory Management System
if __name__ == "__main__":
    # Record start time to calculate runtime
    #start_time = datetime.now()

    # Create the inventory system
    inventory = Inventory()

    # Add products to the inventory with expiry dates
    inventory.add_product(Product("Aspirin", 0.50, 100, 20, "2025-12-31"))
    inventory.add_product(Product("Tylenol", 1.00, 50, 10, "2024-06-30"))
    inventory.add_product(Product("Amoxicillin", 2.00, 30, 10, "2023-11-30"))

    # Simulate selling products
    inventory.sell_product("Aspirin", 10)
    inventory.sell_product("Tylenol", 5)
    inventory.sell_product("Aspirin", 30)  # Selling more Aspirin
    inventory.sell_product("Amoxicillin", 2)

    # Check for reorders
   # inventory.check_reorders()

    # Generate sales reports
    inventory.generate_sales_report()
    inventory.generate_daily_sales_report()

    # Plot inventory levels
    inventory.plot_inventory()

    # Calculate runtime and display it
    end_time = datetime.now()
    runtime = end_time - start_time
    print(f"Program runtime: {runtime} s")