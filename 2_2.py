import re
lines = open("2.input", "r").readlines()

pattern = re.compile(r'(\d+)-(\d+) (\w): (\w*)')
valid=0
for i in lines:
    low, high, char, passw = re.match(pattern, i).groups()
    if bool(passw[int(low)-1]==char) ^ bool(passw[int(high)-1]==char):
        valid+=1

print valid




