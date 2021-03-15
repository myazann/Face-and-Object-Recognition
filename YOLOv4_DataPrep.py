
import os

path = "data/dataset4"

for file in os.listdir(path):
    old_file_path = os.path.join(path,file)
    if ".xml" in file:
        new_name = file.replace(".xml","")
        new_file_path = os.path.join(path,new_name)
        file = os.rename(old_file_path, new_file_path)
        ##os.remove(old_file_path)
 

path = "data/dataset4"

for file in os.listdir(path):
    old_file_path = os.path.join(path,file)
    if "ğ" in file:
        new_name = file.replace("ğ","g")
        new_file_path = os.path.join(path,new_name)
        file = os.rename(old_file_path, new_file_path)
        ##os.remove(old_file_path)


# In[2]:


path = "data/dataset4"
from PIL import Image


for file in os.listdir(path):
    if file.split(".")[1] == "jpeg":
        file_path = path + "/" + file
        img = Image.open(file_path)
        ##img = Image.open(file_path).convert('PNG')
        img.save(path + "/" + file.split(".")[0] + ".jpg")
        os.remove(file_path)


# In[4]:


import numpy as np
import os

path = "data/dataset4"
img_list = []


for file in os.listdir(path):
    if file.split(".")[-1] == "jpg":
        file_name = path + "/" + file
        img_list.append(file_name)

    
    
img_list = list(np.random.permutation(np.array(img_list)))

train_len = int(len(img_list)*0.8)

test_len = len(img_list) - train_len

train = img_list[0:train_len]

test = img_list[train_len:]

with open("data/train.txt", "w") as train_file:
    for elem in train:
        train_file.write(elem + "\n")
    
with open("data/test.txt", "w") as test_file:
    for elem in test:
        test_file.write(elem + "\n")

