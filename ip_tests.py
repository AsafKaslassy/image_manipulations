import cv2
import numpy as np
import os , os.path
from PIL import Image


# Paths
output_path = r"C:\Users\Assaf\PycharmProjects\untitled\output"
input_path = r"C:\Users\Assaf\PycharmProjects\untitled\input"




def load_images_from_folder(input_path):
    images = []
    valid_images = [".jpg",".tiff",".jpeg",".tif"]

    for filename in os.listdir(input_path):
        ext = os.path.splitext(filename)[1]
        if ext.lower() not in valid_images:
            continue
        img = cv2.imread(os.path.join(input_path,filename))
        if img is not None:
            images.append(img)
        print (os.path.join(input_path,filename))
    return;



def resize_images():

    # adjust width and height to your needs
    width = 640
    height = 480
    for image in load_images_from_folder.images:
    resized_image = images.resize((width, height), Image.BILINEAR)

#     pass
#
# def find_edges():
#
#      # edges = cv2.Canny(gray,20,250,apertureSize = 3)
#
#     pass
#
# def feature_matching():
#     pass
#
#
#
#
# def find_lines():
#     """
#     TODO:
#     add docstrings to functions
#     :return:
#     """
#     if not os.path.exists('output'):
#         os.makedirs('output')
#
#     line_img = cv2.imread(input_path)
#     gray = cv2.cvtColor(line_img,cv2.COLOR_BGR2GRAY)
#     edges = cv2.Canny(gray,20,250,apertureSize = 3)
#     cv2.imwrite(output_path + '\IntermediateOutput.jpg' ,edges)
#
#     minLineLength = 999999
#     maxLineGap =  10
#     lines = cv2.HoughLinesP(edges,1,np.pi/180,150,minLineLength,maxLineGap)
#
#     for i in range(len(lines)):
#         for x1,y1,x2,y2 in lines[i]:
#             cv2.line(line_img,(x1,y1),(x2,y2),(255,0,10),3)
#
#     cv2.imwrite(output_path + '\HoughLineOutput.jpg' ,line_img)
#
#
# def circle_detection():
#     """
#     :return:
#     """
#     img = cv2.imread(input_path,0)
#     img = cv2.medianBlur(img,5)
#     cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
#
#     circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
#                                 param1=160,param2=40,minRadius=0,maxRadius=0)
#
#     circles = np.uint16(np.around(circles))
#     if not os.path.exists('output'):
#         os.makedirs('output')
#
#     for i in circles[0,:]:
#         # draw the outer circle
#         cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
#         # draw the center of the circle
#         cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
#
#     cv2.imwrite(output_path + '\circles.jpg' ,cimg)
#
#
#
# def save_outputs():
#
#     pass
#
#
#
#

if __name__ == '__main__':
    print('\n started...\n')
    load_images_from_folder(input_path)
    # find_lines()
    # circle_detection()
    print('\n finished...\n')
