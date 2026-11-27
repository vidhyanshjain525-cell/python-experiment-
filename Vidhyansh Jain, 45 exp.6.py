

while True:
    password = input("Enter password (or type 'stop' to exit): ")

    if password == "stop":
        break

    has_upper = False
    has_lower = False

    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True

    if len(password) >= 8 and has_upper and has_lower:
        print("Password is Strong")
    else:
        print("Password is Weak")