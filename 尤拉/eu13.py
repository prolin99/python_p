#長整數相加
#【最後目標】
#有100個長整數，每一個數字都長達50位數，請求出這100個數字總和的前十位數字。
sum =0
file = open('./eu13-number.txt','r')
for line in file.readlines():
    line=line.strip()
    sum = sum + int(line)

file.close()

print(str(sum)[0:10])
