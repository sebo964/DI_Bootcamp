# import psycopg2
# import secrets

# # Define the database credentials
# db_host = secrets.host
# db_user = secrets.user
# db_password = secrets.password
# db_name = "day6"

# # Establish a connection to the database
# conn = psycopg2.connect(
#     host=db_host, user=db_user, password=db_password, dbname=db_name
# )

# # Create table to hold the menu items
# cursor = conn.cursor()
# query = """CREATE TABLE IF NOT EXISTS menu_items
#             (item_id SERIAL PRIMARY KEY,
#              item_name TEXT NOT NULL,
#              item_price NUMERIC(6, 2) NOT NULL)"""
# cursor.execute(query)
# conn.commit()


# # Function to add a new menu item to the database
# def add_item():
#     item_name = input("Enter the name of the menu item: ")
#     item_price = input("Enter the price of the menu item: ")
#     query = "INSERT INTO menu_items (item_name, item_price) VALUES (%s, %s)"
#     cursor.execute(query, (item_name, item_price))
#     conn.commit()
#     print("Menu item added successfully!")


# # Function to edit an existing menu item in the database
# def edit_item():
#     item_id = input("Enter the ID of the menu item you want to edit: ")
#     item_name = input("Enter the new name of the menu item: ")
#     item_price = input("Enter the new price of the menu item: ")
#     query = "UPDATE menu_items SET item_name = %s, item_price = %s WHERE item_id = %s"
#     cursor.execute(query, (item_name, item_price, item_id))
#     conn.commit()
#     print("Menu item updated successfully!")


# # Function to delete a menu item from the database
# def delete_item():
#     item_id = input("Enter the ID of the menu item you want to delete: ")
#     query = "DELETE FROM menu_items WHERE item_id = %s"
#     cursor.execute(query, (item_id,))
#     conn.commit()
#     print("Menu item deleted successfully!")


# # Function to update the price of a menu item in the database
# def update_price():
#     item_id = input("Enter the ID of the menu item you want to update the price for: ")
#     item_price = input("Enter the new price of the menu item: ")
#     query = "UPDATE menu_items SET item_price = %s WHERE item_id = %s"
#     cursor.execute(query, (item_price, item_id))
#     conn.commit()
#     print("Menu item price updated successfully!")


# # Function to print all the menu items in the database
# def print_items():
#     query = "SELECT * FROM menu_items"
#     cursor.execute(query)
#     results = cursor.fetchall()
#     print("ID\tName\tPrice")
#     for row in results:
#         print(str(row[0]) + "\t" + row[1] + "\t$" + str(row[2]))


# # Function to print the price of a menu item chosen by the user
# def print_price():
#     item_name = input("Enter the name of the menu item: ")
#     query = "SELECT item_price FROM menu_items WHERE item_name = %s"
#     cursor.execute(query, (item_name,))
#     result = cursor.fetchone()
#     if result:
#         print(f"The price of {item_name} is ${result[0]}")
#     else:
#         print("Menu item not found.")


# # Close the database connection


# # Function to print the menu options
# # Function to print the menu options
# def print_menu():
#     while True:
#         print("\nWelcome to the restaurant menu management system!\n")
#         print("Please select an option:")
#         print("1. Add a new menu item")
#         print("2. Edit a menu item")
#         print("3. Delete a menu item")
#         print("4. Update the price of a menu item")
#         print("5. Print all menu items")
#         print("6. Print the price of a menu item")
#         print("7. Exit")
#         choice = input("Enter your choice (1-7): ")
#         if choice == "1":
#             add_item()
#         elif choice == "2":
#             edit_item()
#         elif choice == "3":
#             delete_item()
#         elif choice == "4":
#             update_price()
#         elif choice == "5":
#             print_items()
#         elif choice == "6":
#             print_price()
#         elif choice == "7":
#             print("Exiting...")
#             conn.close()
#             break
#         else:
#             print("Invalid input, please try again.")


# print_menu()


import psycopg2
import secrets


class MenuManagementSystem:
    def __init__(self):
        self.db_host = secrets.host
        self.db_user = secrets.user
        self.db_password = secrets.password
        self.db_name = "day6"
        self.conn = psycopg2.connect(
            host=self.db_host,
            user=self.db_user,
            password=self.db_password,
            dbname=self.db_name,
        )
        self.cursor = self.conn.cursor()
        self.menu_items = []

    def create_table(self):
        query = """CREATE TABLE IF NOT EXISTS menu_items
                    (item_id SERIAL PRIMARY KEY,
                     item_name TEXT NOT NULL,
                     item_price NUMERIC(6, 2) NOT NULL)"""
        self.cursor.execute(query)
        self.conn.commit()

    def add_item(self):
        item_name = input("Enter the name of the menu item: ")
        item_price = input("Enter the price of the menu item: ")
        query = "INSERT INTO menu_items (item_name, item_price) VALUES (%s, %s)"
        self.cursor.execute(query, (item_name, item_price))
        self.conn.commit()
        print("Menu item added successfully!")

    def edit_item(self):
        item_id = input("Enter the ID of the menu item you want to edit: ")
        item_name = input("Enter the new name of the menu item: ")
        item_price = input("Enter the new price of the menu item: ")
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
        item_price = input("Enter the new price of the menu item: ")
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

    def print_menu():
        while True:
            print("\nWelcome to the restaurant menu management system!\n")
            print("Please select an option:")
            print("1. Add a new menu item")
            print("2. Edit a menu item")
            print("3. Delete a menu item")
            print("4. Update the price of a menu item")
            print("5. Print all menu items")
            print("6. Print the price of a menu item")
            print("7. Exit")
            choice = input("Enter your choice (1-7): ")
            if choice == "1":
                add_item()
            elif choice == "2":
                edit_item()
            elif choice == "3":
                delete_item()
            elif choice == "4":
                update_price()
            elif choice == "5":
                print_items()
            elif choice == "6":
                print_price()
            elif choice == "7":
                print("Exiting...")
                conn.close()
                break
            else:
                print("Invalid input, please try again.")


if __name__ == "__main__":
    menu = MenuManagementSystem()
    menu.create_table()
    menu.print_menu()
