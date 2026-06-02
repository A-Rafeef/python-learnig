def tryy():
    try:
        age=int(input("enter you age: "))
    except:
        print("you enter invalied input\ntry again")
        tryy()
    else:
        print(f"Your age is {age}")

tryy()