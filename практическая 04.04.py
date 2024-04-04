#задача 35
import random
def creatArray():
    print('Input first index matrix: ')
    x = int(input())
    print('Input second index matrix: ')
    y = int(input())
    array = []
    for i in range(x):
        array.append([])
        for j in range(y):
            array[i].append(random.randint(-100,100))
    return array
a=int(0)
m=[]
matrix=creatArray()
print(matrix)
for i in matrix: 
    for t in i:
        if t>0:
            a+=t
    print(a)
    m.append(a)
    a=0
print(m)
        
      
#задача 36
#задача 37
#задача 38
#задача 39
#задача 40
