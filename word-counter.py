text = "cat dog cat bird cat dog"
text2=text.split()
text3={}
for i in text2:
    if i in text3:
        text3[i]+=1
    else :
        text3[i]=1
print(text3)
maax=max(text3, key=text3.get)
print(maax)