a = int(input('nam:'))
operation = input('/,*,-,+:')
b = int(input('nam:'))
if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '/':
    if b == 0:
        result = "hobotok"
    else:
        result = a / b
else:
    result = 'not implemented'
print(result)
