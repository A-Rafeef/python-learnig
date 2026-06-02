numbers = [12, 5, 18, 7, 25, 10, 18] 
num=numbers[0]
num2=numbers[1]

for i in numbers:

    if i>num:
        num2=num
        num=i
    elif num>i>num2 :
        num2=i
print(num2)

