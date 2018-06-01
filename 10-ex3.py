import re
import csv

with open('ex3.txt','rt') as fin:
    s=fin.read()
    s=re.findall('\w',s)
    wc=[]
    print(s)
    for w in set(s):
        print (w, s.count(w))
        wc.append([w,s.count(w)])
    #print(wc)
    swc=sorted(wc , key=lambda x:x[1], reverse=True)

    print(swc)
