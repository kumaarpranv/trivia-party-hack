import cv2
import keyboard

img = cv2.imread("D:/code/snapchat-message-bot/image.png", cv2.IMREAD_UNCHANGED)
while True:
    if keyboard.is_pressed("q"):
        break
    cv2.imshow('image', img)