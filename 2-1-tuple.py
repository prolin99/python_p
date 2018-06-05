#陣列
list1=['aaa','bbb','ccc']
list1[2]='change'
#合成一字串
s=','.join(list1)
print(s)

 
#tuple 和陣列類似，但無法再修改
t1=1,2,3
print(t1)

t2=(1,2,3)
#無法做修改  如：  t2[2]=5
print(t2)
print(t2[2])

#分別取值
x,y,z=list1
print(x,y,z)


a,b,c=t2
print(a,b,c)

#互換
x,y = y,x
print(x,y,z)

a,b=b,a
print(a,b,c)

# tuple 增加元素
t2=t1,4,5
print(t2)
print(t2[0])

t3=t1 + (4,5)
print(t3)
print(t3[0])



t3=('x')
t4=('x',)

print('t3 type',type(t3))
print('t4 type',type(t4))
