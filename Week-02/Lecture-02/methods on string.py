s = input("Enter a string: ")

# 1. upper()
# Converts string to uppercase
print("\n1. upper()")
print(s.upper())


# 2. lower()
# Converts string to lowercase
print("\n2. lower()")
print(s.lower())


# 3. capitalize()
# First character uppercase, remaining lowercase
print("\n3. capitalize()")
print(s.capitalize())


# 4. title()
# First letter of every word becomes uppercase
print("\n4. title()")
print(s.title())


# 5. swapcase()
# Uppercase becomes lowercase and vice versa
print("\n5. swapcase()")
print(s.swapcase())


# 6. strip()
# Removes whitespace from both beginning and end
print("\n6. strip()")
print(s.strip())


# 7. lstrip()
# Removes whitespace from the left side
print("\n7. lstrip()")
print(s.lstrip())


# 8. rstrip()
# Removes whitespace from the right side
print("\n8. rstrip()")
print(s.rstrip())


# 9. replace()
# Replaces a part of the string
old = input("\nEnter the text to replace: ")
new = input("Enter the new text: ")

print("\n9. replace()")
print(s.replace(old, new))


# 10. split()
# Converts string into a list
print("\n10. split()")
print(s.split())


# 11. join()
# Joins list elements into one string
words = s.split()

print("\n11. join()")
print("-".join(words))


# 12. find()
# Returns index of first occurrence
# Returns -1 if not found
search = input("\nEnter text to find: ")

print("\n12. find()")
print(s.find(search))


# 13. index()
# Returns index of first occurrence
# Raises ValueError if not found
print("\n13. index()")

if search in s:
    print(s.index(search))
else:
    print("ValueError: substring not found")


# 14. count()
# Counts how many times substring occurs
print("\n14. count()")
print(s.count(search))


# 15. startswith()
# Checks whether string starts with given value
start = input("\nEnter prefix to check: ")

print("\n15. startswith()")
print(s.startswith(start))


# 16. endswith()
# Checks whether string ends with given value
end = input("Enter suffix to check: ")

print("\n16. endswith()")
print(s.endswith(end))


# 17. isalpha()
# Checks whether all characters are alphabets
print("\n17. isalpha()")
print(s.isalpha())


# 18. isdigit()
# Checks whether all characters are digits
print("\n18. isdigit()")
print(s.isdigit())


# 19. isalnum()
# Checks whether string contains only alphabets and digits
print("\n19. isalnum()")
print(s.isalnum())


# 20. isspace()
# Checks whether string contains only whitespace
print("\n20. isspace()")
print(s.isspace())