a = int(input())
b = int(input())
sign = str(input())
if b == 0 and sign == "/":
    print("You can't divide by zero!")
elif sign == "+":
    result = a + b
    print(result)
elif sign == "*":
    result = a * b
    print(result)
elif sign == "/":
    result = a / b
    print(result)
elif sign == "-":
    result = a - b or b - a
    print(result)
elif sign not in ("+", "*", "/", "-"):
    print("invalid operation")
