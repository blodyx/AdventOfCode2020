lines = open("input/3.input", "r").readlines()

trees=0
x=y=0
maxx=len(lines)
maxy=len(lines[0])-1
print maxx,maxy
while 1:
    if x>=maxx:
        break

    print x,y,lines[x][y]
    if lines[x][y] == '#':
        trees+=1
    x+=1
    y+=3

    if y>=maxy:
        y=y-maxy

print trees



