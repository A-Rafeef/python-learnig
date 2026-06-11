def option():
    
    
    print("===== Expense Tracker =====\n1. Add Expense\n2. View Expenses\n3. Show Total\n4. Exit")
    global input1
    while True:
        try:
            input1=int(input("Choose an option: "))
            if input1>0 and input1<5:

                break
            
            
            
            
        except:
            print("Invalid Output Entered, try again")



expenses=[]
def out():
    if input1==1:
        
        
        while True:
            try:
                one_title=input("Enter title: ")
                one_amount=int(input("Enter amount: "))
                dicto={"title": one_title , "amount": one_amount}
                expenses.append(dicto)
                
                
                break
            except: 
                print( " Invalied input")
    elif input1==2:
        for i in expenses:
            print(type(i))
            i=dict(i)
            a=list(i.values())
            print(f"{a[0]} - {a[1]}\n\n\n")
    elif input1==3:
        sum=0
        for i in expenses:
            i=dict(i)
            a=list(i.values())

            print(a)

        print(f"the total expence is {sum}") 
    
        
while True:
    option()
    if input1==4:
        break
    else :
        out()

