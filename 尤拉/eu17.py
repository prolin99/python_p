#英文數字
#342轉成英文後是「three hundred and forty-two」這個英文字總共包含23個字母。
#115轉成英文後是「one hundred and fifteen」這個英文字總共包含20個字母。
#【最後目標】
#將1到1000的數字都寫成英文，一共有多少個字母？
def num2eng(n):
    numbers_eng={0:'' ,1:'one' ,2:'two',3:'three' , 4:'four' , 5:'five' , 6:'six' , 7:'seven' , 8:'eight', 9:'nine',10:'ten' ,
                11:'eleven', 12:'twelve' ,13:'thirteen' ,14:'fourteen' , 15:'fifteen' ,16:'sixteen', 17:'seventeen' ,18:'eighteen',19:'nineteen' ,20:'twenty' ,
                30:'thirty' ,40:'forty' ,50:'fifty' , 60:'sixty',70:'seventy',80:'eighty' ,90:'ninety',100:'hundred',1000:'thousand' }

    n_str= str(n).strip()
    eng=''

    if n>=1000:
        eng = numbers_eng[int(n_str[-4]) ] + ' ' + numbers_eng[1000]
    if n>=100:
        if (n_str[-3] != '0'):
            eng = eng  + ' ' + numbers_eng[int(n_str[-3]) ]+ ' ' + numbers_eng[100]


    dig = n % 100

    #有前有後
    if eng !='' and dig!=0 :
        eng = eng + ' and '

    if dig<20 :
        eng = eng  + numbers_eng[dig]
    else:
        dig2 = int(n_str[-2])
        dig3 = int(n_str[-1])
        eng = eng  + numbers_eng[dig2*10]
        if dig3>0 :
            eng = eng  + '-' + numbers_eng[dig3]
    return eng

def eng_chars(v):
    new=v.replace(' ','')
    new=new.replace('-','')
    return len(new)

sum =0 
for i in range(1,1001):
    n2eng = num2eng(i)
    sum = sum + eng_chars(n2eng)
    print( i , n2eng ,eng_chars(n2eng) )

print(sum)
