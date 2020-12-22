def firstanswer(db):
    total = 0
    for line in db:
        line = line.split(' ')
        pwlen = line[0].split('-')
        pwchar = line[1].strip(':')
        pw = line[2]
        if pw.count(pwchar) >= int(pwlen[0]) and pw.count(pwchar) <= int(pwlen[1]) and pw.count(pwchar) > 0:
            total += 1
    return total

def secondanswer(db):
    total = 0
    for line in db:
        line = line.split(' ')
        pwlen = line[0].split('-')
        pwchar = line[1].strip(':')
        pw = line[2]
        if pw[int(pwlen[0])-1] == pwchar or pw[int(pwlen[1])-1] == pwchar:
            if not (pw[int(pwlen[0])-1] == pwchar and pw[int(pwlen[1])-1] == pwchar):
                total += 1
    return total

f = open('day2.txt','r')
db = [line.strip() for line in f]
f.close()

print(firstanswer(db))
print(secondanswer(db))
