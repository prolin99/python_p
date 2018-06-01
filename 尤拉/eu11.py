#在上面20*20方陣中，包含橫列、縱列、對角線左斜列、右斜列，四個方向，任何連續四個數字相乘，例如紅字的四個數相乘26 × 63 × 78 × 14 結果是1788696。
#【最後目標】
#尋找這樣的連續四個數，求相乘最大的結果。
numbers=[]
file= open('./eu11-numbers.txt','r')
for line in file.readlines():
    line = line.strip()
    number_list=[]
    for number in line.split():
        number_list.append(int(number))
    numbers.append(number_list)

#print(numbers)

max=0
maxlist=''

for row in range(20):
    for col in range(17):
        #後四個數
        product = numbers[row][col]*numbers[row][col+1]*numbers[row][col+2]*numbers[row][col+3]
        if max < product :
            max=product
            maxlist= str(numbers[row][col])  +' ,' + str(numbers[row][col+1]) +' ,' + str(numbers[row][col+2]) +' ,' + str(numbers[row][col+3])
        if (row<20-3):
            #斜後
            product = numbers[row][col]*numbers[row+1][col+1]*numbers[row+2][col+2]*numbers[row+3][col+3]
            if max < product :
                max=product
                maxlist= str(numbers[row][col])  +' ,' + str(numbers[row+1][col+1]) +' ,' + str(numbers[row+2][col+2]) +' ,' + str(numbers[row+3][col+3])
        if (row<20-3)and (col>=3):
            #斜前
            product = numbers[row][col]*numbers[row+1][col-1]*numbers[row+2][col-2]*numbers[row+3][col-3]
            if max < product :
                max=product
                maxlist= str(numbers[row][col])  +' ,' + str(numbers[row+1][col-1]) +' ,' + str(numbers[row+2][col-2]) +' ,' + str(numbers[row+3][col-3])




print(max , maxlist)
