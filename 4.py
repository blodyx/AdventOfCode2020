import re
lines = open("input/4.input", "r").readlines()
words=["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
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
    words=["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    ok=0
    for w in words:
        for o in passport:
            if o == "":
                continue
            if o[0]+o[1]+o[2] == w:
                ok+=1
    if ok==7:
        return 1
    else:       
        return 0

valid=0
for p in passports: 
    valid+= validate(p)

print valid

