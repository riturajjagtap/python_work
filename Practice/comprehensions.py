
li=[i for i in range(0,101,5)]
print(li)
li2=[i**2 for i in range(0,31,3) if i%2==0]
print(li2)


print([i**2 for i in range(0,31,3) if i%9==0])
a=[1,2]
b=[5,6,7]
print([(x,y) for x in a for y in b])