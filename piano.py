#PIANO PROJECT__________________________________________________________________
from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=1200,height=600, background='white')
drawpad.grid(row=0, column=1)

#bases
pianoBaseBlack = drawpad.create_rectangle(50,50,1150,550, fill= "black" )
keyboardBaseWhite = drawpad.create_rectangle(100,200,1100,500, fill= 'red')
waterMark = drawpad.create_rectangle(100,100,1100,150, fill= 'white')

#keys (WHITE KEYS: 50 wide)

# C
c = drawpad.create_rectangle(100,200,225,500, fill= 'white')
# C#
#cSharp = drawpad.create_rectangle(225,200,350,500, fill= 'white')
# D
d = drawpad.create_rectangle(225,200,350,500, fill= 'white')
# D#
#dSharp = drawpad.create_rectangle(475,200,600,500, fill= 'white')
# E
e = drawpad.create_rectangle(350,200,475,500, fill= 'white')
# F
f = drawpad.create_rectangle(475,200,600,500, fill= 'white')
# F#
#fSharp = drawpad.create_rectangle(850,200,975,500, fill= 'white')
# G
g = drawpad.create_rectangle(600,200,725,500, fill= 'white')
# G#
#gSharp = drawpad.create_rectangle(500,200,550,500, fill= 'white')
# A
a = drawpad.create_rectangle(725,200,850,500, fill= 'white')
# A#
#aSharp = drawpad.create_rectangle(600,200,650,500, fill= 'white')
# B
b = drawpad.create_rectangle(850,200,975,500, fill= 'white')
# C Octave
cOctave = drawpad.create_rectangle(975,200,1100,500, fill= 'white')
root.mainloop()


