import tkinter as tk
from tkinter import font
from tkinter.constants import RAISED # import tkiker 
import winsound # import sound
import random # import random
# ---------------------------------------------------------------------------------------------------
# display window
root = tk.Tk() 
root.geometry("770x650")
frame = tk.Frame()
frame.master.title('Amazing game')
canvas = tk.Canvas(frame)
root.resizable(0,0)
# ---------------------------------------------------------------------------------------------------
# menubar
menubar = tk.Menu(frame)  
menubar.add_command(label="Welcome!") 
menubar.add_command(label="Quit!", command=quit) 
# display menubar
root.config(menu=menubar)
# ---------------------------------------------------------------------------------------------------
# images
myBackground=tk.PhotoImage(file='image/backg.png')
avatar = tk.PhotoImage(file='image/avatar.png')
monster = tk.PhotoImage(file='image/monster.png')
home = tk.PhotoImage(file='image/home.png')
key = tk.PhotoImage(file='image/key.png')
wall=tk.PhotoImage(file="image/wall.png")
heart_image=tk.PhotoImage(file="image/heart.png")
coin =tk.PhotoImage(file="image/coin.png")
congrats = tk.PhotoImage(file='image/congrats.png')
lostGame = tk.PhotoImage(file='image/gameover.png')
start = tk.PhotoImage(file = "image/start.png")
laod = tk.PhotoImage(file = "image/laod.png")
# ---------------------------------------------------------------------------------------------------

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
isWin = False
restart = False
# -------------------------------------------
grid = [
    [6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ],
    [6 ,5 ,5 ,5 ,5 ,5 ,5 ,2 ,5 ,6 ,5 ,5 ,5 ,6 ,2 ,5 ,2 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,6 ],
    [6 ,6 ,5 ,6 ,6 ,5 ,6 ,6 ,6 ,6 ,5 ,6 ,5 ,6 ,6 ,6 ,5 ,5 ,5, 5, 6, 5, 3 ,5 ,6 ],
    [6 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,2 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,2 ,5 ,6 ,5 ,6 ],
    [6 ,5 ,5 ,2 ,5 ,5 ,5 ,5 ,5 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,5 ,6 ,6 ,6 ,6 ,5 ,6 ,5, 6 ],
    [6 ,5 ,6 ,6 ,6 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,6 ,5 ,6 ],
    [6 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,2 ,5 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,2 ,6 ,5 ,5 ,5 ,6 ],
    [6 ,5 ,6 ,6 ,5 ,6 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,2 ,5 ,6 ,5 ,5 ,5 ,6 ],
    [6 ,5 ,5 ,2 ,5 ,6 ,5 ,6 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,6 ,6 ,6 ,2 ,6 ],
    [6 ,2 ,6 ,6 ,6 ,6 ,5 ,6 ,6 ,6 ,6 ,5 ,1 ,5 ,6 ,6 ,6 ,6 ,5 ,2 ,5 ,5 ,5 ,5 ,6 ],
    [6 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,6 ,5 ,5 ,2 ,6 ],
    [6 ,2 ,6 ,6 ,6 ,6 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,6 ,5 ,6 ,5 ,6 ],
    [6 ,5 ,2 ,5 ,5 ,6 ,5 ,6 ,5 ,2 ,5 ,5 ,6 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,6 ,5 ,6 ,5 ,6 ],
    [6 ,5 ,6 ,6 ,5 ,6 ,2 ,5 ,5 ,5 ,5 ,5 ,6 ,5 ,5 ,2 ,5 ,5 ,2 ,5 ,6 ,5 ,6 ,5 ,6 ],
    [6 ,4 ,6 ,6 ,5 ,6 ,5 ,5 ,5 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,5 ,6 ,6 ,6 ,6 ,5 ,5 ,2 ,6 ],
    [6 ,2 ,5 ,2 ,5 ,5 ,5 ,5 ,5 ,2 ,5 ,5 ,5 ,2 ,5 ,5 ,2 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,6 ],
    [6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ],

]      

