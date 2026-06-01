def count_even(*args):
    total=0
    for i in range(len(args)):
        if args[i]%2==0:
            total+=1
        return total
print(count_even(1, 2, 3, 4, 5, 6))

# task 5