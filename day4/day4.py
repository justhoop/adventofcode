def parttwo(passport):
    good = 0
    failed = ""
    if not daterange(passport["byr"], 1920, 2002): #byr (Birth Year) - four digits; at least 1920 and at most 2002.
        failed = failed + "byr "
        good += 1
    if not daterange(passport["iyr"], 2010, 2020): #iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        failed = failed + "iry "
        good += 1
    if not daterange(passport["eyr"], 2020, 2030): #eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        failed = failed + "eyr "
        good += 1
    if not height(passport["hgt"]): #hgt (Height) - a number followed by either cm or in:
        failed = failed + "hgt "
        good += 1
    if not hair(passport["hcl"]):
        failed = failed + "hcl "
        good += 1
    if not passport["ecl"] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']: #ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        failed = failed + "ecl "
        good += 1
    if not len(passport["pid"]) == 9: #pid (Passport ID) - a nine-digit number, including leading zeroes.
        failed = failed + "pid "
        good += 1
    
    if good > 0:
        return False
    else:
        return True

def hair(color):
    if '#' in color[0]: #hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        color = color.removeprefix('#')
        if len(color) == 6:
            let = ['a', 'b', 'c', 'd', 'e', 'f']
            num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            for char in color:
                if not char in let and not char in num:
                    return False
            return True
        else:
            return False
    else:
        return False

def height(height):
    if 'in' in height:
        height = height.removesuffix('in')
        if int(height) > 58 and int(height) < 77: #If in, the number must be at least 59 and at most 76.
            return True
        else:
            return False
    if 'cm' in height:
        height = height.removesuffix('cm')
        if int(height) > 149 and int(height) < 194: #If cm, the number must be at least 150 and at most 193.
            return True
        else:
            return False

def daterange(year, low, high):
    if int(year) >= low and int(year) <= high:
        return True
    else:
        return False

def firstanswer(passports):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    good = 0
    for passport in passports:
        if len(passport) > 1:
            temp = []
            for entry in passport:
                temp += entry
        passport = temp
        count = 0
        newpassport = {}
        for entry in passport:
            entry = entry.split(':')
            newpassport[entry[0]] = entry[1]
        for field in fields:
            if  field in newpassport:
                count += 1
        if count >= 7:
            if parttwo(newpassport):
                good += 1
        # if not count >= 7:
        #     print(f'{count} {newpassport}')
    return good

passports = []
passport = []
with open("day4/day4.txt", "r") as f:
    for line in f:
        if line != '\n':
            entry = line.replace('\n', '').split(" ")
            clean = [x.replace(':', '=') for x in entry]
            passport.append(entry)
        else:
            passports.append(passport)
            passport = []
    print('end')

print(firstanswer(passports))
