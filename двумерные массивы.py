#задание 1 
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for i in matrix:
    for element in i:
        print(element, end=' ')
    print()
for i in matrix:
    for element in i:
        if element % 2 != 0:
            print(element, end=' ')
a=0
for i in matrix:
    for element in i:
        if element % 2== 0:
            a+=1
print(a)
