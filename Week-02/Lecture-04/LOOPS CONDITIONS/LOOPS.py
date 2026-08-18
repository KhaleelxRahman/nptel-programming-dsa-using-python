
# 1. FOR LOOP
print("1. FOR LOOP")
for i in range(1, 6):
    print(i)


# 2. FOR LOOP WITH STRING
print("\n2. FOR LOOP WITH STRING")
name = "PYTHON"
for char in name:
    print(char)


# 3. FOR LOOP WITH LIST
print("\n3. FOR LOOP WITH LIST")
numbers = [10, 20, 30, 40, 50]
for num in numbers:
    print(num)


# 4. WHILE LOOP
print("\n4. WHILE LOOP")
i = 1
while i <= 5:
    print(i)
    i += 1


# 5. NESTED FOR LOOP
print("\n5. NESTED FOR LOOP")
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


# 6. BREAK
print("\n6. BREAK")
for i in range(1, 10):
    if i == 5:
        break
    print(i)


# 7. CONTINUE
print("\n7. CONTINUE")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# 8. PASS
print("\n8. PASS")
for i in range(1, 6):
    if i == 3:
        pass
    print(i)


# 9. WHILE LOOP WITH BREAK
print("\n9. WHILE LOOP WITH BREAK")
i = 1
while i <= 10:
    if i == 6:
        break
    print(i)
    i += 1


# 10. WHILE LOOP WITH CONTINUE
print("\n10. WHILE LOOP WITH CONTINUE")
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)