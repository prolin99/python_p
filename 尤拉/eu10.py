#質數和
#小於10的質數有2,3,5,7，把這些質數相加2+3+5+7=17，得到總和17
#最後目標】
#請將小於二百萬的所有質數相加，求總和。

prime=[2]
n=3
while (n<2000000):
    for i in prime:
        max = n ** 0.5
        if (n % i ==0) :
            break
        if (i >max):
            prime.append(n)
            break
    n = n+2

#print(prime)

sum = 0
for i in prime:
    sum = sum + i

print(sum)
