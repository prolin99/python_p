#從20*20方格的左上角出發，沿著向右或向下的路徑前進，最後到達右下角，總共幾種不同的走法？
#列出各路徑， 但會跑不完  (20+20)！/ (20！*20！)

def MOVEF(a,b,path):
    global okPath
    global max
    #print('--',a,b,path)

    if (a<5)  :
        tpath=path+'a'
        ta= a+1
        #print(ta,b,tpath)
        MOVEF(ta,b,tpath)


    if (b<5) :
        tpath=path+'b'
        tb= b+1
        #print(a,tb,tpath)
        MOVEF(a,tb,tpath)

    if(a==5) and (b==5):
        if path!='' :
            #okPath.append(path)
            print(path)
            max =max+1
        return 1


path=''
max =0
okPath=[]
MOVEF(0,0,path)


#print( len(okPath))
print(max)
