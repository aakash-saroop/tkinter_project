from tkinter import *
from PIL import ImageTk, Image
import cv2
import numpy as np
import tensorflow as tf
loaded_model = tf.keras.models.load_model('/Users/aakashsaroop/Desktop/face-flask/model (3) (1).h5')

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

Fact = "The emotion will be displayed here"
T.insert("1.0",Fact)
T.grid()
T.place(anchor = NW)

def predict():
    newsize = (48, 48)
    test_img = face[-1].resize(newsize)
    test_img = test_img.convert('LA')
    # getting the pixel values from the image
    tuple_data = list(test_img.getdata())

    data = []
    for tuple in tuple_data:
        data.append(tuple[0])

    #reshaping the pixel values to make it compatible with the model
    pixel_matrix = np.array(data).reshape(1, 48, 48, 1)
    pixel_matrix = pixel_matrix/255
    print(pixel_matrix.shape)
    yhat_test = loaded_model.predict_classes(pixel_matrix)
    # displaying the output on the webpage
    if (yhat_test==0):
        return'The person in this image appears to be angry.'
    elif (yhat_test==1):
        return 'The person in this image appears to be happy.</h1>'

    elif (yhat_test==2):
        return 'The person in this image appears to be sad.'

    else: # yhat_test==3
        return 'The person in this image appears to be surprised.'
def emotion():
    #root.geometry("500x500")

    root.title("emotion")

    T.delete("1.0",END)
    Emotion = predict()
    T.insert("1.0", Emotion)
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
