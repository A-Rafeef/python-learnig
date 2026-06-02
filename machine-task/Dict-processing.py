# Given:
# data = {"A": 45, "B": 78, "C": 88, "D": 62}
# Task :  
# Print all keys with values greater than 60 

data = {"A": 45, "B": 78, "C": 88, "D": 62} 
for key, value in data.items():
    if value >60:
        print( key, value)