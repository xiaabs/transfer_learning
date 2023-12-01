#Download the CalTech256 dataset
#Create three directories with names train, valid and test.
#Create 10 sub-directories each inside the train and the test directories. The sub-directories should be named bear, chimp, giraffe, gorilla, llama, ostrich, porcupine, skunk, triceratops and zebra.
#Move the first 60 images for bear in the Caltech256 dataset to the directory train/bear. Repeat this step for every animal.
#Move the next 10 images for bear in the Caltech256 dataset to the directory valid/bear. Repeat this step for every animal.
#Copy the remaining images for bear (i.e. the ones not included in a train or valid folders) to the directory test/bear. Repeat this step for every animal.

import shutil
import os
root=os.getcwd()
print("currant path is :")
print(root)
dir = root+"/256_ObjectCategories"
print("dataset is in folder：")
print(dir)


def create_folder(name):
    x=root+"/"+name
    if not os.path.exists(x):
         os.makedirs(x)
    return x

train_path=create_folder("train")
valid_path=create_folder("valid")
test_path=create_folder("test")
    
print(train_path)
# trainfolders=root+"/train"
# if not os.path.exists(trainfolders):
#     os.makedirs(trainfolders)

# 搜索指定目录
#results = []
#folders = [dir]

#循环 caltech256 下的256文件夹
specify_set=["bear", "chimp", "giraffe", "gorilla", "llama", "ostrich", "porcupine", "skunk", "triceratops", "zebra"]
#specify_str = 'ak47'
for specify_str in specify_set:
    for x in os.listdir(dir):
        #匹配包含字符串的文件夹
        if specify_str in x:
            spec_dir=dir+"/"+x
            print(x)
            print(spec_dir)
            
            train_dst=train_path+"/"+specify_str
            if not os.path.exists(train_dst):
                os.makedirs(train_dst)
                
            valid_dst=valid_path+"/"+specify_str
            if not os.path.exists( valid_dst):
                os.makedirs( valid_dst)   
                
            test_dst=test_path+"/"+specify_str
            if not os.path.exists(test_dst):
                os.makedirs(test_dst) 
            a=os.listdir(spec_dir)
            a.sort()
            print(a)
            #匹配目标文件夹中的文件，
            i=0
            for xx in a:
                i=i+1
                src=spec_dir+'/'+xx
                if i<=60:
                    shutil.copyfile( src, train_dst+'/'+xx) 
                elif i>60 and i<=70:
                    shutil.copyfile( src, valid_dst+'/'+xx) 
                else: 
                    shutil.copyfile( src, test_dst+'/'+xx)
            
            

