from tkinter import *
from PIL import ImageTk, Image
import cv2
import numpy as np

root = Tk()
# Create a frame
app = Frame(root, bg="white")
app.grid()
# Create a label in the frame

lmain = Label(app)
# Create text widget and specify size.
T = Text(root, height = 5, width = 52)

# Create label
l = Label(root, text = "Fact of the Day")
l.config(font =("Courier", 14))

Fact = "Emotion will be displayed here"
T.insert("1.0",Fact)
T.grid()
T.place(anchor = NW)
def emotion():
    #root.geometry("500x500")
    root.title("emotion")
b = Button(root, text = "Get emotion", command=emotion)
b.place(anchor = CENTER)
b.grid()
lmain.grid()

# Capture from camera
cap = cv2.VideoCapture(0)

# function for video streaming
face = []
i = 0

def video_stream():

    _, frame = cap.read()

    frame=cv2.flip(frame,1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    '''try:
        print(type(face[0]))
    except:
        print(0)'''
    img = Image.fromarray(cv2image)
    face.append(img)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, video_stream)


video_stream()
root.mainloop()
