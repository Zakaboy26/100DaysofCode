import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculator_dictionary = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def clear_screen():
    print("\n" * 100)

def calculator():
    print(art.logo)
    first_number = float(input("What's the first number?: "))
    should_continue = True

    while should_continue:
        operation_pick = input("+\n-\n*\n/\nPick an operation: ")
        next_number = float(input("What's the next number?: "))
        answer = calculator_dictionary[operation_pick](first_number, next_number)
        print(f"{first_number} {operation_pick} {next_number} = {answer}")

        continue_answer = input(f"Type 'Y' to continue calculating with {answer} or type 'N' to start a new calculator").upper()
        if continue_answer == "Y":
            clear_screen()
            first_number = answer
        elif continue_answer == "N":
            should_continue = False
            calculator()
        else:
            print("Invalid input")
            should_continue = False

calculator()












