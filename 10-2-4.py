s='111\n\
2222'
try:
    fs= open('2.txt','wt')
    print(s,file=fs)
    #fs.write(s)
    #fs.close()
except:
    print('file save error')