#12,9
# ---------------------------------------------------------------------------------------------------
# drawing
def startGame():
     canvas.create_image(380,320, image= start)     
startGame()

def drawGrid():
    global end,lives,restart
    canvas.delete('all')
    canvas.create_image(380,320, image=myBackground)
    canvas.create_text(330,30,text='Lives: ',font=('Arial',18),fill='white')
    # -------------------------------------------- draw heart -------------------------------------------
    if lives == 3:
        heart1 = canvas.create_image(380,30,image=heart_image)
        heart2 = canvas.create_image(420,30,image=heart_image)
        heart3 = canvas.create_image(460,30,image=heart_image)
    elif lives == 2:
        heart1 = canvas.create_image(380,30,image=heart_image)
        heart2 = canvas.create_image(420,30,image=heart_image)
    elif lives == 1:
        heart1 = canvas.create_image(380,30,image=heart_image)
    # -------------------------------------------- draw heart -------------------------------------------
    canvas.create_text(620,30,text='Levels: 1',font=('Arial',18),fill='white') # show level
    canvas.create_text(150,30,text='Score: ' + str(score),font=('Arial',18),fill='white') # show score
    # -------------------------------------------- display message ---------------------------------------
    if hasNoKey:
        textKey = canvas.create_text(380,70,text='You has no key, you need to find key!',font=('Arial',18))
    if hasKey and not hasNoKey:
        textKey = canvas.create_text(380,70,text='You has key, you can go home now!',font=('Arial',18))
    if hasNoKey and hasKey:
        canvas.itemconfig(textKey,text='You has key, you can go home now!')
    if hasKey:
        textKey = canvas.create_text(380,70,text='You has key, you can go home now!',font=('Arial',18))
    # -------------------------------------------- display message ---------------------------------------

    # ------------------------------------------ end game ------------------------------------------------
    if end:
        getStatus()
    # ------------------------------------------ end game ------------------------------------------------

    # ------------------------------------------ restart game ------------------------------------------------
    if restart and not end:
        canvas.after(800,restartGame)
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
                canvas.create_image(x+15,y+15,image = coin,anchor='center') 
            elif grid[row][col]== WALL_CELL:
                canvas.create_image(x+15,y+15,image= wall,anchor='center')           
            x+=30
        x=10
        y+=30
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# move monster
def getMonster(grid):
    indexEnemy = []
    for row in range (len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == MONSTER_CELL:
                indexEnemy.append([row, col])
    return indexEnemy

def moveInGrid(grid,monsterY,monsterX):
    moveMonster = []
    if (grid[monsterY][monsterX-1] == DIAMOND_CELL or grid[monsterY][monsterX-1] == PLAYER_CELL) and grid[monsterY][monsterX-1] != WALL_CELL:
        moveMonster.append('left')
    if (grid[monsterY][monsterX+1] == DIAMOND_CELL or grid[monsterY][monsterX+1] == PLAYER_CELL) and grid[monsterY][monsterX+1] != WALL_CELL :
        moveMonster.append('right')
    if (grid[monsterY-1][monsterX] == DIAMOND_CELL or grid[monsterY-1][monsterX] == PLAYER_CELL) and grid[monsterY-1][monsterX] != WALL_CELL:
        moveMonster.append('up')
    if (grid[monsterY+1][monsterX] == DIAMOND_CELL or grid[monsterY+1][monsterX] == PLAYER_CELL) and grid[monsterY+1][monsterX] != WALL_CELL :
        moveMonster.append('down')
    return moveMonster

def monsterCanMove():
    global grid,lives,end,restart
    if lives <= 0:
        end = True
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
                elif grid[monsterY][monsterX-1] == PLAYER_CELL and lives >= 0:
                    lives -= 1
                    grid[monsterY][monsterX-1] == MONSTER_CELL
                    restart = True
            if moveMonster == 'right':
                if grid[monsterY][monsterX+1] == DIAMOND_CELL:
                    grid[monsterY][monsterX] = DIAMOND_CELL
                    grid[monsterY][monsterX+1] = MONSTER_CELL
                elif grid[monsterY][monsterX+1] == EMPTY_CELL:
                    grid[monsterY][monsterX] = EMPTY_CELL
                    grid[monsterY][monsterX+1] = MONSTER_CELL
                elif grid[monsterY][monsterX+1] == PLAYER_CELL and lives >= 0:
                    lives -= 1 
                    grid[monsterY][monsterX+1] == MONSTER_CELL
                    restart = True
            if moveMonster == 'up':
                if grid[monsterY-1][monsterX] == DIAMOND_CELL:
                    grid[monsterY][monsterX] = DIAMOND_CELL
                    grid[monsterY-1][monsterX] = MONSTER_CELL
                elif grid[monsterY-1][monsterX] == EMPTY_CELL:
                    grid[monsterY][monsterX] = EMPTY_CELL
                    grid[monsterY-1][monsterX] = MONSTER_CELL
                elif grid[monsterY-1][monsterX] == PLAYER_CELL and lives >= 0:
                    lives -= 1
                    grid[monsterY-1][monsterX] = MONSTER_CELL
                    restart = True
            if moveMonster == 'down':
                if grid[monsterY+1][monsterX] == DIAMOND_CELL:
                    grid[monsterY][monsterX] = DIAMOND_CELL
                    grid[monsterY+1][monsterX] = MONSTER_CELL
                elif grid[monsterY+1][monsterX] == EMPTY_CELL:
                    grid[monsterY][monsterX] = EMPTY_CELL
                    grid[monsterY+1][monsterX] = MONSTER_CELL
                elif grid[monsterY+1][monsterX] == PLAYER_CELL and lives >= 0:
                    lives -=1
                    grid[monsterY+1][monsterX] == MONSTER_CELL
                    restart = True
    drawGrid()
    canvas.after(800,monsterCanMove)
canvas.after(800,monsterCanMove)
# ---------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------
# move player

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

def move(moveX, moveY) :
    global lives,score,hasNoKey,hasKey,end,isWin,restart
    playerX = getPlayerX()
    playerY = getPlayerY()
    newPlayerX = playerX + moveX
    newPlayerY = playerY + moveY 
    if grid[newPlayerY][newPlayerX] != WALL_CELL :
        if grid[newPlayerY][newPlayerX] == DIAMOND_CELL: # count score
                score += 10 
                # winsound .PlaySound('sound/coin.wav', winsound.SND_FILENAME)
        if grid[newPlayerY][newPlayerX] == MONSTER_CELL and lives > 0 and not end: # count lives
            lives -= 1
            restart = True 
            if lives == 0:
                end = True
                winsound .PlaySound('sound/lost.wav', winsound.SND_FILENAME)
        if moveX == 1 and moveY == 0: # move right --------------------------------------------------------------
            if grid[newPlayerY][newPlayerX] == KEY_CELL:
                hasKey = True
            if grid[newPlayerY][newPlayerX] == HOME_CELL and hasKey:
                winsound .PlaySound('sound/win.wav', winsound.SND_FILENAME)
                end = True
                isWin = True
            elif grid[newPlayerY][newPlayerX] == HOME_CELL and not hasKey: # get key
                grid[playerY][playerX] = PLAYER_CELL
                grid[newPlayerY][newPlayerX] = HOME_CELL
                hasNoKey = True
            elif grid[newPlayerY][newPlayerX] == MONSTER_CELL:
                grid[playerY][playerX] = EMPTY_CELL
                grid[newPlayerY][newPlayerX] = MONSTER_CELL
                restart = True
            elif newPlayerX < len(grid[0]):
                grid[playerY][playerX] = EMPTY_CELL
                grid[newPlayerY][newPlayerX] = PLAYER_CELL
                
        elif moveX == -1 and moveY == 0: # move left -------------------------------------------------------------
            if grid[newPlayerY][newPlayerX] == KEY_CELL:
                hasKey = True
            if grid[newPlayerY][newPlayerX] == HOME_CELL and hasKey:
                winsound .PlaySound('sound/win.wav', winsound.SND_FILENAME)
                end = True
                isWin = True
            elif grid[newPlayerY][newPlayerX] == HOME_CELL and not hasKey: # get key
                grid[playerY][playerX] = PLAYER_CELL
                grid[newPlayerY][newPlayerX] = HOME_CELL
                hasNoKey = True
            elif grid[newPlayerY][newPlayerX] == MONSTER_CELL:
                grid[playerY][playerX] = EMPTY_CELL
                grid[newPlayerY][newPlayerX] = MONSTER_CELL
                restart = True
            elif newPlayerX >= 0:
                grid[playerY][playerX] = EMPTY_CELL
                grid[newPlayerY][newPlayerX] = PLAYER_CELL

        elif moveX == 0 and moveY == 1: # move down --------------------------------------------------------------
            if grid[newPlayerY][newPlayerX] == KEY_CELL:
                hasKey = True
            if grid[newPlayerY][newPlayerX] == HOME_CELL and hasKey:
                winsound .PlaySound('sound/win.wav', winsound.SND_FILENAME)
                end = True
                isWin = True
            elif grid[newPlayerY][newPlayerX] == HOME_CELL and not hasKey: # get key
                grid[playerY][playerX] = PLAYER_CELL
                grid[newPlayerY][newPlayerX] = HOME_CELL
                hasNoKey = True
            elif grid[newPlayerY][newPlayerX] == MONSTER_CELL:
                grid[playerY][playerX] = EMPTY_CELL
                grid[newPlayerY][newPlayerX] = MONSTER_CELL
                restart = True
            elif newPlayerY < len(grid):
                grid[playerY][playerX] = EMPTY_CELL
                grid[newPlayerY][newPlayerX] = PLAYER_CELL
        elif moveX == 0 and moveY == -1: # move up --------------------------------------------------------------
            if grid[newPlayerY][newPlayerX] == KEY_CELL:
                hasKey = True
            if grid[newPlayerY][newPlayerX] == HOME_CELL and hasKey:
                winsound .PlaySound('sound/win.wav', winsound.SND_FILENAME)
                end = True
                isWin = True    
            elif grid[newPlayerY][newPlayerX] == HOME_CELL and not hasKey: # get key
                grid[playerY][playerX] = PLAYER_CELL
                grid[newPlayerY][newPlayerX] = HOME_CELL
                hasNoKey = True
            elif grid[newPlayerY][newPlayerX] == MONSTER_CELL:
                grid[playerY][playerX] = EMPTY_CELL
                grid[newPlayerY][newPlayerX] = MONSTER_CELL
                restart = True
            elif newPlayerY >= 0:
                grid[playerY][playerX] = EMPTY_CELL
                grid[newPlayerY][newPlayerX] = PLAYER_CELL
    drawGrid()
# ---------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------
# restart game
def restartGame():
    global restart
    if lives >= 0:
        grid[9][12]=PLAYER_CELL
        restart = False
        
        # canvas.after(1600,monsterCanMove)
        # drawGrid()
    canvas.after(800,drawGrid)
# ---------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------
# end game
def getStatus():
    global grid,score
    grid=[]
    canvas.create_image(380,320, image=myBackground)
    if end and not isWin:
        canvas.create_image(380,320, image=lostGame)  
        canvas.create_text(380,400,text='You have ' + str(score) + ' scores' ,font=('Arial',30))
    elif end and isWin:
        canvas.create_image(380,320, image=congrats)
        canvas.create_text(380,400,text='You have ' + str(score) + ' scores',font=('Arial',30))
# ------------------------------------------------------------------

# --------------------------------------------------------
# MOVE PLAYER
def move_right(event):
    move(1,0)
def move_left(event):
    move(-1,0)
def move_down(event):
    move(0,1)
def move_up(event):
    move(0,-1)
# --------------------------------------------------------

# ---------------------------------------------------------------------------------------
# click on key board
root.bind('<Left>',move_left) #### keyboard
root.bind('<Right>',move_right) #### keyboard
root.bind(' <Down>',move_down) #### keyboard
root.bind('<Up>',move_up) #### keyboard
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------
# display all
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.mainloop()
# ---------------------------------------------------------------------------------------