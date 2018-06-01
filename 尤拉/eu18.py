#最大路徑和

#一個給定的4層數字三角形（第n層有n個數），從最頂數位出發每次只能移動到左下或右下的直到最底層。在所有的路徑中，經過路徑數字和最大值是3+7+4+9=23。
#   3
#  7 4
# 2 4 6
#8 5 9 3
#【最後目標】
#一個給定的15層數字三角形（第n層有n個數），從最頂數位出發每次只能移動到左下或右下的直到最底層。請找出最大的經過路徑數字和。
import itertools

numbers=[]
file = open('eu18-number.txt','r')
for line in  file.readlines():
    line= line.strip()
    number_list=[]
    for num in line.split():
        number_list.append(int(num))
    numbers.append(number_list)
file.close()

# ----------------- 這一部份自已做 2 的 14 次方 路徑
mr=[]
def myrouter(nowrouter,maxlevel):
    global mr
    if len(nowrouter)<maxlevel:
        myrouter(nowrouter+'0',maxlevel)
        myrouter(nowrouter+'1',maxlevel)
    else:
        mr.append(nowrouter)
        return(nowrouter)


myrouter('',14)
print(len(mr))
# --------------------------------------------------------

#2 的 14 次方
x=[0,1]
routers=[]
for p in itertools.product(x, repeat=14):
    routers.append(p)
#print(len(routers))
#router='01100110101011'
max=0

for router in routers:
    i=0
    j=0
    nowline='75'
    sum=75

    for digit in router:
        i = i+1
        if digit == 0 :
            sum =sum + numbers[i][j]
        else:
            j=j+1
            sum = sum + numbers[i][j]
        #print(i , j ,numbers[i][j])
        nowline= nowline +','+ str(numbers[i][j])
    #print(router , sum)
    if max < sum :
        max = sum
        max_router=router
        max_router_line=nowline

print(max_router, max_router_line , max )
