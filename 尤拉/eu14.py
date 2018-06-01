#考拉茲猜想
#任意數使用以下公式可以導出一系列數字，而此數列最終會結束於1(目前尚未被證明)
#n →  n/2 (如果n 是偶數 ,下一個數列為 n/2 )
#n → 3n + 1 (n是奇數 ，下個數列為 3n+1  )
#例如 n=13，可以導出以下10個數字，我們可以稱13這個數字的考拉茲生命週期是10。
#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#【最後目標】
#在小於一百萬的數字中，哪一個數字的考拉茲生命週期最長？

def collatz(n):
    global numbers
    global mylen
    numbers.append(n)
    mylen=mylen+1
    #print(n)
    if n ==1 :
        return 1
    elif (n %2 ==0):
        collatz(n//2)
    else:
        collatz(n*3+1)

numbers=[]
mylen=0
max =0
max_i=0
for i in range(1,100):
    numbers=[]
    mylen=0
    collatz(i)
    print(i, mylen)

    #if max < len(numbers):
    if mylen>max :
        #max = len(numbers)
        max=mylen
        max_i = i

print(max_i , max)
