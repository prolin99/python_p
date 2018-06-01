import glob
pyfiles = glob.glob('./*.py')
for fn in pyfiles:
    print('file name:',fn)
    fin = open(fn,'rt')
    for line in fin:
        print(line.rstrip())
    fin.close()
    print('------')
