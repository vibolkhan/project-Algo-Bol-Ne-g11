import tkinter as tk
from tkinter import messagebox
import winsound
root = tk.Tk() 
root.geometry("770x650")
frame = tk.Frame()
frame.master.title('Amazing game')
canvas = tk.Canvas(frame)
root.resizable(0,0)
 

myBackground=tk.PhotoImage(file='image/backg.png')
avatar = tk.PhotoImage(file='image/avatar.png')
monster = tk.PhotoImage(file='image/monster.png')
home = tk.PhotoImage(file='image/home.png')
key = tk.PhotoImage(file='image/key.png')
wall=tk.PhotoImage(file="image/wall.png")
heart_image=tk.PhotoImage(file="image/heart.png")
diamond =tk.PhotoImage(file="image/diamond.png")
congrats = tk.PhotoImage(file='image/congrats.png')

# ---------------------------------------
# CONSTANTS
EMPTY_CELL = 0
PLAYER_CELL = 1
MONSTER_CELL = 2 
HOME_CELL = 3
KEY_CELL = 4
DIAMOND_CELL = 5
WALL_CELL = 6
# ---------------------------------------

# ---------------------------------------
# VARIABLES
lives = 3
score = 0
# ---------------------------------------

# -------------------------------------------
#Boolean
hasKey = False
hasNoKey = False
end = False
# -------------------------------------------
grid = [
    [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6],
    [6,2,0,0,0,0,0,0,0,6,5,0,0,6,0,0,0,0,0,0,6,0,0,5,6],
    [6,6,0,6,6,0,6,6,6,6,0,6,0,6,6,6,0,0,0,0,6,0,0,5,6],
    [6,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,5,6],
    [6,0,4,0,0,0,0,0,0,6,6,6,6,6,6,6,0,6,6,6,6,0,6,0,6],
    [6,0,6,6,6,0,0,5,0,0,0,5,6,0,0,0,0,0,0,0,6,0,6,0,6],
    [6,0,0,0,0,0,0,6,0,0,0,0,6,0,0,0,0,6,0,0,6,0,0,0,6],
    [6,6,6,6,0,6,2,6,0,0,0,5,6,0,0,0,0,6,0,0,6,0,0,0,6],
    [6,0,0,0,0,6,0,6,0,0,0,0,0,0,0,0,0,6,0,0,6,6,6,0,6],
    [6,0,6,6,6,6,5,6,6,6,6,0,1,0,6,6,6,6,0,0,0,0,0,0,6],
    [6,0,0,0,0,0,0,6,0,0,5,0,0,0,0,0,0,6,0,0,6,0,0,0,6],
    [6,0,6,6,6,6,0,6,0,0,5,0,6,0,0,0,0,6,0,0,6,0,6,0,6],
    [6,0,0,0,0,6,0,6,0,0,0,0,6,0,0,0,0,6,0,0,6,0,6,0,6],
    [6,0,6,6,0,6,0,0,0,0,5,0,6,0,0,0,0,0,0,0,6,0,6,0,6],
    [6,0,6,6,0,6,0,0,0,6,6,6,6,6,6,6,0,6,6,6,6,0,0,0,6],
    [6,0,5,2,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,6],
    [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6],

]    

heart1 = canvas.create_image(380,30,image=heart_image)
heart2 = canvas.create_image(420,30,image=heart_image)
heart3 = canvas.create_image(460,30,image=heart_image)

def drawGrid():
    canvas.delete('all')
    canvas.create_image(380,320, image=myBackground)
    canvas.create_text(330,30,text='Lives: ',font=('Ubuntu',18))



    canvas.create_text(620,30,text='Levels: 1 ',font=('Ubuntu',18))

    canvas.create_text(150,30,text='Score: ' + str(score),font=('Ubuntu',18))

    if hasNoKey:
        textKey = canvas.create_text(380,70,text='You has no key, you need to find key!',font=('Ubuntu',18))
    if hasKey and not hasNoKey:
        textKey = canvas.create_text(380,70,text='You has key, you can go home now!',font=('Ubuntu',18))
    if hasNoKey and hasKey:
        canvas.itemconfig(textKey,text='You has key, you can go home now!')
    if hasKey:
        textKey = canvas.create_text(380,70,text='You has key, you can go home now!',font=('Ubuntu',18))

    
    x=10
    y=100
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 0:
                canvas.create_rectangle(x,y,x+30,y+30,fill='')
            elif grid[row][col] == 1:
                canvas.create_image(x+15,y+15,image = avatar,anchor='center')   
            elif grid[row][col] == 2:
                canvas.create_image(x+15,y+15,image = monster,anchor='center')      
            elif grid[row][col] == 3:
                canvas.create_image(x+15,y+15,image = home,anchor='center')
            elif grid[row][col] == 4:
                canvas.create_image(x+15,y+15,image = key,anchor='center')  
            elif grid[row][col] == 5:
                canvas.create_image(x+15,y+15,image = diamond,anchor='center') 
            elif grid[row][col]== 6:
                canvas.create_image(x+15,y+15,image= wall,anchor='center')           
            x+=30
        x=10
        y+=30

