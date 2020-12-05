import re
lines = open("input/5.input", "r").readlines()
seatid=[]
for l in lines:
    rowlo=0 
    rowhi=127
    collo=0
    colhi=7
    for i in l:
        if i == 'B':
            rowlo=(rowlo+rowhi)/2+1
        if i == 'F':
            rowhi=(rowlo+rowhi)/2
        if i == 'R':
            collo=(collo+colhi)/2+1
        if i == 'L':
            colhi=(collo+colhi)/2

    seatid.append(rowlo*8+collo)
seatid.sort()
print seatid[len(seatid)-1]

j=0
for i in seatid:
   if j+1<i and j!=0:
       print j
   j=i
