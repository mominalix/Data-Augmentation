import os
import re
current=os.getcwd()
print(current)
for a,filename in enumerate(os.listdir(current+'/annotations/xml/')):
    print(filename)
    file=open('annotations/xml/'+filename,'r')
    data=file.readlines()
    file.close()
    file=open('annotations/xml/'+filename,'w')
    filename = filename.split('.')
    data[2]='	<filename>'+filename[0]+'.jpg</filename>\n'
    data[3]='	<path>'+current+'\images\\'+filename[0]+'.jpg</path>\n'
    for lines in data:
        file.writelines(lines)
    file.close