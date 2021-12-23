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
diamond =tk.PhotoImage(file="image/diamond.png")
congrats = tk.PhotoImage(file='image/congrats.png')

grid = [
    [0,6,4,2,0,5,0,0,0,0,0],
    [6,0,0,5,2,0,0,0,0,0,0],
    [0,6,6,6,0,0,0,0,0,0,0],
    [0,2,1,2,6,0,0,0,0,0,0],
    [0,6,6,6,0,5,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,6,4,2,0,5,0,0,0,0,0],
    [6,0,0,5,2,0,0,0,0,0,0],
    [0,6,6,6,0,0,0,0,0,0,0],
    [0,6,4,2,0,5,0,0,0,0,0],

]

countScore = 0
hasKey = False
hasNoKey = False
arrivedHome = False
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
    

    if hasNoKey:
        textKey = canvas.create_text(300,70,text='You has no key, you need to find key!',font=('Ubuntu',18))
    if hasKey and not hasNoKey:
        textKey = canvas.create_text(300,70,text='You has key, you can go home now!',font=('Ubuntu',18))
    if hasNoKey and not hasKey:
        textKey = canvas.create_text(300,70,text='You has no key, you need to find key!',font=('Ubuntu',18))
    if hasNoKey and hasKey:
        canvas.itemconfig(textKey,text='You has key, you can go home now!')
    if hasKey:
        textKey = canvas.create_text(300,70,text='You has key, you can go home now!',font=('Ubuntu',18))

    
    x=35
    y=80
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 0:
                canvas.create_rectangle(x,y,x+50,y+50,fill='',outline='')
            elif grid[row][col] == 1:
                canvas.create_image(x+30,y+30,image = avatar,anchor='center')   
            elif grid[row][col] == 2:
                canvas.create_image(x+30,y+30,image = monster,anchor='center')      
            elif grid[row][col] == 3:
                canvas.create_image(x+30,y+30,image = home,anchor='center')
            elif grid[row][col] == 4:
                canvas.create_image(x+30,y+30,image = key,anchor='center')  
            elif grid[row][col] == 5:
                canvas.create_image(x+30,y+30,image = diamond,anchor='center') 
            elif grid[row][col]== 6:
                canvas.create_image(x+30,y+30,image= stair,anchor='center')           
            x+=50
        x=35
        y+=50

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
    global countScore, hasKey,textkey,lives,hasNoKey,arrivedHome
    row = getRowOf1()
    col = getColOf1()
    if col != 0 :
        if col != 0 and grid[row][col-1] != 6 and row < len(grid)-1:
            if grid[row+1][col] == 6 and grid[row+1][col-1] == 6:
                currentValue = grid[row][col-1]
                grid[row][col] = 0
                grid[row][col-1]=1
                if currentValue == 5:
                    countScore += 10
                    winsound .PlaySound('sound/coin.wav', winsound.SND_FILENAME)
                elif currentValue == 4:
                    hasKey = True
                elif currentValue == 3 and hasKey:
                    arrivedHome = True
                    winsound .PlaySound('sound/win.wav', winsound.SND_FILENAME)
                    messagebox.showinfo("Congrats","You Win!")
                elif currentValue == 3 and not hasKey:
                    grid[row][col]=1
                    grid[row][col-1] = 3
                    hasNoKey = True
                elif currentValue == 2:
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
    global countScore, hasKey,textkey,lives,hasNoKey,arrivedHome
    row = getRowOf1()
    col = getColOf1()
    if col < len(grid[0])-1 and grid[row][col+1] != 6 and row < len(grid)-1:
        if grid[row+1][col] == 6 and grid[row+1][col+1] == 6:
            currentValue = grid[row][col+1]
            grid[row][col] = 0
            grid[row][col+1]=1
            if currentValue == 5:
                countScore += 10
                winsound .PlaySound('sound/coin.wav', winsound.SND_FILENAME)
            elif currentValue == 4:
                hasKey = True
            elif currentValue == 3 and hasKey:
                arrivedHome = True
                winsound .PlaySound('sound/win.wav', winsound.SND_FILENAME)
                messagebox.showinfo("Win","You Win!")
            elif currentValue == 3 and not hasKey:
                    grid[row][col]=1
                    grid[row][col+1] = 3
                    hasNoKey = True
            elif currentValue == 2:
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
    global countScore, hasKey,textkey,lives,hasNoKey,arrivedHome
    row = getRowOf1()
    col = getColOf1()
    
    if row < len(grid)-1 and grid[row+1][col] != 6 and col < len(grid[0])-1:
        if grid[row][col-1] == 6 and grid[row+1][col-1] == 6:
            currentValue = grid[row+1][col]
            grid[row][col] = 0
            grid[row+1][col]=1
            if currentValue == 5:
                countScore += 10
                winsound .PlaySound('sound/coin.wav', winsound.SND_FILENAME)
            elif currentValue == 4:
                hasKey = True
            elif currentValue == 3 and hasKey:
                arrivedHome = True
                winsound .PlaySound('sound/win.wav', winsound.SND_FILENAME)
                messagebox.showinfo("Win","You Win!")
            elif currentValue == 3 and not hasKey:
                    grid[row][col] = 1
                    grid[row+1][col] = 3
                    hasNoKey = True
            elif currentValue == 2:
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
    global countScore, hasKey,textkey,lives,hasNoKey,arrivedHome
    row = getRowOf1()
    col = getColOf1()
    if row != 0 and grid[row-1][col] != 6 and col < len(grid[0])-1:
        if grid[row][col-1] == 6 and grid[row+1][col+1] == 6:
            currentValue = grid[row-1][col]
            grid[row][col] = 0
            grid[row-1][col]=1
            if currentValue == 5:
                countScore += 10
                winsound .PlaySound('sound/coin.wav', winsound.SND_FILENAME)
            elif currentValue == 4:
                hasKey = True
            elif currentValue == 3 and hasKey:
                arrivedHome = True
                winsound .PlaySound('sound/win.wav', winsound.SND_FILENAME)
                messagebox.showinfo("Win","You Win!")     
            elif currentValue == 3 and not hasKey:
                    grid[row][col] =1
                    grid[row-1][col] = 3
                    hasNoKey = True
            elif currentValue == 2:
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