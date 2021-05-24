import os
collection = os.getcwd()
i = 90
for a,filename in enumerate(os.listdir(collection)):
    os.rename(collection+'/Data/annotations/' + filename, collection+'/Data/annotations/' + str(i) + ".xml")
    i=i+1