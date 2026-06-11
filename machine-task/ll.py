list1=[]
list2=[]
while True :
    try :
        num=int(input("Enter number"))
        list1.append(num)
        if num%2==0:
            list2.append(num)
        if len(list1)==5:
            break
    except: 
        print("invalid input entered")
print(list2)