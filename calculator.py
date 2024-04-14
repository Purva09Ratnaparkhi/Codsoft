def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def multi(num1,num2):
    return num1 * num2

def div(num1,num2):
    return num1 / num2

while True:
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nChoose an operation:")
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
    operation = int(input("Enter your choice: "))

    if operation == 1:
        result = add(num1,num2)
    elif operation == 2:
        result = sub(num1,num2)
    elif operation == 3:
        result = multi(num1,num2)
    elif operation == 4:
        result = div(num1,num2)
    else:
        print("Invalid Operation Selected.")
        
    print("Result: ", result)
     
    choice = input("\nDo you want to continue? (y/n): ")
    if choice != 'y':
         break
