def count_even(*args):
    
    total=0
    count=0
    largest=args[0]
    smallest=args[0]
    for i in range(len(args)):
        total+=args[i]
        count+=1

        if args[i]>largest:
            largest=args[i]
        if args[i]<smallest:
            smallest=args[i]

    return total, count, largest, smallest

count,total, largest, smallest=count_even(1, 2, 3, 4, 5, 6)
print(f"count: {count} \ntotal: {total} \nlargest : {largest} \nsmallest : {smallest} ")