
class Customer:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
        self.purchased_cars = []

    def purchase_car(self, dealership, car_make, car_model):
        # Find car in the dealership's inventory
        car = next((c for c in dealership.cars if c['make'] == car_make and c['model'] == car_model), None)
        
        if car and car['stock'] > 0:
            # Process sale
            car['stock'] -= 1
            self.purchased_cars.append(car)
            print(f"{self.name} purchased a {car['make']} {car['model']}!")
            dealership.sales.append((self.name, car['make'], car['model'], car['price']))
        else:
            print(f"Sorry, {car_make} {car_model} is out of stock or not found.")

class Dealership:
    def __init__(self, name):
        self.name = name
        self.cars = []  # List of car dictionaries
        self.sales = []  # List of sales transactions (tuples)

    def add_car(self, make, model, year, price, stock):
        car = {'make': make, 'model': model, 'year': year, 'price': price, 'stock': stock}
        self.cars.append(car)

    def show_inventory(self):
        if not self.cars:
            print("No cars available in the dealership.")
        else:
            for car in self.cars:
                print(f"{car['year']} {car['make']} {car['model']} - ${car['price']} ({car['stock']} in stock)")

    def show_sales(self):
        if not self.sales:
            print("No sales have been made yet.")
        else:
            for sale in self.sales:
                print(f"{sale[0]} bought a {sale[1]} {sale[2]} for ${sale[3]}")

# Example usage
def main():
    # Create dealership
    dealership = Dealership("Best Cars Dealership")

    # Add some cars to inventory
    dealership.add_car("Toyota", "Camry", 2023, 25000, 5)
    



    # Display available cars
    print("Available Cars:")
    dealership.show_inventory()

if __name__ == "__main__":
    main()
