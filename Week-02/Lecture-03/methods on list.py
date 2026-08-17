
numbers = list(map(int, input("Enter list elements: ").split()))

print("\nOriginal List:", numbers)


# 1. append()
# Adds ONE element at the end
a = numbers.copy()
a.append(100)

print("\n1. append()")
print(a)


# 2. extend()
# Adds multiple elements at the end
a = numbers.copy()
a.extend([100, 200, 300])

print("\n2. extend()")
print(a)


# 3. insert()
# Adds an element at a specified index
a = numbers.copy()
a.insert(1, 100)

print("\n3. insert()")
print(a)


# 4. remove()
# Removes the first occurrence of a value
a = numbers.copy()

if len(a) > 0:
    value = a[0]
    a.remove(value)

print("\n4. remove()")
print(a)


# 5. pop()
# Removes and returns an element
a = numbers.copy()

if len(a) > 0:
    removed = a.pop()

print("\n5. pop()")
print("Removed:", removed if len(numbers) > 0 else "Nothing")
print("List:", a)


# 6. clear()
# Removes all elements from the list
a = numbers.copy()
a.clear()

print("\n6. clear()")
print(a)


# 7. index()
# Returns the index of the first occurrence
a = numbers.copy()

if len(a) > 0:
    value = a[0]

    print("\n7. index()")
    print(a.index(value))


# 8. count()
# Counts how many times a value occurs
a = numbers.copy()

if len(a) > 0:
    value = a[0]

    print("\n8. count()")
    print(a.count(value))


# 9. sort()
# Sorts the list in ascending order
a = numbers.copy()
a.sort()

print("\n9. sort()")
print(a)


# 10. reverse()
# Reverses the order of elements
a = numbers.copy()
a.reverse()

print("\n10. reverse()")
print(a)


# 11. copy()
# Creates a shallow copy of the list
a = numbers.copy()
b = a.copy()

print("\n11. copy()")
print("Original:", a)
print("Copy:", b)