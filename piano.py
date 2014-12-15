#PIANO PROJECT__________________________________________________________________
import winsound, sys
from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=1200,height=600, background='white')

#bases
pianoBaseBlack = drawpad.create_rectangle(50,50,1150,550, fill= "black" )
keyboardBaseWhite = drawpad.create_rectangle(100,200,1100,500, fill= 'red')
waterMark = drawpad.create_rectangle(100,100,1100,150, fill= 'white')

#keys (WHITE KEYS: 50 wide)

# C
c = drawpad.create_rectangle(100,200,225,500, fill= 'white')
# D
d = drawpad.create_rectangle(225,200,350,500, fill= 'white')
# E
e = drawpad.create_rectangle(350,200,475,500, fill= 'white')
# F
f = drawpad.create_rectangle(475,200,600,500, fill= 'white')
# G
g = drawpad.create_rectangle(600,200,725,500, fill= 'white')
# A
a = drawpad.create_rectangle(725,200,850,500, fill= 'white')
# B
b = drawpad.create_rectangle(850,200,975,500, fill= 'white')
# C Octave
cOctave = drawpad.create_rectangle(975,200,1100,500, fill= 'white')
# C#
cSharp = drawpad.create_rectangle(193.75,200,256.25,350, fill= 'black')
# D#
dSharp = drawpad.create_rectangle(318.75,200,381.25,350, fill= 'black')
# F#
fSharp = drawpad.create_rectangle(568.75,200,631.25,350, fill= 'black')
# G#
gSharp = drawpad.create_rectangle(693.75,200,756.25,350, fill= 'black')
# A#
aSharp = drawpad.create_rectangle(818.75,200,881.25,350, fill= 'black')

waterMarkText = drawpad.create_text(600,125, fill= 'black', text= 'Python Piano - By Chris Lee, Mason Confer, and Joe Torres. (c) 2014')

#control text
class myApp(object):
    def __init__(self, parent):
        drawpad.pack()
        root.bind_all('<Key>', self.key)
    
    def key(self,event):
         global c
         global drawpad
         if event.char == "a":
             drawpad.itemconfig(c, fill= "black")
             root.update_idletasks()
             winsound.PlaySound('H:\CompSci\Piano\Piano-Project\Piano Tones\C.wav',winsound.SND_FILENAME)
             drawpad.itemconfig(c, fill= "white")
         if event.char == "s":
             drawpad.itemconfig(d, fill= "black")
             root.update_idletasks()
             winsound.PlaySound('H:\CompSci\Piano\Piano-Project\Piano Tones\D.wav',winsound.SND_FILENAME)
             drawpad.itemconfig(d, fill= "white")
         if event.char == "d":
             drawpad.itemconfig(e, fill= "black")
             root.update_idletasks()
             winsound.PlaySound('H:\CompSci\Piano\Piano-Project\Piano Tones\E.wav',winsound.SND_FILENAME)
             drawpad.itemconfig(e, fill= "white")
         if event.char == "f":
             drawpad.itemconfig(f, fill= "black")
             root.update_idletasks()
             winsound.PlaySound('H:\CompSci\Piano\Piano-Project\Piano Tones\F.wav',winsound.SND_FILENAME)
             drawpad.itemconfig(f, fill= "white")
         if event.char == "g":
             drawpad.itemconfig(g, fill= "black")
             root.update_idletasks()
             winsound.PlaySound('H:\CompSci\Piano\Piano-Project\Piano Tones\G.wav',winsound.SND_FILENAME)
             drawpad.itemconfig(g, fill= "white")
         if event.char == "h":
             drawpad.itemconfig(a, fill= "black")
             root.update_idletasks()
             winsound.PlaySound('H:\CompSci\Piano\Piano-Project\Piano Tones\A2.wav',winsound.SND_FILENAME)
             drawpad.itemconfig(a, fill= "white")
         if event.char == "j":
             drawpad.itemconfig(b, fill= "black")
             root.update_idletasks()
             winsound.PlaySound('H:\CompSci\Piano\Piano-Project\Piano Tones\B2.wav',winsound.SND_FILENAME)
             drawpad.itemconfig(b, fill= "white")
         if event.char == "k":
             drawpad.itemconfig(cOctave, fill= "black")
             root.update_idletasks()
             winsound.PlaySound('H:\CompSci\Piano\Piano-Project\Piano Tones\C2.wav',winsound.SND_FILENAME)
             drawpad.itemconfig(cOctave, fill= "white")
         if event.char == "q":
             drawpad.itemconfig(cSharp, fill= "white")
             root.update_idletasks()
             winsound.PlaySound('H:\CompSci\Piano\Piano-Project\Piano Tones\C#.wav',winsound.SND_FILENAME)
             drawpad.itemconfig(cSharp, fill= "black")
         if event.char == "w":
             drawpad.itemconfig(dSharp, fill= "white")
             root.update_idletasks()
             winsound.PlaySound('H:\CompSci\Piano\Piano-Project\Piano Tones\D#.wav',winsound.SND_FILENAME)
             drawpad.itemconfig(dSharp, fill= "black")
         if event.char == "r":
             drawpad.itemconfig(fSharp, fill= "white")
             root.update_idletasks()
             winsound.PlaySound('H:\CompSci\Piano\Piano-Project\Piano Tones\F#.wav',winsound.SND_FILENAME)
             drawpad.itemconfig(fSharp, fill= "black")
         if event.char == "t":
             drawpad.itemconfig(gSharp, fill= "white")
             root.update_idletasks()
             winsound.PlaySound('H:\CompSci\Piano\Piano-Project\Piano Tones\G#.wav',winsound.SND_FILENAME)
             drawpad.itemconfig(gSharp, fill= "black")
         if event.char == "y":
             drawpad.itemconfig(aSharp, fill= "white")
             root.update_idletasks()
             winsound.PlaySound('H:\CompSci\Piano\Piano-Project\Piano Tones\A#2.wav',winsound.SND_FILENAME)
             drawpad.itemconfig(aSharp, fill= "black")
              
             
app = myApp(root)
root.mainloop()