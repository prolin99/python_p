#階乘數字和
#一個正整數的階乘（英語：factorial）是所有小於及等於該數的正整數的乘積，並且有0的階乘為1。自然數n的階乘寫作n!。
#5! = 5*4*3*2*1 = 120
#將5!展開後的數字和為1+2+0=3
#【最後目標】
#求 100! 展開後的數字和
import math


def T(n):
    product=1
    for i in range(1,n+1):
        product = product * i
    return product

#mystr= str(math.factorial(100))
mystr= str(T(100))
sum =0
for n in mystr:
    sum = sum + int(n)

print(sum)
