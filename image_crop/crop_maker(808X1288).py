from PIL import Image
import numpy as np
import re
import glob
import os

images_DD=glob.glob('.\DD\*\*.jpg')
images_DD=np.array(images_DD).tolist()

images_NN=glob.glob('.\\NN\*\*.jpg')
images_NN=np.array(images_NN).tolist()

images_kind=[images_DD,images_NN]
folder_name=['/DD','/NN']

def createfolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
            pass
        
def image_cropper(images_kind,folder_name): 
    for i in range(len(images_kind)):
        if 'TMJ' in images_kind[i]:
            for j in range(4):

                image = Image.open(images_kind[i])
                if j<=1:
                    croppedImage=image.crop((22*(j+1)+(11+51+808)*j,58,(22+808)*(j+1)+(11+51)*j,1346))
                elif j==2:
                    croppedImage=image.crop((22*(2)+(11+51+808)*2,58,808+(22+808)*(2)+(11+51)*2,1346))
                else:
                    croppedImage=image.crop((22*(2)+(11+51+808)*2+808+33+51,58,808+(22+808)*(2)+(11+51)*2+808+33+51,1346))
                pattern=re.compile(r'\d+')
                number=pattern.search(images_kind[i])
                number=number.group()

                if j==0:
                    directory=f'.{folder_name}\R_C'
                    createfolder(directory)
                    croppedImage.save(f'.{folder_name}\R_C{folder_name}_R_C_{number}.PNG','png')
                elif j==1:
                    directory=f'.{folder_name}\R_O'
                    createfolder(directory)
                    croppedImage.save(f'.{folder_name}\R_O{folder_name}_R_O_{number}.PNG','png')
                elif j==2:
                    directory=f'.{folder_name}\L_O'
                    createfolder(directory)
                    croppedImage.save(f'.{folder_name}\L_O{folder_name}_L_O_{number}.PNG','png')
                else:
                    directory=f'.{folder_name}\L_C'
                    createfolder(directory)
                    croppedImage.save(f'.{folder_name}\L_C{folder_name}_L_C_{number}.PNG','png')

for i in range(len(images_kind)):
    image_cropper(images_kind[i],folder_name[i])