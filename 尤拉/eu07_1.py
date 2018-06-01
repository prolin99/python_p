#質數
#質數（Prime number），指在大於1的自然數中，除了1和該數自身外，無法被其他自然數整除的數。
#驗證一個數字n是否為質數的一種簡單但緩慢的方法為試除法。此一方法會測試n是否為任一在2與之間的整數之倍數。
#【最後目標】
#找出第10001個質數。

#計時開頭
import time
tStart = time.time()#計時開始

primes = [2]
n = 3
ni = 2
while ni <= 10001 :
        max = n ** 0.5
        for i in primes:            #求質數只以質數做除數，比較有效率
                if n % i == 0:
                        break
                if i > max:
                        primes.append(n)
                        print(ni, n)
                        ni = ni + 1
                        break
        n = n + 2

#print(primes)


#計時結尾
tEnd = time.time()#計時結束
#列印結果
print ("It cost %f sec" % (tEnd - tStart) ) #會自動做近位
print (tEnd - tStart)#原型長這樣
