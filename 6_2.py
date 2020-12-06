with open("input/6.input", "r") as f:
    groups = f.read().split('\n\n')
ans=0
allones=[]
for g in groups:
    g=g.split()
    group=set(g[0])

    for i in g:
        group=group.intersection(set(i))
    allones.append(group)   

for a in allones:
   ans+= len(a)
print ans
