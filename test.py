from math import trunc
import tkinter as tk
from tkinter import PhotoImage, messagebox
from tkinter import font
import winsound
import random
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
lostGame = tk.PhotoImage(file='image/gameover.png')
empty_heart = tk.PhotoImage(file='image/empty-heart.png')
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
tomove=[]
# ---------------------------------------

# -------------------------------------------
#Boolean
hasKey = False
hasNoKey = False
end = False
# -------------------------------------------
grid = [
    [6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6],
    [6 ,0 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,5 ,5 ,5, 6, 5, 5,0 ,6 ],
    [6 ,6 ,0 ,6 ,6 ,5 ,6 ,6 ,6 ,6 ,5 ,6 ,0 ,6 ,6 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,3 ,5 ,6],
    [6 ,5 ,5 ,5 ,5 ,0 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,0 ,5 ,5 ,5 ,5 ,5 ,6, 5, 6],
    [6 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,6 ,6 ,6 ,6 ,6 , 6 ,5 ,6 ,6 ,6 ,6 ,5 ,6 ,5 ,6],
    [6 ,5 ,6 ,6 ,6 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,6 ,5 ,6],
    [6 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,6 ,5 ,5 ,5 ,6],
    [6 ,5 ,6 ,6 ,5 ,6 ,0 ,6 ,5 ,5 ,5 ,5 ,6 ,2 ,0 ,5 ,5 ,6 ,5 ,5 ,6 ,0 ,5 ,5 ,6],
    [6,5,5,5,5,6,5,6,5,5,5,5,5,5,5,5,5,6,5,5,6,6,6,5,6],
    [6,5,6,6,6,6,5,6,6,6,6,5,1,5,6,6,6,6,5,5,0,5,5,5,6],
    [6,5,5,0,5,5,5,6,5,5,5,5,5,5,5,5,5,6,5,5,6,5,5,5,6],
    [6,5,6,6,6,6,5,6,5,0,5,5,6,5,5,5,5,6,5,5,6,5,6,5,6],
    [6,5,5,5,5,6,5,6,5,5,5,5,6,5,5,5,5,6,5,5,6,5,6,5,6],
    [6,5,6,6,5,6,5,5,5,5,5,5,6,5,5,5,5,5,5,5,6,5,6,5,6],
    [6,5,6,6,5,6,5,5,5,6,6,6,6,6,6,6,5,6,6,6,6,5,5,5,6],
    [6,4,5,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6],
    [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6],

]    

def drawGrid():
    # canvas.delete('all')
    canvas.create_image(380,320, image=myBackground)
    canvas.create_text(330,30,text='Lives: ',font=('Ubuntu',18))
    heart1=canvas.create_image(380,30,image=heart_image)
    heart2=canvas.create_image(420,30,image=heart_image)
    heart3=canvas.create_image(460,30,image=heart_image)
    
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

    if lives == 2:
        canvas.move(heart3,-50,-50)
    if lives == 1:
        canvas.move(heart2,-50,-50)
    if lives == 0:
        canvas.move(heart1,-50,-50)
    x=10
    y=100
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == EMPTY_CELL:
                canvas.create_rectangle(x,y,x+30,y+30,fill='',outline='')
            elif grid[row][col] == PLAYER_CELL:
                canvas.create_image(x+15,y+15,image = avatar,anchor='center')   
            elif grid[row][col] == MONSTER_CELL:
                canvas.create_image(x+15,y+15,image = monster,anchor='center')      
            elif grid[row][col] == HOME_CELL:
                canvas.create_image(x+15,y+15,image = home,anchor='center')
            elif grid[row][col] == KEY_CELL:
                canvas.create_image(x+15,y+15,image = key,anchor='center')  
            elif grid[row][col] == DIAMOND_CELL:
                canvas.create_image(x+15,y+15,image = diamond,anchor='center') 
            elif grid[row][col]== WALL_CELL:
                canvas.create_image(x+15,y+15,image= wall,anchor='center')           
            x+=30
        x=10
        y+=30

drawGrid()

# ----------------------------------move monster

