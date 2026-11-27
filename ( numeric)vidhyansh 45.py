print("===== CALCULATOR =====")

try:
    # Input two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Basic calculations
    print("\n--- Basic Calculations ---")
    print("Addition =", num1 + num2)
    print("Subtraction =", num1 - num2)
    print("Multiplication =", num1 * num2)

    if num2 != 0:
        print("Division =", num1 / num2)
    else:
        print("Division = Cannot divide by zero")

    # Ask user for advanced calculations
    choice = input("\nDo you want advanced calculations? (yes/no): ").lower()

    if choice == "yes":
        print("\n--- Advanced Calculations ---")
        print("Exponentiation =", num1 ** num2)

        if num2 != 0:
            print("Modulus =", num1 % num2)
            print("Floor Division =", num1 // num2)
        else:
            print("Modulus = Cannot divide by zero")
            print("Floor Division = Cannot divide by zero")

    elif choice == "no":
        print("\nAdvanced calculations skipped.")

    else:
        print("\nInvalid choice. Please enter 'yes' or 'no'.")

except ValueError:
    print("Error: Invalid input! Please enter numbers only.")