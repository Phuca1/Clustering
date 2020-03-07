import numpy as np

file = open('WSCD.csv')
a = list(file)
arr = []
for i in range(1,len(a)):
    txt = a[i]
    txt.strip()
    point = txt.split(',')
    x =[]
    for item in point:
        x.append(int(item))
    arr.append(x)

print(arr)