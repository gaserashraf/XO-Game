import tkinter as tk
import tkinter.font as font
import sys;
import time
root= tk.Tk()
canvas1 = tk.Canvas(root, width = 340, height = 450)
canvas1.pack()
root.title('XO Game')
root.i = 0
root.x = 0
root.b=False
root.wi=False
root.eror=False
#global gaser
def NameOfplay():
    if root.x%2==0:
        root.x = root.x + 1
        n='x'
    else:
        root.x = root.x + 1
        n='o'
    global player
    player = tk.Label(root, text='Chose your position player '+ n)
    player.config(font=('helvetica', 10))
    canvas1.create_window(110, 370, window=player)
def whoPlay():
    if root.i%2==0:
        root.i = root.i + 1
        return 'x'
    else:
        root.i = root.i + 1
        return 'o'
def Error():
    global ThisPlace
    ThisPlace = tk.Label(root, text='Error!! This place Is already Token')
    ThisPlace.config(font=('helvetica', 10))
    canvas1.create_window(110, 400, window=ThisPlace)
    root.b=True
    root.eror=True
def WIN():
    global win
    win = tk.Label(root, text='Congrate  the player win is '+whoWin())
    win.config(font=('helvetica', 10))
    canvas1.create_window(110, 440, window=win)
    root.wi = True
NameOfplay()
def Reset():
    B11['text'] =''
    B12['text'] =''
    B13['text'] = ''
    B21['text'] = ''
    B22['text'] = ''
    B23['text'] = ''
    B31['text'] = ''
    B32['text'] = ''
    B33['text'] = ''
    root.i=0
    root.x= 0
    NameOfplay()
    if root.wi:
        win.destroy()
#helv36 = tkFont.Font(family='Helvetica', size=10, weight='bold')
def whoPlays11():
    if whoWin()==-1:
        if B11['text']!='o' and B11['text']!='x':
            if root.b == True:
                ThisPlace.destroy()
                root.b=False
            B11.config(text=whoPlay())
            if whoWin() != -1:
                WIN()
            else:
                player.destroy()
                NameOfplay()
        else:
            if root.b== False:
                Error()
    else:
        WIN()
def whoPlays12():
    if whoWin() == -1:
        if B12['text'] != 'o' and B12['text'] != 'x':
            if root.b == True:
                ThisPlace.destroy()
                root.b = False
            B12.config(text=whoPlay())
            if whoWin() != -1:
                WIN()
            else:
                player.destroy()
                NameOfplay()
        else:
            if root.b == False:
                Error()
    else:
        WIN()
def whoPlays13():
    if whoWin() == -1:
        if B13['text'] != 'o' and B13['text'] != 'x':
            if root.b == True:
                ThisPlace.destroy()
                root.b = False
            B13.config(text=whoPlay())
            if whoWin() != -1:
                WIN()
            else:
                player.destroy()
                NameOfplay()
        else:
            if root.b == False:
                Error()
    else:
        WIN()
def whoPlays21():
    if whoWin() == -1:
        if B21['text'] != 'o' and B21['text'] != 'x':
            if root.b == True:
                ThisPlace.destroy()
                root.b = False
            B21.config(text=whoPlay())
            if whoWin() != -1:
                WIN()
            else:
                player.destroy()
                NameOfplay()
        else:
            if root.b == False:
                Error()
    else:
        WIN()
def whoPlays22():
    if whoWin() == -1:
        if B22['text'] != 'o' and B22['text'] != 'x':
            if root.b == True:
                ThisPlace.destroy()
                root.b = False
            B22.config(text=whoPlay())
            if whoWin() != -1:
                WIN()
            else:
                player.destroy()
                NameOfplay()
        else:
            if root.b == False:
                Error()
    else:
        WIN()
def whoPlays23():
    if whoWin() == -1:
        if B23['text'] != 'o' and B23['text'] != 'x':
            if root.b == True:
                ThisPlace.destroy()
                root.b = False
            B23.config(text=whoPlay())
            if whoWin() != -1:
                WIN()
            else:
                player.destroy()
                NameOfplay()
        else:
            if root.b == False:
                Error()
    else:
        WIN()
def whoPlays31():
    if whoWin() == -1:
        if B31['text'] != 'o' and B31['text'] != 'x':
            if root.b == True:
                ThisPlace.destroy()
                root.b = False
            B31.config(text=whoPlay())
            if whoWin() != -1:
                WIN()
            else:
                player.destroy()
                NameOfplay()
        else:
            if root.b == False:
                Error()
    else:
        WIN()
