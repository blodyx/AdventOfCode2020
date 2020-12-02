f = open("input/1.input", "r")
listan=[]
for i in f:
    listan.append(int(i.strip()))

for x in range(0,len(listan)):
    for y in range(x+1,len(listan)):
        for z in range(y+1,len(listan)):
            if listan[x]+listan[y]+listan[z]==2020:
                print listan[x]*listan[y]*listan[z]
