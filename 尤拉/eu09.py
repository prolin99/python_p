#畢氏三元數
#若直角三角形的兩股長為a,b，斜邊長為c，則。這個定理是畢達哥拉斯發現的，因此把它叫做畢氏定理。
#而滿足的一組正整數解a,b,c則稱為一組畢氏三元數(Pythagorean triples)。
#例如：(3,4,5)就是一組畢氏三元數。
#【最後目標】
#找出一組畢氏三元數，其中 a+b+c = 1000，求a,b,c三數的乘積
find=False

for a in range(1,1000):
    for b in range(1,1000):
        c= (a**2 + b**2)**0.5

        #if c==int(c) :
        if (a+b+c>1000):
            break

        if (a+b+c==1000) :
            print (a,b,c)
            find = True
            break
    if find:
        break
