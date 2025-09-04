


# Question 1
def Solution_1():

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
        result = a / b
        return result


    while True:
        print("-------------------------")
        print("Calculator App: ")
        print("-------------------------")


        print("select an operation: ")
        print("1. addition")
        print("2. subtraction")
        print("3. multiplication")
        print("4. division")
        print("5. exit ")



        choice = input("input 1/2/3/4/5: ")

        if choice == '1':
            num1 = float(input("input first number: "))
            num2 = float(input("input second number: "))

            add(num1, num2)

        elif choice == '2':
            num1 = float(input("input first number: "))
            num2 = float(input("input second number: "))

            subtract(num1, num2)

        elif choice == '3':
            num1 = float(input("input first number: "))
            num2 = float(input("input second number: "))

            multiply(num1, num2)
        
        elif choice == '4':
            num1 = float(input("input first number: "))
            num2 = float(input("input second number: "))

            divide(num1, num2)
        elif choice == '5':
            print("Calculator Closing..")
            print("Calculator Closed, bye.")
            break









# Question 2
def Solution_2():

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
def Solution_3():

    print("-------------------------")
    print("Question 3 ")
    print("-------------------------")

    while True:
        age = input("Enter your age (or type exit to quit): ")
        if age == exit:
            print("Goodbye!")
            break
        
        try:
            if int(age) >= 18:
                print("You can vote")
            else:
                print("You cannot vote")
        except ValueError:
            print("Invalid input")







print("Exam solutions - Ayyub Raji")
print("Solution 1. calculator")
print("Solution 2. Code Copletion")
print("Solution 3. Code Error fix")
print("4. close Exam assessment")



while True:
    solution = input("Pls select a Solution to review 1, 2, 3 or select 4 to complete:  ")
    if solution == '1':
        Solution_1()

    elif solution == '2':
        Solution_2()


    elif solution == '3':
        Solution_3()

    elif solution == '4':
        print("Thanks for the review.")