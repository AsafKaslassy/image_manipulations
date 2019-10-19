import os
import cv2
import numpy as np


class Images(object):

    def __init__(self):
        self.imageNames = os.listdir(input_path)
        self.imageList = []


    def load_images(self):

        valid_images = [".jpg", ".tiff", ".jpeg", ".tif", ".bmp"]
        for idx, imageName  in enumerate(self.imageNames):
            extension = os.path.splitext(imageName)[1]
            if extension.lower() not in valid_images:
                continue
            print ("\nreading " + (os.path.join(input_path, imageName)))
            self.imageList.append(cv2.imread(os.path.join(input_path, imageName)))
            filename = os.path.splitext(imageName)[0]
            self.imageList[idx] = cv2.cvtColor(self.imageList[idx], cv2.COLOR_BGR2GRAY)
            if not os.path.exists('Gray'):
                os.makedirs('output/Gray', exist_ok=True)
            gray_golder_path = os.path.join(str(output_path)+'\Gray', filename + extension)
            cv2.imwrite(gray_golder_path, self.imageList[idx])
            print ("Saving ->" + gray_golder_path)


    def resize_images(self):

        new_width  = 640
        new_height = 480

        for idx, image in enumerate(self.imageList):
            resized = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)
            if not os.path.exists('output\Resized'):
                os.makedirs('output\Resized')
            cv2.imwrite(os.path.join(str(output_path)+'\Resized', "resized_" + self.imageNames[idx]), resized)

    def find_lines(self):
        """
        TODO:
        add docstrings to functions
        :return:
        """
        if not os.path.exists('output\lines'):
            os.makedirs('output\lines')
            os.makedirs('output\edges')
        for idx, image in enumerate(self.imageList):
            # gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(image,20,250,apertureSize = 3)
            cv2.imwrite(os.path.join(str(output_path)+'\edges', "edges" + self.imageNames[idx]), edges)

            minLineLength = 999
            maxLineGap =  10
            lines = cv2.HoughLinesP(edges,1,np.pi/180,150,minLineLength,maxLineGap)

            for i in range(len(lines)):
                for x1,y1,x2,y2 in lines[i]:
                    cv2.line(image,(x1,y1),(x2,y2),(255,0,10),3)

            cv2.imwrite(os.path.join(str(output_path)+'\lines', "lines" + self.imageNames[idx]), lines)



if __name__ == '__main__':

    print('\n started...\n')

    input_path = r"C:\Users\Assaf\PycharmProjects\untitled\input"
    output_path = r"C:\Users\Assaf\PycharmProjects\untitled\output"
    ImageClass = Images()

    ImageClass.load_images()
    ImageClass.resize_images()
    ImageClass.find_lines()

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

