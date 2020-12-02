import re
f = open("2.input", "r")
lines = f.readlines()

pattern = re.compile(r'(\d+)-(\d+) (\w): (\w*)')
valid=0
for i in lines:
    low, high, char, passw = re.match(pattern, i).groups()
    count=0
    for j in passw:
        if j is char:
            count+=1
#    print char,low, high, count
    if int(low)<=count<=int(high):
        valid+=1

print valid

