def add(n1,n2):
    return n1+n2
    
def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2
    
def divide(n1,n2):
    return n1/n2
    
operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
first_number=float(input("What is the first number: "))
should_continue=True
while should_continue:
    for symbol in operations:
        print(symbol)
    operation_symbol=input("pick an opration: ")
    second_number=float(input("What is the next number: "))
    calculation_function=operations[operation_symbol]
    answer=calculation_function(first_number,second_number)
    print(f"{first_number} {operation_symbol} {second_number}={answer}")
    
    choice=input(
        f"Type y to continue calculation with {answer},"
        "'n' for a new calculation, or 'exit' to stop:").lower()
        
    if choice=="y":
        first_number=answer
    elif choice=="n":
        first_number=float(input("What is the first number?"))
    else:
        should_continue=False