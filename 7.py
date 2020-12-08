import re
with open("input/7.test", "r") as f:
    data = f.readlines()
rules=[]
for line in data:
    temp = re.split(r' contain|,|\.\n',line)
    rules.append(temp)
print rules
run=0
def can_contain(color,rules):
    count=0
    for r in rules:
        for i in range(len(r)-1):
            if -1 != r[i+1].find(color):
                count+= int(r[i+1][1])
            if -1==r[i+1].find('no other bag'):
                print r[i+1]
                count+=can_contain(r[i+1][3:11],rules)
    return count

print can_contain('gold',rules)
