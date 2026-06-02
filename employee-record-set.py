sa=[1,2,3,4,5]
sb=[3,4,8,6,7]
a=set(sa)
b=set(sb)
commen=a & b
a_only=a-b

print(f"both workshops: {commen}\na workshop only: {a_only}")