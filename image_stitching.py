import numpy as np
import cv2
import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("input_path", required=True, type=str, help="path to list of input images for image stitching")
ap.add_argument("output_path", required=True, type=str, help="path to output image")

imagePaths=os.listdir(input_path)
images=[]
for imagePath in imagePaths:
    image=cv2.imread(path+imagePath)
    images.append(image)
    
stitcher=cv2.Stitcher_create()
(status, stitched) = stitcher.stitch(images)
if status == 0:
    stitched1 = cv2.copyMakeBorder(stitched, 10, 10, 10, 10,cv2.BORDER_CONSTANT, (0, 0, 0))
    gray = cv2.cvtColor(stitched1, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)[1]
    cnts, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts=sorted(cnts,key=cv2.contourArea,reverse=True)
    mask = np.zeros(thresh.shape, dtype="uint8")
    (x, y, w, h) = cv2.boundingRect(cnts[0])
    res = cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)
    minRect = mask.copy()
    sub = mask.copy()
    # Eliminate excess black portion by 99%
    c=cv2.countNonZero(sub)*0.01
    while cv2.countNonZero(sub) > c:
        minRect = cv2.erode(minRect, None)
        sub = cv2.subtract(minRect, thresh)

    cv2.destroyAllWindows()
    cnts, hierarchy = cv2.findContours(minRect.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts=sorted(cnts,key=cv2.contourArea,reverse=True)
    (x, y, w, h) = cv2.boundingRect(cnts[0])
    stitched1 = stitched1[y:y + h, x:x + w]
    cv2.imwrite(output_path+"stitched.jpg",stitched)
    cv2.imwrite(output_path+"cropped.jpg",stitched1)
else:
    print("Image stitching failed!")
