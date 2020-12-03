lines = open("input/3.input", "r").readlines()

trees=[]
maxx=len(lines)
maxy=len(lines[0])-1
print maxx,maxy
test=[[1,1],[1,3],[1,5],[1,7],[2,1]]
for t in test:
    cx,cy =t
    tree=x=y=0
    while 1:
        if x>=maxx:
            break

        print x,y,lines[x][y]
        if lines[x][y] == '#':
            tree+=1
        x+=cx
        y+=cy

        if y>=maxy:
            y=y-maxy

    print tree
    trees.append(tree)

print trees
ans=1
for t in trees:
    ans=ans*t

print ans


