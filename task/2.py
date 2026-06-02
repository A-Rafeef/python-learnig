text = "  Python is Powerful and python is easy to Learn  " 
text2remove=text.strip()
text2lower=text2remove.lower()
text2split=text2lower.split()

print(f"{text2remove}\n{text2lower}\n{text2split}")
count={}

for ch in text2split:
    if ch in count:
        count[ch]+=1
    else:
        count[ch]=1
        
print(count)
county=list(count)
print(county)