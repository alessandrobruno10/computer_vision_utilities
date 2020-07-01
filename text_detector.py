'''
created on Tuesday the 26th of May 2020
@author: Alessandro Bruno
'''

#the code snippet down below allows for the extraction of text from frames
#the objective within the frame of the current project is to detect all text
#in a given video-sequence

from PIL import Image
import pytesseract
from wand.image import Image as Img
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import numpy as np
import glob
import os
os.chdir('image_frames')
filenames = sorted(glob.glob('*.png'), key=os.path.getmtime)

for name in filenames:
    demo = Image.open(name)
    text = pytesseract.image_to_string(demo, lang='eng')
    print(text)
