#質數
#質數（Prime number），指在大於1的自然數中，除了1和該數自身外，無法被其他自然數整除的數。
#驗證一個數字n是否為質數的一種簡單但緩慢的方法為試除法。此一方法會測試n是否為任一在2與之間的整數之倍數。
#【最後目標】
#找出第10001個質數。
import time
tStart = time.time()#計時開始

def is_prime(n):
    i=2
    while i <= n**0.5:
        if (n % i == 0):
            return False
        i=i+1
    return True

n=1
ni=1    #已有一個 2
while ni < 10001:
    n=n+2       #由3開始 只取奇數
    if is_prime(n):
        ni = ni+1
        print(ni,n)

print(n)



tEnd = time.time()#計時結束
#列印結果
print ("It cost %f sec" % (tEnd - tStart) ) #會自動做近位
print (tEnd - tStart)#原型長這樣