def getMonster(grid):
    indexEnemy = []
    for row in range (len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == MONSTER_CELL:
                indexEnemy.append([row, col])
    return indexEnemy

def moveInGrid(grid,monsterY,monsterX):
    moveMonster = []
    if (grid[monsterY][monsterX-1] == DIAMOND_CELL or grid[monsterY][monsterX-1] == EMPTY_CELL or grid[monsterY][monsterX-1] == PLAYER_CELL) and grid[monsterY][monsterX-1] != WALL_CELL:
        moveMonster.append('left')
    if (grid[monsterY][monsterX+1] == DIAMOND_CELL  or grid[monsterY][monsterX+1] == EMPTY_CELL or grid[monsterY][monsterX+1] == PLAYER_CELL) and grid[monsterY][monsterX+1] != WALL_CELL :
        moveMonster.append('right')
    if (grid[monsterY-1][monsterX] == DIAMOND_CELL or grid[monsterY-1][monsterX] == EMPTY_CELL or grid[monsterY-1][monsterX] == PLAYER_CELL) and grid[monsterY-1][monsterX] != WALL_CELL:
        moveMonster.append('up')
    if (grid[monsterY+1][monsterX] == DIAMOND_CELL or grid[monsterY+1][monsterX] == EMPTY_CELL or grid[monsterY+1][monsterX] == PLAYER_CELL) and grid[monsterY+1][monsterX] != WALL_CELL :
        moveMonster.append('down')
    return moveMonster

def canMove():
    global grid,lives
    indexEmeny = getMonster(grid)
    for move in indexEmeny:
        monsterY = move[0]
        monsterX = move[1]
        postionToGo = moveInGrid(grid,monsterY,monsterX)
        if len(postionToGo) > 0:
            moveMonster = random.choice(postionToGo)
            if moveMonster == 'left':
                if grid[monsterY][monsterX-1] == DIAMOND_CELL:
                    grid[monsterY][monsterX] = DIAMOND_CELL
                    grid[monsterY][monsterX-1] = MONSTER_CELL
                elif grid[monsterY][monsterX-1] == EMPTY_CELL:
                    grid[monsterY][monsterX] = EMPTY_CELL
                    grid[monsterY][monsterX-1] = MONSTER_CELL
                elif grid[monsterY][monsterX-1] == PLAYER_CELL:
                    lives -= 1
                    # winsound .PlaySound('sound/died.wav', winsound.SND_FILENAME)
            if moveMonster == 'right':
                if grid[monsterY][monsterX+1] == DIAMOND_CELL:
                    grid[monsterY][monsterX] = DIAMOND_CELL
                    grid[monsterY][monsterX+1] = MONSTER_CELL
                elif grid[monsterY][monsterX+1] == EMPTY_CELL:
                    grid[monsterY][monsterX] = EMPTY_CELL
                    grid[monsterY][monsterX+1] = MONSTER_CELL
                elif grid[monsterY][monsterX+1] == PLAYER_CELL:
                    lives -= 1
                    # winsound .PlaySound('sound/died.wav', winsound.SND_FILENAME)
                    
            if moveMonster == 'up':
                if grid[monsterY-1][monsterX] == DIAMOND_CELL:
                    grid[monsterY][monsterX] = DIAMOND_CELL
                    grid[monsterY-1][monsterX] = MONSTER_CELL
                elif grid[monsterY-1][monsterX] == EMPTY_CELL:
                    grid[monsterY][monsterX] = EMPTY_CELL
                    grid[monsterY-1][monsterX] = MONSTER_CELL
                elif grid[monsterY-1][monsterX] == PLAYER_CELL:
                    lives -= 1
                    # winsound .PlaySound('sound/died.wav', winsound.SND_FILENAME)
            if moveMonster == 'down':
                if grid[monsterY+1][monsterX] == DIAMOND_CELL:
                    grid[monsterY][monsterX] = DIAMOND_CELL
                    grid[monsterY+1][monsterX] = MONSTER_CELL
                elif grid[monsterY+1][monsterX] == EMPTY_CELL:
                    grid[monsterY][monsterX] = EMPTY_CELL
                    grid[monsterY+1][monsterX] = MONSTER_CELL
                elif grid[monsterY+1][monsterX] == PLAYER_CELL:
                    lives -=1
                    # winsound .PlaySound('sound/died.wav', winsound.SND_FILENAME)
    canvas.delete("all")                
    drawGrid()
    canvas.after(300,canMove)
canvas.after(300,canMove)
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

# end game

# def endGame():
#     canvas.delete('all')
#     canvas.create_text(350,350,text='Congratulation',font=('Arial',65))

# if end:
#     endGame()

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
            
            winsound .PlaySound('sound/died.wav', winsound.SND_FILENAME)
            if lives == 0:
                end = True
                messagebox.showinfo("Lost","You Lost this game!")
        if moveX == 1 and moveY == 0: # move right
            if grid[newPlayerY][newPlayerX] == KEY_CELL:
                hasKey = True
            if grid[newPlayerY][newPlayerX] == HOME_CELL and hasKey:
                winsound .PlaySound('sound/win.wav', winsound.SND_FILENAME)
                messagebox.showinfo("Congrats","You Win!")
                end = True
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