#! /usr/bin/env python3

def add(n1,n2):
    return n1 + n2

def substract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2
    
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/":divide,
}

def calculator():
    continuous_calculation = True
    memory = 0
    while continuous_calculation == True:
        for key in operations:
            print(key)

        operations_symbol = input(f"Pick an operation from the line above: ")

        if memory == 0:
            num1 = float(input(f"Enter number 1: "))
            num2 = float(input(f"Enter number 2: "))
        else:
            num1 = memory
            print(f"Previous answer: {memory}")
            num2 = float(input(f"Enter a number: "))
            
        calculation_function = operations[operations_symbol]
        answer = calculation_function(num1,num2)

        print(
            f"{num1} {operations_symbol} {num2} = {answer}"
        )

        while True:
            continue_question = input(f"Continue on with this calculation? (y/n) ")
            if continue_question == "y":
                continuous_calculation = True
                memory = answer
                break
            elif continue_question == 'n':
                continuous_calculation = False
                memory = 0
                break
            else:
                print(f"Enter y or n to proceed...s")

calculator()