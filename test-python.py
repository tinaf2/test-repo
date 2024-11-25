def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

def add(a, b):
    return a + b

result = add(2, 3)
print(result)

class Calculator:
    def __init__(self, value=0):
        self.value = value
    
    def add(self, amount):
        self.value += amount
        return self.value

calc = Calculator()
print(calc.add(5))

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function(10)

print(outer_function(5))


def invalid_function
    print("This will cause a syntax error")

def unclosed_string():
    print("This string is not closed)

def incorrect_indentation():
print("This will cause an indentation error")

def add_numbers(a, b):
    return a + b

print(add_numbers("hello", 2))  

def mismatched_parentheses():
    print("This is a syntax error"  

undefined_function_call()  
