#回文數(palindromic number)

#回文數(或迴文數)是指一個像14641這樣「對稱」的數，即：將這個數的數字按相反的順序重新排列後，所得到的數和原來的數一樣。

#【最後目標】

#在二個二位數字乘積的數字中，最大的回文數是9009=91*99

#請找出二個三位數字乘積數字中，最大的回文數。

def is_turn(v):
    #print(v)
    reverse=0
    set_v = v
    while (v>0 ):
        reverse = reverse*10 +  (v%10)
        v = v // 10
    #print (set_v, reverse)

    if reverse == set_v :
        return True
    else :
        return False

x=1000
y=1000
no_exit = True
re_array=[]
while (x>100) and no_exit  :
    y=1000
    x=x-1
    while(y>100) and no_exit :
        y=y-1
        if is_turn(x*y):
            print (x,y , x*y)
            re_array.append(x*y)
            #no_exit = False


#排序，倒序            
re_array.sort(reverse=True)
print('最大回文數：' , re_array[0])
