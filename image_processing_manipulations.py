import cv2
import numpy as np
import os , os.path
from PIL import Image

class Images(object):

    def __init__(self, input_path, output_path):
        self.imageNames = os.listdir(input_path)

        self.imageList = list()
        # for image in self.imageArr :
        #     img = cv2.imread(os.path.join(input_path, image))
        #     extension = os.path.splitext(image)[1]
        #     # if extension.lower() not in self.valid_images:
        #         continue
        #     print ("\nreading " + (os.path.join(input_path, image)))
        #     filename = os.path.splitext(image)[0]
        #     # print (os.path.splitext(image)[0])
        #     gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #     cv2.imwrite(str(output_path) + filename + extension,gray)
        #     print ("Saving ->" + (os.path.join(output_path, image)))
        #
        # self.filename = filename
        # self.new_width = new_width
        # self.new_height = new_height
        # self.input_path = input_path

    def load_images(self):

        valid_images = [".jpg", ".tiff", ".jpeg", ".tif", ".bmp"]
        for idx, imageName  in enumerate(self.imageNames):
            extension = os.path.splitext(imageName)[1]
            if extension.lower() not in valid_images:
                continue
            print ("\nreading " + (os.path.join(input_path, imageName)))
            self.imageList.append(cv2.imread(os.path.join(input_path, imageName)))
            filename = os.path.splitext(imageName)[0]
            # print (os.path.splitext(image)[0])
            self.imageList[idx] = cv2.cvtColor(self.imageList[idx], cv2.COLOR_BGR2GRAY)
            cv2.imwrite(os.path.join(str(output_path), filename + extension), self.imageList[idx])
            print ("Saving ->" + (os.path.join(output_path, imageName)))

    def resize_images(self):

        new_width  = 640
        new_height = 480

        for idx, image in enumerate(self.imageList):
            resized = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)
            
            #resized = Image.resize((new_width, new_height), Image.ANTIALIAS)
            cv2.imwrite(os.path.join(str(output_path), "Resized_" + self.imageNames[idx]), resized)


if __name__ == '__main__':

    print('\n started...\n')

    input_path = r"D:\Output\Test"
    output_path = r"D:\Output\Test\Output"
    KasTheKing = Images(input_path,output_path)

    KasTheKing.load_images()
    KasTheKing.resize_images()

    print('\n finished...\n')

#     pass
#
# def find_edges(self,):
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
# def find_lines(self,):
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

# def save_outputs():
#
#     pass
#

