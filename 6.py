lines = open("input/6.input", "r").readlines()
questions=[]
group =''
for l in lines:
    for i in l:
        if i == '\n' and last == '\n':
            for g in group:
                if -1==questions[i].find(g):
                    print g
                else:
                    questions[i]=''
                    break
            questions.append(group)
            group=''
        last = i
        if i ==' ':
            break
        if -1 == group.find(i) and i != '\n':
            print i
            group=group+i
questions.append(group)
print questions
ans=0
for q in questions:
    ans += len(q)
print ans
