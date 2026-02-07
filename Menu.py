# Restaurant Menu
menu = {
    "Pizza": 280,
    "Burger": 110,
    "Pasta": 150,
    "Coffee": 60,
    "Cold Drinks": 50,
    "Noodles": 140,
    "Cold Coffee": 120,
    "Ice-Cream": 80
}

# Greeting
print("🎉 Welcome to Our Restaurant 🎉")
print("Type the item name to order")
print("Type 'no' to finish your order\n")

# Display Menu
print("🍽️ ------ MENU ------ 🍽️")
for item, price in menu.items():
    print(f"{item} : ₹{price}")

order_total = 0

# Ordering Loop
while True:
    choice = input("\nEnter item name: ").title()

    if choice == "No":
        print("\n📄 ------ BILL ------ 📄")
        print(f"Total Amount to Pay: ₹{order_total}")
        print("Thank you for visiting! 😊")
        break

    elif choice in menu:
        order_total += menu[choice]
        print(f"✅ {choice} added successfully!")
        print(f"Current Total: ₹{order_total}")

    else:
        print("❌ Sorry, this item is not available.")
        print("Please choose from the menu.")
