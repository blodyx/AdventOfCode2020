import re
with open("input/7.test", "r") as f:
    data = f.readlines()
allrules=[]
for line in data:
    temp = re.split(r' contain|,|\.\n',line)
    allrules.append(temp)
#print rules
run=0
def can_contain(color,rules):
    count=0
    for rule in rules:
        found=0
        for r in rule[1:]:
            if r.find(color) !=-1:
                print r,color
                found=1
        if not found:
            print r,r[3:13]
            [x for x in allrules if (x[0].find(str(r[3:13])) != -1)]
            print x
                #can_contain(color, [x for x in allrules if (x[0].find(str(r[3:13])) != -1)])



print can_contain('gold',allrules)
