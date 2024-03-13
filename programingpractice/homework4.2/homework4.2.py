import turtle
from collections import deque
from copy import deepcopy



t = turtle.Turtle()
s = turtle.Screen()


#part1
with open('/Users/jiho/OneDrive - Kyoto University/2回生後期/programing practice/homework4.2/maze.txt', 'r') as f:
    maze = [s.strip() for s in f.readlines()]
    
mazelist = [list(maze[i]) for i in range(0,len(maze))]


maze_width = 30 #迷路のサイズ
positionx, positiony = -len(maze[0])*maze_width/2, len(maze)*maze_width/2 #迷路の左上の座標
penwidth = maze_width/2 #経路の線の太さ

t.hideturtle()
t.penup()
t.setposition(positionx,positiony)
t.pendown()
t.speed(0)
s.tracer(0)



#迷路作成
for i in range(0,len(mazelist)):
    for j in range(0,len(mazelist[i])):
        #draw wall
        if mazelist[i][j] == '+' :
            t.fillcolor('black')
            t.begin_fill()
            for k in range(0,4):
                t.forward(maze_width)
                t.left(90)
            t.forward(maze_width)
            t.end_fill()
        # draw street
        if mazelist[i][j] == ' ' :
            t.penup()
            t.forward(maze_width)
            t.pendown()
        #draw start
        if mazelist[i][j] == 'T':
            t.fillcolor('green')
            t.begin_fill()
            for k in range(0,4):
                t.forward(maze_width)
                t.left(90)
            t.forward(maze_width)
            t.end_fill()
            START = (i,j)
        #draw goal
        if mazelist[i][j] == '*':
            t.fillcolor('red')
            t.begin_fill()
            for k in range(0,4):
                t.forward(maze_width)
                t.left(90)
            t.forward(maze_width)
            t.end_fill()
            GOAL = (i,j)
            
            
    t.penup()
    t.left(180)
    t.forward(maze_width*len(mazelist[i]))
    t.left(90)
    t.forward(maze_width)
    t.left(90)
    t.pendown


#part2
#最短距離探索
a,b = GOAL
mazelist[a][b] = ' '
WIDTH  = len(mazelist[0])
HEIGHT = len(mazelist)



def print_maze(maze_data, print_width=3):
    for line in maze_data:
        for char in line:
            print(char.center(print_width), end='')
        print()


def dfsearch(maze_data):
    mazelist = deepcopy(maze_data)
    steps = 1
    stack = [START]

    while stack:
        y, x = stack.pop()
        mazelist[y][x] = str(steps)
        if y == GOAL[0] and x == GOAL[1]:
            break
    
        for yi, xi in [(y, x-1), (y, x+1), (y-1, x), (y+1, x)]:
            if mazelist[yi][xi] == ' ':
                stack.append((yi, xi))
        steps += 1

    return mazelist

def print_maze(maze_data, print_width=3):
    for line in maze_data:
        for char in line:
            print(char.center(print_width), end='')
        print()

def dfsearch(maze_data):
    mazelist = deepcopy(maze_data)
    steps = 1
    stack = [START]

    while stack:
        y, x = stack.pop()
        mazelist[y][x] = str(steps)
        if y == GOAL[0] and x == GOAL[1]:
            break
    
        for yi, xi in [(y, x-1), (y, x+1), (y-1, x), (y+1, x)]:
            if mazelist[yi][xi] == ' ':
                stack.append((yi, xi))
        steps += 1

    return mazelist

def bfsearch(maze_data):
    mazelist = deepcopy(maze_data)
    distance = [[-1]*WIDTH for _ in range(HEIGHT)]
    distance[START[0]][START[1]] = 1
    que = deque([START])

    while que:
        y, x = que.popleft()
        mazelist[y][x] = str(distance[y][x])
        if y == GOAL[0] and x == GOAL[1]:
            break
    
        for yi, xi in [(y, x-1), (y, x+1), (y-1, x), (y+1, x)]:
            if mazelist[yi][xi] == ' ':
                que.append((yi, xi))
                distance[yi][xi] = distance[y][x] + 1

    return mazelist



def position(x,y):
    a = (positionx+ (x+0.5)*maze_width ,positiony - (y-0.5)*maze_width)

    return a


def shortest_draw(bfresult):
    y, x = GOAL
    ys, xs = START
    count = int(bfresult[GOAL[0]][GOAL[1]])
    shortest_list = [position(x,y)]

    while count > 1:
        count -= 1
        for yi, xi in [(y, x-1), (y, x+1), (y-1, x), (y+1, x)]:
            if bfresult[yi][xi] == str(count):
                y, x = yi, xi
                shortest_list.insert(0,position(x,y))
                break

    return shortest_list

if __name__ == '__main__':
    bfresult = bfsearch(mazelist)

#draw root
c,d = START
t.setposition(position(d,c))
t.pendown()
s.tracer(1)
t.speed(1)



for i in range(0,int(bfresult[a][b])):
    t.pencolor('red')
    t.width(penwidth)
    t.setpos(shortest_draw(bfresult)[i])




turtle.done()
