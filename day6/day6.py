answers = []
group = []
with open("day6/day6.txt", "r") as f:
    for line in f:
        if line != '\n':
            entry = line.replace('\n', '')
            for item in entry:
                group.append(item)
        else:
            myset = set(group)
            answers.append(myset)
            group = []
    myset = set(group)
    answers.append(myset)
total = 0
for i in answers:
    total = total + len(i)
print(total)