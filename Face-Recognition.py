import os
import sys
py_dll_path = os.path.join(sys.exec_prefix, 'Library', 'bin')
os.environ['PATH'] += py_dll_path

import warnings
warnings.filterwarnings("ignore")

from facenet_pytorch import MTCNN, InceptionResnetV1
import torch
from torch.utils.data import DataLoader
from torchvision import datasets
import numpy as np
import pandas as pd
import cv2
import csv

workers = 0 if os.name == 'nt' else 4


device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print('Running on device: {}'.format(device))


def verify(img1_path, img2_path, detector_backend):
    
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)
    
    if detector_backend == "mtcnn":
    
        img1_aligned = mtcnn(img1, return_prob=False)
        img2_aligned = mtcnn(img2, return_prob=False)

        aligned1 = []
        aligned2 = []

        aligned1.append(img1_aligned)
        aligned2.append(img2_aligned)
        
        aligned1 = torch.stack(aligned1).to(device)
        aligned2 = torch.stack(aligned2).to(device) 
        
    
    e1 = resnet(aligned1).detach()
    e2 = resnet(aligned2).detach()
    
    return (e1 - e2).norm().item()


mtcnn = MTCNN(
    image_size=160, margin=0, min_face_size=20,
    thresholds=[0.6, 0.7, 0.7], factor=0.709, post_process=True,
    device=device
)


resnet = InceptionResnetV1(pretrained='vggface2').eval().to(device)



cap = cv2.VideoCapture(0)

## change path to your photo
anchor_photo = "FaceRecognition_dataset/osym/mert_yazan.jpg"

img2 = cv2.imread(anchor_photo)
img2_aligned = mtcnn(img2, return_prob=False)

aligned2 = []
aligned2.append(img2_aligned)
aligned2 = torch.stack(aligned2).to(device) 

e2 = resnet(aligned2).detach()


dist = 0

while True:
    try:
        ret, frame = cap.read()
        img1_aligned = mtcnn(frame, return_prob=False)
        
        aligned1 = []
        aligned1.append(img1_aligned)
        
        aligned1 = torch.stack(aligned1).to(device) 

        e1 = resnet(aligned1).detach()
        
        dist = (e1 - e2).norm().item()
        
        frame = cv2.putText(frame, str(dist), (300, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))

        cv2.imshow('frame',frame)
        
        
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    except Exception as e:
        print(e)

cap.release()
cv2.destroyAllWindows()  

