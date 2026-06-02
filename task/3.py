expenses = [250, 400, 120, 900, 50, 300]
total=0
while True:
    try :
        new=int(input("Enter expence"))
        expenses.append(new)
        break
    except:
        print("invalid input")

for i in expenses:
    total+=i
moreAvg=[]
avg=total/len(expenses)
for j in expenses:
    if j>avg:
        moreAvg.append(j)
print("total",total)
print("lowest expence",min(expenses))
print("Hightest expence",max(expenses))
print("Avarage",avg)
print("all expenses above average", moreAvg)
