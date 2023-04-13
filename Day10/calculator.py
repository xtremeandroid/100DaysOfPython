from art import logo

def add(n1,n2):
    return n1+n2
def substract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}
def calculator():
    print(logo)
    num1 = float(input("Enter your first number : "))
    for key in operations:
        print(key)
    shouldContinue = True
    while shouldContinue:
        operation_symbol = input("Pick an operation : ")
        num2 = float(input("What's the next number?: "))
        answer = operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"to continue calculations with {answer} type 'y' to start new calculation type 'n': ") == "y":
            num1 = answer
        else:
            shouldContinue=False
            calculator()

calculator()