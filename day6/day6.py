from collections import Counter

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

total = 0
answers = []
group = []
with open("day6/day6.txt", "r") as f:
    for line in f:
        if line != '\n':
            entry = line.replace('\n', '')
            group.append(entry)
        else:
            answers.append(group)
            group = []
    answers.append(group)
for group in answers:
    x = ""
    members = len(group)
    for answer in group:
        x += answer
    c = Counter(x)
    for e in c.values():
        if e == members:
            total += 1
print(total)