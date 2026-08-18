# NESTED IF STATEMENT

age = int(input("Enter your age: "))
citizen = input("Are you an Indian citizen? (yes/no): ")
                
if age >= 18:
    if citizen == "yes":
        print("You are eligible to vote.")
    else:
        print("You must be an Indian citizen to vote.")
else:
    print("You are not eligible to vote.")