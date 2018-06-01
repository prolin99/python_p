list1=range(0,5)
print(list1)
#放入陣列
t = [n for n in range(0,5)]
print (t)

#字串也可以視為陣列
list3='python'
for t in list3:
    print(t)

#字串分割
list3= "2016/12/31".split('/')

print(list3)

#陣列內容 反轉 [開始：結束：移動數]
print(list3[::-1])
