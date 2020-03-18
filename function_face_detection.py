#the python code down below is a function who returns the coordinates, width and height of the bounding box concerning the closest face to the screen.
#In our work our hypothesis is the closest person to be the most engaged. Further developments could be integrated together with the output of posent

#the algorithm down below aims to identify the biggest rectangle within the ones detected as it is supposed to be of the most engaged person
import sys
import cv2
import numpy as np
#the relative path of the haarcascade_frontalface_default is put down below
cascPath = './haarcascade_frontalface_default.xml'

#the function has a single frame as an argument
def function_face_detection(frame):
    # Create the haar cascade from cascPath using cv2 library
    faceCascade = cv2.CascadeClassifier(cascPath)
    # Read the image

    image = frame
    #note that faceCascade works with grayscale Images, it is needed to convert RGB images
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('image',image)
    #cv2.waitKey(0)
    #now face intances over the image are extracted using the method "detectMulticale"
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    NUM_FACES = (len(faces))
    #let's play with faces... i.e. counting the number of people gathered in front of the screen/camera
    if NUM_FACES == 1:
        #if faceCascade detects a single instance of faces the output will be arranged as it follows:
        #faces[0][0] = X coordinate
        #faces[0][1] = Y coordinate
        #faces[0][2] = width in pixels
        #faces[0][3] = height in pixels

        print('\n\t num faces detecetd is 1')
        return faces[0][0], faces[0][1], faces[0][0]+faces[0][2], faces[0][1]+faces[0][3]

    elif (NUM_FACES==0):
        print('\n\t num faces detecetd is 0')
        ppp = np.zeros(0)
        return ppp

    elif (NUM_FACES>1):
        print('\n\t num faces detecetd is :::',NUM_FACES)
        # if the algorithm detects multiple instances of face in the image we need to calculate the area of each face and then select the biggest one
        temp = 0 #we want to compute area values of each face detected
        print("\n faces size is :::",faces.shape)
        faces_w_h = faces[:,2:4]
        Area = np.zeros((4,1))

        for i in range(4):
            Area[i]=faces_w_h[i][0]*faces_w_h[i][1]

        print("\n faces size is :::",faces_w_h.shape)
        print("\n Area size is :::",Area.shape)
        INDEX = np.argmax(Area) #retrieving the max area value index
        #for (x, y, w, h) in faces:
        #cv2.rectangle(image, (faces[INDEX][0], faces[INDEX][1]), (faces[INDEX][0]+faces[INDEX][2], faces[INDEX][1]+faces[INDEX][3]), (0, 255, 0), 2)
        return faces[INDEX][0], faces[INDEX][1], faces[INDEX][0]+faces[INDEX][2], faces[INDEX][1]+faces[INDEX][3]
