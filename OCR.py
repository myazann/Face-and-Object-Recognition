#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pytesseract as pt
import cv2
from PIL import Image
import numpy as np


pt.pytesseract.tesseract_cmd = r'D:\Uygulamalar\Tesseract\tesseract.exe'


# In[116]:


thresholds = [75,100,125]

def image_threshold(im, thresholds):
    
    for thr in thresholds:

        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        thres_1 = cv2.threshold(gray, thr, 255, cv2.THRESH_BINARY_INV)
                
        text_gray = pt.image_to_string(thres_1[1])
        
        sonuc_gray = np.asarray(text_gray.strip().split())
            
        if sonuc_gray.size != 0:
            print(f"{thr} Threshold sonuçlar: {sonuc_gray}")


# In[117]:


cap = cv2.VideoCapture(0)
length_checker = np.vectorize(len) 

while(True):
    try:
        ret, frame = cap.read()
        
        im = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)


        text = pt.image_to_string(frame)
        sonuc = np.asarray(text.strip().split())

        if sonuc.size != 0:
            
            print("Oynanmamış fotoda sonuçlar: ", sonuc)
            
        image_threshold(im, thresholds)
                       
                
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    except Exception as e:
        print(e)

cap.release()
cv2.destroyAllWindows()


# <h5> See image

# In[95]:


Image.fromarray(im)


# <h5> Make image blurrier or illuminate it

# In[ ]:


aydın = cv2.add(im, np.array([50.0]))
blur = cv2.GaussianBlur(im, (9,9), 3)   


# <h5> Only print numbers

# In[ ]:


if True in np.char.isdigit(sonuc):
    print(sonuc[np.char.isdigit(sonuc)])
                

