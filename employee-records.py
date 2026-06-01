a=[1,2,3,4,5]
b=[3,4,8,6,7]
commen=[]
a_only=[]
for i in a:
    if i in b:
        commen.append(i)
    else :
        a_only.append(i)
print(f"both workshops: {commen}\na workshop only: {a_only}")