def calculator (a, b, operation):
    if operation == "add":
        return a+b
    elif operation == "sub":
        return a-b
    elif operation == "multiply":
        return a*b
    elif operation == "divide":
        return a/b
    else:
        print("operation not found")
print(calculator(22,11, "add"))
print(calculator(22,11,"sub"))
print(calculator(22,11, "multiply"))
print(calculator(22,11, "divide"))
print(calculator(22,11, "permutation"))
