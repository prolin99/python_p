#質因數
#120的所有因數有1,2,3,4,5,6,8,10,12,15,20,24,30,40,60, 120
#這些因數中，有2,3,5三個數是質數，因此又稱為120的質因數，
#而120可以因數分解成這三個質因數的乘積。
#我們可以進一步再推出120最大的質因數是5。
#最後目標】求600851475143的最大質因數是多少？

def is_prime(value):
    maxi = int(value**0.5)
    for i in range(2,maxi):
        if (value % i == 0 ):
            #print(value, '---',i)
            return False
    return True

set_value = 600851475143
maxi= int(set_value ** 0.5)
max = 1 ;

for i in range(1, maxi):
    if (set_value %i ==0) :
        #print(i)
        if is_prime(i):
            #print (i)
            max =  i

print(max)
