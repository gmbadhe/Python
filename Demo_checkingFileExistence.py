import os,sys

fname=input("filename : ")
if os.path.isfile(fname):
    f1=open(fname,'r')
else:
    print(fname+'File not exists')
    sys.exit()
    
print('The file content: \n\n')
str=f1.read()
print(str)
f1.close()
