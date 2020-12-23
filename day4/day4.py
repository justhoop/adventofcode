import re

def parttwo(passport):
    bad = 0
    failed = ""
    if not int(passport["byr"]) >= 1920 and int(passport["byr"]) <= 2002: #byr (Birth Year) - four digits; at least 1920 and at most 2002.
        failed = failed + "byr "
        bad += 1
    if not int(passport["iyr"]) >= 2010 and int(passport["iyr"]) <= 2020: #iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        failed = failed + "iry "
        bad += 1
    if not int(passport["eyr"]) >= 2020 and int(passport["eyr"]) <= 2030: #eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        failed = failed + "eyr "
        bad += 1
    if not height(passport["hgt"]): #hgt (Height) - a number followed by either cm or in:
        failed = failed + "hgt "
        bad += 1
    if not hair(passport["hcl"]):
        failed = failed + "hcl "
        bad += 1
    if not passport["ecl"] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']: #ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        failed = failed + "ecl "
        bad += 1
    if not len(passport["pid"]) == 9: #pid (Passport ID) - a nine-digit number, including leading zeroes.
        failed = failed + "pid "
        bad += 1
    
    if bad > 0:
        return False
    else:
        return True

def hair(color):
    pattern = re.compile(r'^(#)([a-fA-F0-9]){6}')
    if pattern.fullmatch(color):
        return True
    else:
        return False

def height(height):
    if 'in' in height:
        height = height.removesuffix('in')
        if int(height) >= 59 and int(height) <= 76: #If in, the number must be at least 59 and at most 76.
            return True
        else:
            return False
    elif 'cm' in height:
        height = height.removesuffix('cm')
        if int(height) >= 150 and int(height) <= 193: #If cm, the number must be at least 150 and at most 193.
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
    passports.append(passport)
    print('end')

print(firstanswer(passports))
