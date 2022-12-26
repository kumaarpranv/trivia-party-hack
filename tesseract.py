
import time
import cv2
import keyboard
import pytesseract
import pyautogui
from pytesseract import Output
import numpy as np
pytesseract.pytesseract.tesseract_cmd = (r"C:\Program Files\Tesseract-OCR\tesseract") # needed for Windows as OS

def ret_tess(img):
    blur = cv2.GaussianBlur(img, (3,3), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    invert = 255 - opening
    data = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')
    return data

def take_screenshot():
    screenshot = pyautogui.screenshot()
    img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)
    question = img[int(len(img)*0.448):int(len(img)*0.53), int(len(img[0])*0.415):int(len(img[0])*0.63)]
    answer = img[int(len(img)*0.45):int(len(img)*0.77), int(len(img[0])*0.35):int(len(img[0])*0.66)]
    option1 = img[int(len(img)*0.571):int(len(img)*0.64), int(len(img[0])*0.37):int(len(img[0])*0.49)]
    option2 = img[int(len(img)*0.571):int(len(img)*0.64), int(len(img[0])*0.37 + len(img[0])*0.13):int(len(img[0])*0.49 + len(img[0])*0.13)]
    option3 = img[int(len(img)*0.571 + len(img[0])*0.063):int(len(img)*0.64 + len(img[0])*0.063), int(len(img[0])*0.37):int(len(img[0])*0.49)]
    option4 = img[int(len(img)*0.571 + len(img[0])*0.063):int(len(img)*0.64  + len(img[0])*0.063), int(len(img[0])*0.37 + len(img[0])*0.13):int(len(img[0])*0.49 + len(img[0])*0.13)]
    #cv2.imwrite('./option4.jpg', option4)
    question = ret_tess(question)
    option1 = ret_tess(option1)
    option2 = ret_tess(option2)
    option3 = ret_tess(option3)
    option4 = ret_tess(option4)
    return {'question': question, 'option1': option1, 'option2': option2, 'option3': option3, 'option4': option4}
    #print(data)