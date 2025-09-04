


# Question 1

# operations
def add(a, b):
    result = a + b
    print(result)
    return result

def subtract(a, b):
    result = a - b

    return result

def multiply(a, b):
    result = a * b
    return result

def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Cannot Divide by zero")


while True:
    print("-------------------------")
    print("Calculator App: ")
    print("-------------------------")


    num1 = float(input("input first number: "))
    num2 = float(input("input second number: "))
    choice = input("Choose operation (+, -, *, /) or 'exit' to quit: ")

    if choice == '+':
   

        add(num1, num2)

    elif choice == '-':
        

        subtract(num1, num2)

    elif choice == '*':
        

        multiply(num1, num2)
    
    elif choice == '/':
        

        divide(num1, num2)
    elif choice == 'exit':
        print("Calculator Closing..")
        print("Exiting calculator, goodbye.")
        break









# Question 2

print("-------------------------")
print("Question 2 ")
print("-------------------------")


while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    if user_input == "exit":
        print("Goodbye!")
        break      # break out of loop
    
    num = int(user_input)   # convert to integer
    
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")












# Question 3

print("-------------------------")
print("Question 3 ")
print("-------------------------")

while True:
    age = input("Enter your age (or type exit to quit): ")
    if age == "exit":
        print("Goodbye!")
        break
    
    try:
        if int(age) >= 18:
            print("You can vote")
        else:
            print("You cannot vote")
    except ValueError:
        print("Invalid input")




