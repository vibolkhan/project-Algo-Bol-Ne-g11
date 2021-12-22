import tkinter as tk

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
    [0,2,5,5,5,0],
    [0,1,0,3,0,0],
]

countScore = 0
hasKey = False
arrivedHome = False

def drawGrid():
    canvas.delete('all')
    canvas.create_image(210,310, image=myBackground)
    
    canvas.create_text(250,30,text='Lives: ',font=('Ubuntu',18))
    canvas.create_image(300,30,image=heart_image)
    canvas.create_image(340,30,image=heart_image)
    canvas.create_image(380,30,image=heart_image)

    canvas.create_text(540,30,text='Levels: 1 ',font=('Ubuntu',18))


    canvas.create_text(70,30,text='Score: ' + str(countScore),font=('Ubuntu',18))

    if hasKey:
        canvas.create_text(300,70,text='You has key',font=('Ubuntu',18))

    if arrivedHome:
        canvas.itemconfig(textkey,text='You Win!')

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
                canvas.create_image(x,y,image= stair,anchor='center')           
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
    global countScore, hasKey,textkey,arrivedHome
    row = getRowOf1()
    col = getColOf1()
    if col != 0 and grid[row][col-1] != 3:
        oldValue = grid[row][col-1]
        grid[row][col] = 0
        grid[row][col-1]=1
        if oldValue == 5:
            countScore += 10
        elif oldValue == 4:
            hasKey = True
            textkey="You can go home now"
            
        if oldValue == 3 and hasKey:
            arrivedHome = True
    drawGrid()
def move_right(event):
    global countScore, hasKey,textkey,arrivedHome
    row = getRowOf1()
    col = getColOf1()
    if col < len(grid[0])-1 and grid[row][col+1] != 3:
        oldValue = grid[row][col+1]
        grid[row][col] = 0
        grid[row][col+1]=1
        if oldValue == 5:
            countScore += 10
        elif oldValue == 4:
            hasKey = True
            textkey="You can go home now"
        if oldValue == 3 and hasKey:
            arrivedHome = True
    drawGrid()

def move_down(event):
    global countScore, hasKey,textkey,arrivedHome
    row = getRowOf1()
    col = getColOf1()
    
    if row < len(grid)-1 and grid[row+1][col] != 3:
        oldValue = grid[row+1][col]
        grid[row][col] = 0
        grid[row+1][col]=1
        if oldValue == 5:
            countScore += 10
        elif oldValue == 4:
            hasKey = True
            textkey="You can go home now"
        if oldValue == 3 and hasKey:
            arrivedHome = True
    drawGrid()

def move_up(event):
    global countScore, hasKey,textkey,arrivedHome
    row = getRowOf1()
    col = getColOf1()
    if row != 0 and grid[row-1][col] != 3:
        oldValue = grid[row-1][col]
        grid[row][col] = 0
        grid[row-1][col]=1
        if oldValue == 5:
            countScore += 10
        elif oldValue == 4:
            hasKey = True
            textkey="You can go home now"
        if oldValue == 3 and hasKey:
            arrivedHome = True
    drawGrid()

root.bind('<Left>',move_left) #### keyboard
root.bind('<Right>',move_right) #### keyboard
root.bind('<Down>',move_down) #### keyboard
root.bind('<Up>',move_up) #### keyboard

canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')

root.mainloop()