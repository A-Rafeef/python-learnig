students = { 
    "Asha": [78, 82, 69],
    "Rahul": [35, 60, 38],
    "Meena": [90, 92, 88],
    "Kiran": [25, 30, 28]
      } 
st={"fail": 0,
    "pass": 0}
fail=[]
top=0
for key, value in students.items():
    sum=0
    avg=0
    for i in value:
        sum+=i
    avg=sum/3
    if top<avg:
        top=avg
        topper=key
    if avg>=75:
        result,a="Distinction",2
        st["pass"]+=1
    elif 75>avg>50:
        result,a="Pass",1
        st["pass"]+=1
    elif avg<50:
        result,a= "Fail",0
        fail.append(key)
        st["fail"]+=1
        
    print(key,avg,result)

print("failed Students",fail)
print("the topper is ",topper, "mark", top)
print(st)
