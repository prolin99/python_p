dict1={}
lang={'早安':'good Morning','午安':'good afternoon'}
print(lang)
print(lang['早安'])
print(lang.get('早'))
print(lang.pop('早安'))
print(lang)
lang2={'你好':'hi'}
lang.update(lang2)
print(lang)

for ch,en in lang.items():
    print(ch,en)
for ch in lang.keys():
    print(ch)
for en in lang.values():
    print(en)
