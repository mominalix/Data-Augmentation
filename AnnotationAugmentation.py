import numpy as np
import re
import os

def min_max(Anticlockwise):
    if Anticlockwise[0][0] < Anticlockwise[1][0]:
        xmin = Anticlockwise[0][0]
        xmax = Anticlockwise[1][0]
    else:
        xmin = Anticlockwise[1][0]
        xmax = Anticlockwise[0][0]
    if Anticlockwise[0][1] < Anticlockwise[1][1]:
        ymin = Anticlockwise[0][1]
        ymax = Anticlockwise[1][1]
    else:
        ymin = Anticlockwise[1][1]
        ymax = Anticlockwise[0][1]
    return [[int(xmin), int(ymin)], [int(xmax), int(ymax)]]


def rotate(p, origin=(0, 0), degrees=0):
    angle = np.deg2rad(degrees)
    R = np.array([[np.cos(angle), -np.sin(angle)],
                  [np.sin(angle), np.cos(angle)]])
    o = np.atleast_2d(origin)
    p = np.atleast_2d(p)
    return np.squeeze((R @ (p.T - o.T) + o.T).T)


def flip(p, center, flip_direction):
    new = []
    if flip_direction == 'H':
        for point in p:
            a = point[0] - center[0]
            if a < 0:
                point[0] = point[0] - (a * 2)
            elif a > 0:
                point[0] = point[0] - (a * 2)
            new.append(point)

    if flip_direction == 'V':
        for point in p:
            a = point[1] - center[1]
            if a < 0:
                point[1] = point[1] - (a * 2)
            elif a > 0:
                point[1] = point[1] - (a * 2)
            new.append(point)
    return new

def Writefile(points,index,data):
    name = index
    print('name is:'+name)
    newfile= open('annotations/xml/'+name+'.xml','w')
    i=0
    data[2]='	<filename>'+name+'.png</filename>\n'
    data[3]='   	<path>C:\\Users\Momin\Desktop\Resource Sharing with Rovers\Pygame_Simulation\V3.0\Object detection\dataset\\'+name+'.png</path>\n'
    data[19] ='			<xmin>'+str(points[0][0])+'</xmin>\n'
    data[20] ='			<ymin>'+str(points[0][1])+'</ymin>\n'
    data[21] ='			<xmax>'+str(points[1][0])+'</xmax>\n'
    data[22] ='			<ymax>'+str(points[1][1])+'</ymax>\n'
    for line in data:
            newfile.write(line)
    newfile.close()




c_dir = os.getcwd()
orignal_path = os.path.join(os.getcwd(), 'sample images') # path to original images
files = []  # to store paths of images from folder

for im in os.listdir(orignal_path):  # read image name from folder and append its path into "images" array
    files.append(im)
    print(im)
idx =89
for file in files:
    Name=file.split('.')
    filename=Name[0]
    inFile = open('sample labels/'+filename+'.xml', 'r')
    data = inFile.readlines()

    Xmin = re.split('[><]', data[19])
    Ymin = re.split('[><]', data[20])
    Xmax = re.split('[><]', data[21])
    Ymax = re.split('[><]', data[22])

    min = [int(Xmin[2]), int(Ymin[2])]
    max = [int(Xmax[2]), int(Ymax[2])]

    print(min, max)
    # Points to be rotated
    points = (min, max)

    # Centre of rotation
    origin = (320, 240)
    #

    Anticlockwise = rotate([[points[0][0],points[0][1]],[points[1][0],points[1][1]]], origin=origin, degrees=-90)
    Anticlockwise = min_max(Anticlockwise)

    Clockwise = rotate([[points[0][0],points[0][1]],[points[1][0],points[1][1]]], origin=origin, degrees=90)
    Clockwise = min_max(Clockwise)

    horizontal_flip = flip([[points[0][0],points[0][1]],[points[1][0],points[1][1]]], [320, 240], 'H')
    horizontal_flip = min_max(horizontal_flip)

    vertical_flip = flip([[points[0][0],points[0][1]],[points[1][0],points[1][1]]], [320, 240], 'V')
    vertical_flip = min_max(vertical_flip)

    noise = points
    noise = min_max(noise)
    idx+=1
    print(Anticlockwise)
    Writefile(Anticlockwise,str(idx),data)
    idx+=1
    print(Clockwise)
    Writefile(Clockwise,str(idx),data)
    idx+=1
    print(horizontal_flip)
    Writefile(horizontal_flip,str(idx),data)
    idx+=1
    print(vertical_flip)
    Writefile(vertical_flip,str(idx),data)
    idx+=1
    print(noise)
    Writefile(noise,str(idx),data)