def whoPlays32():
    if whoWin() == -1:
        if B32['text'] != 'o' and B32['text'] != 'x':
            if root.b == True:
                ThisPlace.destroy()
                root.b = False
            B32.config(text=whoPlay())
            if whoWin() != -1:
                WIN()
            else:
                player.destroy()
                NameOfplay()
        else:
            if root.b == False:
                Error()
    else:
        WIN()
def whoPlays33():
    if whoWin() == -1:
        if B33['text'] != 'o' and B33['text'] != 'x':
            if root.b == True:
                ThisPlace.destroy()
                root.b = False
            B33.config(text=whoPlay())
            if whoWin() != -1:
                WIN()
            else:
                player.destroy()
                NameOfplay()
        else:
            if root.b == False:
                Error()
    else:
        WIN()
def whoWin():
    if (B11['text']=='x'and B12['text']=='x'and B13['text']=='x') or(B21['text']=='x'and B22['text']=='x'and B23['text']=='x')or(B31['text']=='x'and B32['text']=='x'and B31['text']=='x'):
        return 'x'
    elif (B11['text']=='x'and B21['text']=='x'and B31['text']=='x') or(B12['text']=='x'and B22['text']=='x'and B32['text']=='x')or(B13['text']=='x'and B23['text']=='x'and B33['text']=='x'):
        return 'x'
    elif (B11['text']=='x'and B22['text']=='x'and B33['text']=='x') or(B13['text']=='x'and B22['text']=='x'and B31['text']=='x'):
        return 'x'
    if (B11['text']=='o'and B12['text']=='o'and B13['text']=='o') or(B21['text']=='o'and B22['text']=='o'and B23['text']=='o')or(B31['text']=='o'and B32['text']=='o'and B31['text']=='o'):
        return 'o'
    elif (B11['text']=='o'and B21['text']=='o'and B31['text']=='o') or(B12['text']=='o'and B22['text']=='o'and B32['text']=='o')or(B13['text']=='o'and B23['text']=='o'and B33['text']=='o'):
        return 'o'
    elif (B11['text']=='o'and B22['text']=='o'and B33['text']=='o') or(B13['text']=='o'and B22['text']=='o'and B31['text']=='o'):
        return 'o'
    else:
        return -1
B11=tk.Button(text='',command=whoPlays11,height=0,width=3,bd=5,bg="yellow",fg="black")
canvas1.create_window(58,58, window=B11)
myFont = font.Font(family='Helvetica',size=42)
B11['font'] = myFont
# create button
##button = Button(gui, text='My Button', fg='#ffffff')
# apply font to the button label
B12=tk.Button(text='',command=whoPlays12,height=1,width=3,bd=5,bg="yellow",fg="black")
canvas1.create_window(172,58, window=B12)
B12['font'] = myFont
B13=tk.Button(text='',command=whoPlays13,height=1,width=3,bd=5,bg="yellow",fg="black")
canvas1.create_window(287,58, window=B13)
B13['font'] = myFont
B21=tk.Button(text='',command=whoPlays21,height=0,width=3,bd=5,bg="yellow",fg="black")
canvas1.create_window(58,178, window=B21)
B21['font'] = myFont
B22=tk.Button(text='',command=whoPlays22,height=1,width=3,bd=5,bg="yellow",fg="black")
canvas1.create_window(172,178, window=B22)
B22['font'] = myFont
B23=tk.Button(text='',command=whoPlays23,height=1,width=3,bd=5,bg="yellow",fg="black")
canvas1.create_window(287,178, window=B23)
B23['font'] = myFont
B31=tk.Button(text='',command=whoPlays31,height=0,width=3,bd=5,bg="yellow",fg="black")
canvas1.create_window(58,298, window=B31)
B31['font'] = myFont
B32=tk.Button(text='',command=whoPlays32,height=1,width=3,bd=5,bg="yellow",fg="black")
canvas1.create_window(172,298, window=B32)
B32['font'] = myFont
B33=tk.Button(text='',command=whoPlays33,height=1,width=3,bd=5,bg="yellow",fg="black")
canvas1.create_window(287,298, window=B33)
B33['font'] = myFont
BnewGame=tk.Button(text='New Game',command=Reset)
canvas1.create_window(300,380, window=BnewGame)
root.mainloop()