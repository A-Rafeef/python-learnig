def prime(num):
    num2=int(num**(1/2))
    count=0
    for i in range(2,num2+1):
        if num%i==0:
            count=1
            
            break
    return count

def number(numb):
    box=[]
    for i in range(2,numb):
        a=prime(i)
        if a==0:
            box.append(i)
    return box
print(number(100))