def large(*args):
    l=args[0]
    for i in args:
        if i>l:
            l=i
    return l
print(large(20,4,5,6,7,33))