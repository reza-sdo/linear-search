test = input("enter value and splice with space: ").split()
dic={}
a = 0
b=0

for i in test:

    if i not in list(dic.keys()):
        dic[i] = 1
    else:
        dic[i] += 1

for i in range(len(list(dic.values()))):
    if list(dic.values())[i] >= a :
        a = list(dic.values())[i]
        b=list(dic.keys())[i]
    
print(f"{b} repeats {a} times")


