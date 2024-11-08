import tkinter
import cv2
import PIL.Image , PIL.ImageTk
from functools import partial
import threading
import imutils
import time
import pyttsx3
#for voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0])
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#for access video
stream=cv2.VideoCapture("VIDEO.mp4")
#setting width and height
SET_WIDTH=400
SET_HIGHT=400
flag=True
def play(speed):
    global flag
    #print(f"play speed is {speed}")
    frame1=stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1+speed)

    grabbed,frame=stream.read()
    if not grabbed:
      exit()
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,ancho=tkinter.NW,image=frame)
    if flag:
     canvas.create_text(130,30,fill="red",font="Times 20 bold",text=">>Decision Pending>>")
    flag= not flag

def pending(decision):
   frame=cv2.cvtColor(cv2.imread("DECISion.jpeg"),cv2.COLOR_BGR2RGB)
   frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HIGHT)
   frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
   canvas.image=frame
   canvas.create_image(0,0,ancho=tkinter.NW,image=frame)
   speak("decision pending")
   time.sleep(1.5)
    
   if decision =='out':
     decisionImg="OUT.jpeg"
     speak("out")
   else:
     decisionImg="NOT OUT.jpeg"
     speak("not out")
    
   frame=cv2.cvtColor(cv2.imread(decisionImg),cv2.COLOR_BGR2RGB)
   frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HIGHT)
   frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
   canvas.image=frame
   canvas.create_image(0,0,ancho=tkinter.NW,image=frame)


def out():
 thread=threading.Thread(target=pending,args=('out',))
 thread.daemon=1
 thread.start()
 print("out")

def not_out():
 thread=threading.Thread(target=pending,args=('not out',))
 thread.daemon=1
 thread.start()
 print("not out")

# SET_WIDTH=500
# SET_HIGHT=500

window=tkinter.Tk()
window.title("sujoy review system")
cv_img=cv2.cvtColor(cv2.imread("welcome.jpeg"),cv2.COLOR_BGR2RGB)
canvas=tkinter.Canvas(window,width=SET_WIDTH,height=SET_HIGHT)
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas=canvas.create_image(0,0,ancho=tkinter.NW,image=photo)
canvas.pack()

#button to control
btn=tkinter.Button(window,text="<< Previous(fast)",bg="pink",width=80,command=partial(play,-25))
btn.pack()
btn=tkinter.Button(window,text="<< Previous(slow)",bg="pink",width=80,command=partial(play,-2))
btn.pack()
btn=tkinter.Button(window,text="Next(fast)>>",bg="pink",width=80,command=partial(play,25))
btn.pack()
btn=tkinter.Button(window,text="Next(slow)>>",bg="pink",width=80,command=partial(play,2))
btn.pack()
btn=tkinter.Button(window,text="<< OUT >>",bg="pink",width=80,command=out)
btn.pack()
btn=tkinter.Button(window,text="<< NOT OUT >>",bg="pink",width=80,command=not_out)
btn.pack()

window.mainloop()