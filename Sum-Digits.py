def sumDigits(x):
    global i
    sum = 0
    y = str(x)
    for i in range(0, len(y)):
        sum += int(y[i])
    return sum

x = int(input("number:\n"))

print(sumDigits(x))
