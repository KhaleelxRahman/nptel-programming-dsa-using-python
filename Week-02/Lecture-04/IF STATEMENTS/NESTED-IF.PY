age = int(input("Enter your age: "))
if age >= 18:
    has_id = input("Do you have ID? (yes/no): ")
    if has_id == "yes":
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Under 18")