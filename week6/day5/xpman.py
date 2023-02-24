import psycopg2
import secrets


class RestaurantMenuManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        db_host = secrets.host
        db_user = secrets.user
        db_password = secrets.password
        self.conn = psycopg2.connect(
            host=db_host, user=db_user, password=db_password, dbname="day6"
        )
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        query = """CREATE TABLE IF NOT EXISTS menu_items
                    (item_id SERIAL PRIMARY KEY,
                     item_name TEXT NOT NULL,
                     item_price NUMERIC(6, 2) NOT NULL)"""
        self.cursor.execute(query)
        self.conn.commit()

    def add_item(self):
        item_name = input("Enter the name of the menu item: ")
        item_price = float(input("Enter the price of the menu item: "))
        query = "INSERT INTO menu_items (item_name, item_price) VALUES (%s, %s)"
        self.cursor.execute(query, (item_name, item_price))
        self.conn.commit()
        print("Menu item added successfully!")

    def edit_item(self):
        item_id = input("Enter the ID of the menu item you want to edit: ")
        item_name = input("Enter the new name of the menu item: ")
        item_price = float(input("Enter the new price of the menu item: "))
        query = (
            "UPDATE menu_items SET item_name = %s, item_price = %s WHERE item_id = %s"
        )
        self.cursor.execute(query, (item_name, item_price, item_id))
        self.conn.commit()
        print("Menu item updated successfully!")

    def delete_item(self):
        item_id = input("Enter the ID of the menu item you want to delete: ")
        query = "DELETE FROM menu_items WHERE item_id = %s"
        self.cursor.execute(query, (item_id,))
        self.conn.commit()
        print("Menu item deleted successfully!")

    def update_price(self):
        item_id = input(
            "Enter the ID of the menu item you want to update the price for: "
        )
        item_price = float(input("Enter the new price of the menu item: "))
        query = "UPDATE menu_items SET item_price = %s WHERE item_id = %s"
        self.cursor.execute(query, (item_price, item_id))
        self.conn.commit()
        print("Menu item price updated successfully!")

    def print_items(self):
        query = "SELECT * FROM menu_items"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        print("ID\tName\tPrice")
        for row in results:
            print(str(row[0]) + "\t" + row[1] + "\t$" + str(row[2]))

    def print_price(self):
        item_name = input("Enter the name of the menu item: ")
        query = "SELECT item_price FROM menu_items WHERE item_name = %s"
        self.cursor.execute(query, (item_name,))
        result = self.cursor.fetchone()
        if result:
            print(f"The price of {item_name} is ${result[0]}")
        else:
            print("Menu item not found.")

    def close(self):
        self.conn.close()


def print_menu_options():
    print("\nPlease select an option:")
    print("1. Add a new menu item")
    print("2. Edit a menu item")
    print("3. Delete a menu item")
    print("4. Update the price of a menu item")
    print("5. Print all menu items")
    print("6. Print the price of a menu item")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")
    if choice == "1":
        menu_manager.add_item()
        print_menu_options()
    elif choice == "2":
        menu_manager.edit_item()
        print_menu_options()
    elif choice == "3":
        menu_manager.delete_item()
        print_menu_options()
    elif choice == "4":
        menu_manager.update_price()
        print_menu_options()
    elif choice == "5":
        menu_manager.print_items()
        print_menu_options()
    elif choice == "6":
        menu_manager.print_price()
        print_menu_options()
    elif choice == "7":
        print("Exiting...")
        menu_manager.close()
        return False
    else:
        print("Invalid input, please try again.")
        print_menu_options()


menu_manager = RestaurantMenuManager("restaurant_menu_db")
menu_manager.connect()
print_menu_options()
menu_manager.close()
