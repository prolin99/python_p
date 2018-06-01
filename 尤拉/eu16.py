#2^10 = 1024，將這個展開後的數字拆開相加，1+0+2+4=7，可以得到數字和7

#【最後目標】

#將 2^1000 展開後的數字拆開相加，求數字和。

pow = 2**10000
numbers=str(pow).strip()
sum=0
for i in numbers:
    print(i)
    sum = sum + int(i)

print(sum)
