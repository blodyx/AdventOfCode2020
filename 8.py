from copy import deepcopy
lines = open("input/8.input", "r").readlines()
data=[]        
for i in lines:
    data.append(i.split())

def execute(code):
    acc=0 
    i=0
    while len(code[i])<4 :
      try:
        if code[i][0]=='nop':
            i+=1
            code[i].append(1)
        if code[i][0]=='acc':
            acc+=int(code[i][1])
            i+=1
            code[i].append(1)
        if code[i][0]=='jmp':
            i+=int(code[i][1])
            code[i].append(1)
      except:
        return acc
    return -1

#       print execute(data)
ans = 0
for i in range(len(data)):
    test=deepcopy(data)

    if data[i][0]=='jmp':
        test[i][0]='nop' 
    elif data[i][0]=='nop':
        test[i][0]='jmp'


#    print i,test
    ans = execute(test)
    if -1 != ans:
        print(ans)
        break
