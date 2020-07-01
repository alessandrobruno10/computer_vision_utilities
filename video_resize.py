#video_resize allows user to rescale a videosequence
#code usage:
#python video_resize.py video_filename width height
#example: python video_resize.py example.mp4 300 400

import cv2
import os
import numpy as np
import sys

def main():
    cap = cv2.VideoCapture(sys.argv[1]);
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = sys.argv[2]
    height = sys.argv[3]
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    videowriter = cv2.VideoWriter('rescaled_video.mp4',fourcc, fps,(int(width),int(height)))
    if cap:
        print("\n\t Video loading succeded...")
        ret, frame = cap.read()
        while ret:
            #
            frame2 = cv2.resize(frame,(int(width),int(height)),interpolation = cv2.INTER_AREA)
            ret, frame = cap.read()
            videowriter.write(frame2)
        videowriter.release()
    else:
        print("\n\t Some error occurred during the video opening...")

    print("\n\t The program execution has just finished...")



if __name__ == '__main__':
    main()
