lines = open("input/3.input", "r").readlines()

product=1
maxx=len(lines)
maxy=len(lines[0])-1
test=[[1,1],[1,3],[1,5],[1,7],[2,1]]

for cx,cy in test:
    tree=x=y=0
    while x<maxx:

        if lines[x][y] == '#':
            tree+=1
        x+=cx
        y+=cy

        if y>=maxy:
            y=y-maxy

    product *= tree
print product
