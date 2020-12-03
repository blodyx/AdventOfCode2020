lines = open("input/3.input", "r").readlines()

tests=[]
maxx=len(lines)
maxy=len(lines[0])-1

for cx in range(10,19):
  for cy in range(10,19):
    tree=x=y=0
    while x<maxx:
        if lines[x][y] == '#':
            tree+=1
        x+=cx
        y+=cy

        if y>=maxy:
            y=y-maxy
    tests.append([cx,cy,tree])
print tests
