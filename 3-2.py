shoplist=['apple','milk','pen']
print(shoplist)
print(shoplist[0])
print(len(shoplist))

shoplist[2]='eggs'
print(shoplist)

print(shoplist.index('milk'))

shoplist.append('bread')

print(shoplist)

shoplist.insert(0,'butter')
print(shoplist)

buy =shoplist.pop()
print(buy)
print(shoplist)
shoplist.pop(1)
print(shoplist)


shoplist.sort()
print(shoplist)

for item in shoplist:
    print(item)


newlist=['paper','ox']
newshoplist=shoplist+newlist
print(newshoplist)
