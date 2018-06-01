#在這個50行*20列=1000個數字串中，將所有相鄰的4個數字相乘所得的乘積中，最大的一組是 9×9×8×9=5832
#【最後目標】
#在這個50行*20列=1000個數字串中，將所有相鄰的13個數字相乘所得的乘積中，請求出最大的乘積。

numbers=[]
file= open("eu08-number.txt","r")
for line in file.readlines():
    line = line.strip()  #移除頭尾特定字符如空白
    for chr in line:
        numbers.append(int(chr))
file.close()

print(numbers)


post=0
max=1
max_list=[]
max_post=0

for n in numbers:
    if (post<= (len(numbers)-4) ) :
        product=1
        for i in range(4):
            product = product * numbers[i+post]


        if max < product :
            max = product
            max_post= post
        post=post+1

print(max )
for i in range(4):
    print(numbers[i+max_post])


    #max=
