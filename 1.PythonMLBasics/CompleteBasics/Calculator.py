def calc(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if num2 == 0:
            raise Exception("Can't divide by 0!")
        else:
            return num1/num2
    elif op == "^":
        return pow(num1, num2)
    else:
        raise Exception("Invalid operator!")

print(calc(float(input("Enter first num: ")), float(input("Enter second num: ")), input("Enter operator: ")))