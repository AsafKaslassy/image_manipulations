import os
import cv2
import numpy as np
import configparser


class Images(object):

    def __init__(self):
        self.input_path = r"C:\Users\Assaf\PycharmProjects\untitled\input"
        self.output_path = r"C:\Users\Assaf\PycharmProjects\untitled\output"
        self.imageNames = os.listdir(self.input_path)
        self.imageList = []
        self.new_width  = 1080
        self.new_height = 1920
        self.valid_images = \
        [".jpg" ,  ".tiff", ".jpeg", ".tif"  ,".bmp" ]


    def prep_folders(self):

        if not os.path.exists('output/Gray'):
            os.makedirs('output/Gray')
        if not os.path.exists('output\Resized'):
            os.makedirs('output\Resized')
        if not os.path.exists('output\lines'):
            os.makedirs('output\lines')
        if not os.path.exists('output\edges'):
            os.makedirs('output\edges')
        if not os.path.exists('output\edges\Sobel_edges'):
            os.makedirs('output\edges\Sobel_edges')
        if not os.path.exists('output\edges\Canny_edges'):
            os.makedirs('output\edges\Canny_edges')
        if not os.path.exists('output\circles'):
            os.makedirs('output\circles')


    def load_images(self):

        for idx, imageName  in enumerate(self.imageNames):
            extension = os.path.splitext(imageName)[1]
            if extension.lower() not in self.valid_images:
                continue
            print ("\nreading " + (os.path.join(self.input_path, imageName)))
            self.imageList.append(cv2.imread(os.path.join(self.input_path, imageName)))
            filename = os.path.splitext(imageName)[0]
            self.imageList[idx] = cv2.cvtColor(self.imageList[idx], cv2.COLOR_BGR2GRAY)
            gray_golder_path = os.path.join(str(self.output_path)+'\Gray', filename + extension)
            cv2.imwrite(gray_golder_path, self.imageList[idx])


    def resize_images(self):

        for idx, image in enumerate(self.imageList):
            resized = cv2.resize(image, (self.new_width, self.new_height), interpolation=cv2.INTER_AREA)
            print ("\n resizing " + os.path.join(str(self.output_path)+'\Resized', "resized_" + self.imageNames[idx]))
            cv2.imwrite(os.path.join(str(self.output_path)+'\Resized', "resized_" + self.imageNames[idx]), resized)


    def find_lines(self):
        """
        TODO:
        add docstrings to functions
        :return:
        """

        for idx, image in enumerate(self.imageList):
            # gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            Canny_edges = cv2.Canny(image,5,250,apertureSize = 3)
            Sobel_edges = cv2.Sobel(image, cv2.CV_16S, 0, 1, ksize=3, scale=2, delta=1, borderType=cv2.BORDER_DEFAULT)
            cv2.imwrite(os.path.join(str(self.output_path)+'\edges\Sobel_edges', "Sobel_" + self.imageNames[idx]), Sobel_edges)
            cv2.imwrite(os.path.join(str(self.output_path)+'\edges\Canny_edges', "Canny_" + self.imageNames[idx]), Canny_edges)
            print ("\n   finding edges  " + os.path.join(str(self.output_path), "Edges_" + self.imageNames[idx]))

            ## DrawLines on edges
            # minLineLength = 9999
            # maxLineGap =  100
            # lines = cv2.HoughLinesP(edges,1,np.pi/180,150,minLineLength,maxLineGap)
            # for i in range(len(lines)):
            #     for x1,y1,x2,y2 in lines[i]:
            #         cv2.line(edges,(x1,y1),(x2,y2),(255,0,10),3)
            # cv2.imwrite(os.path.join(str(output_path)+'\lines', "lines" + self.imageNames[idx]), lines)


    # def sift(self):
    #     """
    #     """
    #     for idx, image in enumerate(self.imageList):
    #         # self.imageList[idx] = cv2.cvtColor(self.imageList[idx], cv2.COLOR_BGR2GRAY)
    #         sift = cv2.xfeatures2d.SIFT_create()
    #         kp = sift.detect(image,None)
    #
    #         img=cv2.drawKeypoints(image,kp)
    #
    #         cv2.imwrite('sift_keypoints.jpg',img)



        ## Load the configuration file

        # with open("config.ini") as f:
        #     sample_config = f.read()
        # config = ConfigParser.RawConfigParser(allow_no_value=True)
        # config.readfp(io.BytesIO(sample_config))
        #
        # # List all contents
        # print("List all contents")
        # for section in config.sections():
        #     print("Section: %s" % section)
        #     for options in config.options(section):
        #         print("x %s:::%s:::%s" % (options,
        #                                   config.get(section, options),
        #                                   str(type(options))))
        #
        # # Print some contents
        # print("\nPrint some contents")
        # print(config.get('other', 'use_anonymous'))  # Just get the value
        # print(config.getboolean('other', 'use_anonymous'))  # You know the datatype?


            # cv2.imwrite(os.path.join(str(output_path)+'\circles', "Circles_" + self.imageNames[idx]), cimg)


    # def circle_detection(self):
    #     """
    #     """
    #     for idx, image in enumerate(self.imageList):
    #         image = cv2.medianBlur(image,21)
    #         print ("blurring image", image)
    #         cimg = cv2.cvtColor(image,cv2.COLOR_GRAY2BGR)
    #
    #         circles = cv2.HoughCircles(self.imageList[idx],cv2.HOUGH_GRADIENT,1,20,
    #                                     param1=160,param2=40,minRadius=0,maxRadius=0)
    #         # circles = np.uint16(np.around(circles))
    #         for i in circles[0,:]:
    #             print (i)
    #             # draw the outer circle
    #             cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    #             # draw the center of the circle
    #             cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    #
    #         cv2.imwrite(os.path.join(str(output_path)+'\circles', "Circles_" + self.imageNames[idx]), cimg)


if __name__ == '__main__':

    print('\n started...\n')

    ImageClass = Images()

    ImageClass.prep_folders()
    ImageClass.load_images()
    ImageClass.resize_images()
    ImageClass.find_lines()
    # ImageClass.sift()

    print('\n finished...\n')



# TODO:
# read from config.ini
# export info to XMl and Json
# run with a gui
# compile

