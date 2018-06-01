#【最後目標】請求出小於1000的數字中，所有3和5的倍數和。

sum =0
for i in range(1,1000):
    if (i%3==0)or (i%5==0):
        #print (i)
        sum = sum + i

print('sum:' + str(sum))
