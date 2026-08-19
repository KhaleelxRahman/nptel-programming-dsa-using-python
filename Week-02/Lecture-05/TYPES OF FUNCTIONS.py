
# 1. BUILT-IN FUNCTIONS
print("Hello Python")

numbers = [10, 20, 30, 40, 50]

print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
print("Type:", type(numbers))


# 2. USER-DEFINED FUNCTION
def greet():
    print("Hello Khaleel!")
greet()


# 3. FUNCTION WITH PARAMETERS
def add(a, b):
    print("Addition:", a + b)
add(10, 20)


# 4. FUNCTION WITH RETURN VALUE
def square(n):
    return n * n
result = square(5)
print("Square:", result)


# 5. DEFAULT ARGUMENT
def welcome(name="User"):
    print("Welcome", name)
welcome()
welcome("Khaleel")


# 6. KEYWORD ARGUMENT
def student(name, age, branch):
    print("Name:", name)
    print("Age:", age)
    print("Branch:", branch)
student(
    branch="AI & ML",
    name="Khaleel",
    age=19
)


# 7. * function
def add_many(*numbers):
    return sum(numbers)
print("Sum using *args:", add_many(10, 20, 30, 40))


# 8. **function
def student_details(**details):
    print("Student Details:", details)


student_details(
    name="Khaleel",
    age=19,
    branch="AI & ML"
)


# 9. LAMBDA FUNCTION
square_lambda = lambda x: x * x
print("Lambda Square:", square_lambda(6))
multiply = lambda a, b: a * b

print("Lambda Multiplication:", multiply(5, 4))


# 10. RECURSIVE FUNCTION
def factorial(n):

 if n == 0:
        return 1
 else:
        return n * factorial(n - 1)
print("Factorial:", factorial(5))



# BONUS: MAP()
numbers = [1, 2, 3, 4, 5]
squares = [x * x for x in numbers] 
print("Squares using map:", squares)

# BONUS: FILTER()
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print("Even numbers:", even_numbers)