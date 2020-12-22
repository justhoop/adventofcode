def firstanswer(field):
    index = 0
    answer = 0
    for line in field:
        index = index % 31
        if line[index] == "#":
            answer += 1
        # print(f'{line} index {index} char {line[index]} answer {answer}')
        index += 3
    return answer

def secondanswer(field, right, down):
    index = 0
    answer = 0
    for i in range(0, len(field), down):
        index = index % 31
        line = field[i]
        if line[index] == "#":
            answer += 1
        index += right
    return answer

f = open('day3.txt', 'r')
field = [line.strip() for line in f]
f.close()

# print(firstanswer(field))
print(secondanswer(field, 1, 1) * secondanswer(field, 3, 1) * secondanswer(field, 5, 1) * secondanswer(field, 7, 1) * secondanswer(field, 1, 2))
