def calculate(gate, first, second):
    result = None
    if gate == "or":
        result = first or second
    elif gate == "and":
        result = first and second
    elif gate == "xor":
        if (first == 0 and second == 1) or (first == 1 and second == 0):
            result = 1
        else:
            result = 0
    elif gate == "nand":
        result = not(first and second)
    elif gate == "nor":
        result = not(first or second)
    else:
        print("Invalid input")
    return result

gate = input("Enter logic gate: ")
gate = gate.lower()
first = int(input("Enter the first input: "))
second = int(input("Enter the second input: "))

result = calculate(gate, first, second)
print(f"Result = {result}")
