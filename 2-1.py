list1=['aaa','bbb','ccc']
s=','.join(list1)
print(s)
t=1,2,3
t=(1,2,3)
print(t)
print(t[2])
a,b,c=t
print(a,b,c)
a,b=b,a
print(a,b,c)
t2=t,4,5
print(t2)
print(t2[0])
t3=('x')
t4=('x',)

print('t3 type',type(t3))
print('t4 type',type(t4))
