#最小公倍數

#能夠被某些數字都除盡的最小正整數稱為是這些數字的最小公倍數

#【最後目標】

#請找出數字1-20都能除盡的最小正整數
def find(value):
    for i in range(10,1,-1):
        if (value % i >0 ):
            return False
    return True

#最大公因數
def GCD(a,b):
    if b<a:
        m=b;
        b=a;
        a=m;
    m=a%b
    while (m >0) :
        a=b
        b= m
        m=a%b
    return b



#最小公倍數
def LCM(a,b):
    return a*b //GCD(a,b)

t=1
for i in range(2,21):
    tv= LCM(t,i)

    print(t,i , tv)
    t= tv
