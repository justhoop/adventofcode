def first(numbers):
    output = []
    for number in numbers:
        if 2020 - number in numbers:
            output.append(number)
    return output[0] * output[1]

def second(numbers):
    for number1 in numbers:
        for number2 in numbers:
            for number3 in numbers:
                if (number1 + number2 + number3 == 2020):
                    return number1 * number2 * number3

f = open('day1.txt','r')
numbers = [int(line.strip()) for line in f]
f.close()

print(first(numbers))
print(second(numbers))