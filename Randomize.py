import os
import random

c_dir = os.getcwd()
images_path = os.path.join(c_dir+ '\\images') # path to original images
annotations_path=os.path.join(c_dir+ '\\annotations\\xml') # path to original labels

images = []  # to store paths of images from folder
annotations = [] # to store paths of labels from folder


for im in os.listdir(images_path):  # read image name from folder and append its path into "images" array
    images.append(im)
    os.rename(images_path+'\\'+im,images_path+'\\'+'a'+im)
for lab in os.listdir(annotations_path):
    os.rename(annotations_path+'\\'+lab,annotations_path+'\\'+'a'+lab)

size = len(images)  # Total number of images
randomlist=random.sample(range(size),size)
print(randomlist)

i=0
for im in os.listdir(images_path):  # read image name from folder and append its path into "images" array
    os.rename(images_path+'\\'+im,images_path+'\\'+str(randomlist[i])+'.jpg')
    i+=1
    
i = 0
for lab in os.listdir(annotations_path):  # read image name from folder and append its path into "images" array
    os.rename(annotations_path + '\\' + lab, annotations_path + '\\' + str(randomlist[i])+'.xml')
    i+=1
