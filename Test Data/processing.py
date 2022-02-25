import os
import shutil

def convert(size, box):
    w = box[2]*size[0]
    h = box[3]*size[1]
    x = box[0]*size[0]
    y = box[1]*size[1]
    dw=640
    dh=512
    x = round(x/dw,6)
    w = round(w/dw,6)
    y = round(y/dh,6)
    h = round(h/dh,6)

    return (x,y,w,h)

targetDir = r"C:\Users\User\Desktop\car\yolov5-master\Test Data\RGB\labels\val"
targetDir2 = r"C:\Users\User\Desktop\car\yolov5-master\Test Data\RGB\IR_labels"
num = 0
file_list = os.listdir(targetDir)

size=[2048,1536]

txt_list = []
for file in file_list:
    if '.txt' in file:
        txt_list.append(file)

for txt_file in txt_list:
    num+=1
    name=txt_file.split('-')[1]
    target_path = targetDir + "\\" + txt_file
    target_path2 = targetDir2 + "\\" + "lwir-"+name
    targetTXT = open(target_path, 'r')
    line= targetTXT.readlines()
    
    for word in line:
        box=word.split(' ')
        bbox=[float(box[1]),float(box[2]),float(box[3]),float(box[4])]
        bbox=convert(size,bbox)
        line=f'{box[0]} {bbox[0]} {bbox[1]} {bbox[2]} {bbox[3]}\n'
        newfile=open(target_path2,'a')
        newfile.write(word)
        newfile.close()

print(num)
print("done")