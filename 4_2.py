import re
lines = open("input/4.input", "r").readlines()
passports=[]
passport=[]
for l in lines:
    
    temp = re.split("\s",l)
    if temp == ['', '']:
        passports.append(passport)
        passport=[]
    else:
        passport = passport+temp
passports.append(passport)
ok=0

def validate(passport):
    byr = iyr = eyr = hgt = hcl = ecl = pid = 0
    for p in passport:
        if p == '':
            continue
        else:
            string = ''
            string=string.join(p)
            test ,rest = string.split(':')
        if "byr" == test:
            if 1920 <= int(rest) <= 2002:
                byr = 1

        if "iyr" == test:
            if 2010 <= int(rest) <= 2020:
                iyr = 1

        if "eyr" == test:
            if 2020 <= int(rest) <= 2030:
                eyr = 1

        if "hgt" == test:
            if rest.endswith('cm'):
                if 150 <= int(rest[:-2]) <=193:
                   hgt = 1
            if rest.endswith('in'):
                if 59 <= int(rest[:-2]) <=76:
                   hgt = 1

        if "hcl" == test:
            pattern = re.compile("#[0-9a-f]{6}")
            if pattern.match(rest):
                hcl = 1

        if "ecl" == test:
            hair=["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if rest in hair:
                ecl = 1

        if "pid" == test:
            if len(rest)==9 and int(rest):
                print rest
                pid = 1

    return byr * iyr * eyr * hgt * hcl * ecl * pid

valid=0
for p in passports: 
    valid+= validate(p)

print valid

