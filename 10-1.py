import os
os.chdir('/home/user')
print(os.getcwd())
fds=os.listdir('.')
fds.sort()
print(fds)
for fd in fds:
    if os.path.isdir(fd):
        print('dir:', fd)
    else:
        print('file:',fd)
