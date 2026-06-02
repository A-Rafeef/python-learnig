# Given:
# text = "Python is easy and python is powerful" 
# Task :
# Print the most frequent word 

text = "Python is easy and python is powerful" 
text2=text.lower().split()
count={}
for ch in text2:
    if ch in count:
        count[ch]+=1
    else :
        count[ch]=1
count0=max(count.values())

for key,value in count.items():
    if count0 ==count.get(key):
        print(key,value)

