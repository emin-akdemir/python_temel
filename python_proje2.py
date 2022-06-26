l= [[1, 2], [3, 4], [5, 6, 7]]

x = l [::-1]
z=0
for i in x:
    if type(i) == list:
        y= i[::-1]
        x[z]=[y]
    z+=1
print(x)
