# For deeplearning
import tensorflow as tf       
from tensorflow import keras 
from keras.utils.np_utils import to_categorical 
from tensorflow.keras.preprocessing.image import ImageDataGenerator 
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
# For managing files   
import os
# For image manipulation
from PIL import Image
import cv2
import imutils
# Vectorized code, translate images into vector arrays
import numpy as np
# Data processing, confusion matrix and classification report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder 
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import classification_report
# For visualization and image display
import matplotlib.pyplot as plt
import cv2
import imutils
from google.colab.patches import cv2_imshow
# Utilities
from collections import Counter
import copy
import random