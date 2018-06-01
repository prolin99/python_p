#費式數列(Fibonacci)
#
#規則：第一項為1，第二項為1，往後每一項數字為前二項數字和。
#【最後目標】求出費式數列中，小於4百萬的所有數字中，該項是偶數的所有數字和。
a1=1
a2=1

number=0
fs_sum =0
while number < 4000000 :
    number=a1+a2

    if (number%2 ==0 ):
        print (number)
        fs_sum = fs_sum + number

    a1=a2
    a2= number

print('sum:  ' , fs_sum)
