sandwich_orders = [
    "Tuna sandwich",
    "Avocado sandwich",
    "Egg sandwich",
    "Sabih sandwich",
    "Pastrami sandwich",
]

sandwich_orders.append("Pastrami sandwich")
sandwich_orders.append("Pastrami sandwich")

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

print("Deli has run out of pastrami.")

finished_sandwiches = []

for sand in sandwich_orders:
    finished_sandwiches.append(sand)

for sandfin in finished_sandwiches:
    print(f"I nmade your {sandfin}.")

print(sandwich_orders)
