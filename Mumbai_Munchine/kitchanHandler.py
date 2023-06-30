class Snack:
    def __init__(self, snack_id, name, price, availability):
        self.snack_id = snack_id
        self.name = name
        self.price = price
        self.availability = availability


class Canteen:
    def __init__(self):
        self.inventory = {}
        self.sales_records = []

    def add_snack(self, snack):
        self.inventory[snack.snack_id] = snack

    def remove_snack(self, snack_id):
        if snack_id in self.inventory:
            del self.inventory[snack_id]
            print("Snack removed from inventory.")
        else:
            print("Snack not found in inventory.")

    def update_snack_availability(self, snack_id, availability):
        if snack_id in self.inventory:
            snack = self.inventory[snack_id]
            snack.availability = availability
            print("Snack availability updated.")
        else:
            print("Snack not found in inventory.")

    def record_sale(self, snack_id):
        if snack_id in self.inventory:
            snack = self.inventory[snack_id]
            if snack.availability == "yes":
                self.sales_records.append(snack)
                snack.availability = "no"
                print("Sale recorded.")
            else:
                print("Snack not available for sale.")
        else:
            print("Snack not found in inventory.")

    def print_inventory(self):
        print("Current Snack Inventory:")
        for snack_id, snack in self.inventory.items():
            print(f"Snack ID: {snack_id}")
            print(f"Name: {snack.name}")
            print(f"Price: {snack.price}")
            print(f"Availability: {snack.availability}")
            print()

    def print_sales_records(self):
        print("Sales Records:")
        for snack in self.sales_records:
            print(f"Snack ID: {snack.snack_id}")
            print(f"Name: {snack.name}")
            print(f"Price: {snack.price}")
            print()


def main():
    canteen = Canteen()

    while True:
        print("Welcome to Mumbai Munchies Canteen System!")
        print("1. Add Snack")
        print("2. Remove Snack")
        print("3. Update Snack Availability")
        print("4. Record Sale")
        print("5. Print Snack Inventory")
        print("6. Print Sales Records")
        print("7. Quit")
        print("============================================")
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            snack_id = input("Enter snack ID: ")
            name = input("Enter snack name: ")
            price = input("Enter snack price: ")
            availability = input("Enter snack availability (yes/no): ")
            snack = Snack(snack_id, name, price, availability)
            canteen.add_snack(snack)

        elif choice == "2":
            snack_id = input("Enter snack ID to remove: ")
            canteen.remove_snack(snack_id)

        elif choice == "3":
            snack_id = input("Enter snack ID to update availability: ")
            availability = input("Enter updated availability (yes/no): ")
            canteen.update_snack_availability(snack_id, availability)

        elif choice == "4":
            snack_id = input("Enter snack ID sold: ")
            canteen.record_sale(snack_id)

        elif choice == "5":
            canteen.print_inventory()

        elif choice == "6":
            canteen.print_sales_records()

        elif choice == "7":
            print("Thank you for using Mumbai Munchies Canteen System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
