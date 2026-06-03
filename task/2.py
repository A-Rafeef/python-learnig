text = "  Python is Powerful and python is easy to Learn  " 
text2remove=text.strip()
text2lower=text2remove.lower()
text2split=text2lower.split()

print(f"{text2remove}\n\n{text2lower}\n\n{text2split}\n\n")
count={}

for ch in text2split:
    if ch in count:
        count[ch]+=1
    else:
        count[ch]=1
        
print(count,"\n\n")
county=list(count)
county2=" ".join(county)
print(county2)