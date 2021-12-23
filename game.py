import tkinter as tk
from tkinter import messagebox
import winsound
root = tk.Tk() 
root.geometry("610x610")
frame = tk.Frame()
frame.master.title('Amazing game')
canvas = tk.Canvas(frame)

myBackground=tk.PhotoImage(file='image/backg.png')
avatar = tk.PhotoImage(file='image/avatar.png')
monster = tk.PhotoImage(file='image/monster.png')
home = tk.PhotoImage(file='image/home.png')
key = tk.PhotoImage(file='image/key.png')
stair=tk.PhotoImage(file="image/stair.png")
heart_image=tk.PhotoImage(file="image/heart.png")
diamond =tk.PhotoImage(file="image/dimond.png")
congrats = tk.PhotoImage(file='image/congrats.png')

grid = [
    [0,0,4,2,0,5],
    [0,0,4,5,2,0],
    [0,2,5,2,5,0],
    [0,5,2,0,0,5],
    [6,6,6,6,6,6],
    [0,1,0,3,0,0],
]

countScore = 0
hasKey = False
lives = 3
def drawGrid():
    canvas.delete('all')
    canvas.create_image(210,310, image=myBackground)
    
    canvas.create_text(250,30,text='Lives: ',font=('Ubuntu',18))

    heart1 = canvas.create_image(300,30,image=heart_image)
    heart2 = canvas.create_image(340,30,image=heart_image)
    heart3 = canvas.create_image(380,30,image=heart_image)

    canvas.create_text(540,30,text='Levels: 1 ',font=('Ubuntu',18))


    canvas.create_text(70,30,text='Score: ' + str(countScore),font=('Ubuntu',18))

    if hasKey:
        textKey = canvas.create_text(300,70,text='You has key',font=('Ubuntu',18))
        canvas.after(60,textKey)

    x=35
    y=80
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 0:
                canvas.create_rectangle(x,y,x+90,y+90,fill='',outline='')
            elif grid[row][col] == 1:
                canvas.create_image(x+45,y+45,image = avatar,anchor='center')   
            elif grid[row][col] == 2:
                canvas.create_image(x+45,y+45,image = monster,anchor='center')      
            elif grid[row][col] == 3:
                canvas.create_image(x+45,y+45,image = home,anchor='center')
            elif grid[row][col] == 4:
                canvas.create_image(x+45,y+45,image = key,anchor='center')  
            elif grid[row][col] == 5:
                canvas.create_image(x+45,y+45,image = diamond,anchor='center') 
            elif grid[row][col]== 6:
                canvas.create_image(x+45,y,image= stair,anchor='center')           
            x+=90
        x=35
        y+=90

drawGrid()

def getRowOf1():
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                index = row
    return index

def getColOf1():
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                index = col
    return index

def move_left(event):
    global countScore, hasKey,textkey,lives
    row = getRowOf1()
    col = getColOf1()

    if col != 0 and grid[row][col-1] != 3 and grid[row][col-1] != 2:
        if col != 0:
            oldValue = grid[row][col-1]
            grid[row][col] = 0
            grid[row][col-1]=1
            if oldValue == 5:
                countScore += 10
                winsound .PlaySound('sound/coin.wav', winsound.SND_FILENAME)
            elif oldValue == 4:
                hasKey = True
                
            elif oldValue == 3 and hasKey:
                winsound .PlaySound('sound/win.wav', winsound.SND_FILENAME)
                messagebox.showinfo("Congrats","You Win!")
            elif oldValue == 3 and not hasKey:
                oldValue = 3
                
            elif oldValue == 2:
                lives -= 1
                if lives == 2:
                    canvas.delete('heart1')
                elif lives == 1:
                    canvas.delete('heart2')
                elif lives == 0:
                    winsound .PlaySound('sound/lost.wav', winsound.SND_FILENAME)
                    messagebox.showinfo("Lost","You Lost!")
    drawGrid()
def move_right(event):
    global countScore, hasKey,textkey,lives
    row = getRowOf1()
    col = getColOf1()
    if col < len(grid[0])-1 and grid[row][col+1] != 3 and grid[row][col+1] != 2:
        oldValue = grid[row][col+1]
        grid[row][col] = 0
        grid[row][col+1]=1
        if oldValue == 5:
            countScore += 10
            winsound .PlaySound('sound/coin.wav', winsound.SND_FILENAME)
        elif oldValue == 4:
            hasKey = True
        elif oldValue == 3 and hasKey:
            winsound .PlaySound('sound/win.wav', winsound.SND_FILENAME)
            messagebox.showinfo("Win","You Win!")
        elif oldValue == 2:
            lives -= 1
            if lives == 2:
                canvas.delete('heart1')
            elif lives == 1:
                canvas.delete('heart2')
            elif lives == 0:
                winsound .PlaySound('sound/lost.wav', winsound.SND_FILENAME)
                messagebox.showinfo("Lost","You Lost!")
    drawGrid()

def move_down(event):
    global countScore, hasKey,textkey,lives
    row = getRowOf1()
    col = getColOf1()
    
    if row < len(grid)-1 and grid[row+1][col] != 3 and grid[row+1][col] != 2:
        oldValue = grid[row+1][col]
        grid[row][col] = 0
        grid[row+1][col]=1
        if oldValue == 5:
            countScore += 10
            winsound .PlaySound('sound/coin.wav', winsound.SND_FILENAME)
        elif oldValue == 4:
            hasKey = True
        elif oldValue == 3 and hasKey:
            winsound .PlaySound('sound/win.wav', winsound.SND_FILENAME)
            messagebox.showinfo("Win","You Win!")
        elif oldValue == 2:
            lives -= 1
            if lives == 2:
                canvas.delete('heart1')
            elif lives == 1:
                canvas.delete('heart2')
            elif lives == 0:
                winsound .PlaySound('sound/lost.wav', winsound.SND_FILENAME)
                messagebox.showinfo("Lost","You Lost!")
    drawGrid()

def move_up(event):
    global countScore, hasKey,textkey,lives
    row = getRowOf1()
    col = getColOf1()
    if row != 0 and grid[row-1][col] != 3 and grid[row-1][col] != 2:
        oldValue = grid[row-1][col]
        grid[row][col] = 0
        grid[row-1][col]=1
        if oldValue == 5:
            countScore += 10
            winsound .PlaySound('sound/coin.wav', winsound.SND_FILENAME)
        elif oldValue == 4:
            hasKey = True
        elif oldValue == 3 and hasKey:
            winsound .PlaySound('sound/win.wav', winsound.SND_FILENAME)
            messagebox.showinfo("Win","You Win!")     
        elif oldValue == 2:
            lives -= 1
            if lives == 2:
                canvas.delete('heart1')
            elif lives == 1:
                canvas.delete('heart2')
            elif lives == 0:
                winsound .PlaySound('sound/lost.wav', winsound.SND_FILENAME)
                messagebox.showinfo("Lost","You Lost!")
    drawGrid()

root.bind('<Left>',move_left) #### keyboard
root.bind('<Right>',move_right) #### keyboard
root.bind('<Down>',move_down) #### keyboard
root.bind('<Up>',move_up) #### keyboard

canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')

root.mainloop()