drawGrid()

def getPlayerY():
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                index = row
    return index

def getPlayerX():
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                index = col
    return index

# move
def move(moveX, moveY) :
    global lives,score,hasNoKey,hasKey,end
    playerX = getPlayerX()
    playerY = getPlayerY()
    newPlayerX = playerX + moveX
    newPlayerY = playerY + moveY 
    if grid[newPlayerY][newPlayerX] != WALL_CELL :
        if grid[newPlayerY][newPlayerX] == DIAMOND_CELL: # count score
                score += 10 
                winsound .PlaySound('sound/coin.wav', winsound.SND_FILENAME)

        if grid[newPlayerY][newPlayerX] == MONSTER_CELL: # count lives
            lives -= 1
            winsound .PlaySound('sound/lost.wav', winsound.SND_FILENAME)
            if lives == 0:
                messagebox.showinfo("Lost","You Lost this game!")
        if moveX == 1 and moveY == 0: # move right
            if grid[newPlayerY][newPlayerX] == KEY_CELL:
                hasKey = True
            if grid[newPlayerY][newPlayerX] == HOME_CELL and hasKey:
                winsound .PlaySound('sound/win.wav', winsound.SND_FILENAME)
                messagebox.showinfo("Congrats","You Win!")
            if grid[newPlayerY][newPlayerX] == HOME_CELL and not hasKey: # get key
                grid[playerY][playerX] = PLAYER_CELL
                grid[newPlayerY][newPlayerX] = HOME_CELL
                hasNoKey = True
            elif newPlayerX < len(grid[0]):
                grid[playerY][playerX] = EMPTY_CELL
                grid[newPlayerY][newPlayerX] = PLAYER_CELL
                
        elif moveX == -1 and moveY == 0: # move left
            if grid[newPlayerY][newPlayerX] == KEY_CELL:
                hasKey = True
            if grid[newPlayerY][newPlayerX] == HOME_CELL and hasKey:
                winsound .PlaySound('sound/win.wav', winsound.SND_FILENAME)
                messagebox.showinfo("Congrats","You Win!")
            if grid[newPlayerY][newPlayerX] == HOME_CELL and not hasKey: # get key
                grid[playerY][playerX] = PLAYER_CELL
                grid[newPlayerY][newPlayerX] = HOME_CELL
                hasNoKey = True
            elif newPlayerX >= 0:
                grid[playerY][playerX] = EMPTY_CELL
                grid[newPlayerY][newPlayerX] = PLAYER_CELL

        elif moveX == 0 and moveY == 1: # move down
            if grid[newPlayerY][newPlayerX] == KEY_CELL:
                hasKey = True
            if grid[newPlayerY][newPlayerX] == HOME_CELL and hasKey:
                winsound .PlaySound('sound/win.wav', winsound.SND_FILENAME)
                messagebox.showinfo("Congrats","You Win!")
            if grid[newPlayerY][newPlayerX] == HOME_CELL and not hasKey: # get key
                grid[playerY][playerX] = PLAYER_CELL
                grid[newPlayerY][newPlayerX] = HOME_CELL
                hasNoKey = True
            elif newPlayerY < len(grid):
                grid[playerY][playerX] = EMPTY_CELL
                grid[newPlayerY][newPlayerX] = PLAYER_CELL

        elif moveX == 0 and moveY == -1: #move up
            if grid[newPlayerY][newPlayerX] == KEY_CELL:
                hasKey = True
            if grid[newPlayerY][newPlayerX] == HOME_CELL and hasKey:
                winsound .PlaySound('sound/win.wav', winsound.SND_FILENAME)
                messagebox.showinfo("Congrats","You Win!")
            if grid[newPlayerY][newPlayerX] == HOME_CELL and not hasKey: # get key
                grid[playerY][playerX] = PLAYER_CELL
                grid[newPlayerY][newPlayerX] = HOME_CELL
                hasNoKey = True
            elif newPlayerY >= 0:
                grid[playerY][playerX] = EMPTY_CELL
                grid[newPlayerY][newPlayerX] = PLAYER_CELL
    
    drawGrid()

# --------------------------------------
# MOVE POSITION
def move_right(event):
    move(1,0)
def move_left(event):
    move(-1,0)
def move_down(event):
    move(0,1)
def move_up(event):
    move(0,-1)
# --------------------------------------

# click on key board
root.bind('<Left>',move_left) #### keyboard
root.bind('<Right>',move_right) #### keyboard
root.bind('<Down>',move_down) #### keyboard
root.bind('<Up>',move_up) #### keyboard

# display all
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.mainloop()