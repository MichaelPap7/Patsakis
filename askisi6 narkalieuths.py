import random

def addscores():
    for i in range(1,width):
        for j in range(1,height):
            if board[i][j]!='*':
                if board [i-1][j]=='*':
                    board[i][j]+=1
                if board[i-1][j+1]=='*':
                    board[i][j]+=1
                if board [i][j-1]=='*':
                    board[i][j]+=1
                if board [i][j+1]=='*':
                    board[i][j]+=1
                if board[i+1][j-1]=='*':
                    board[i][j]+=1
                if board[i+1][j]=='*':
                    board[i][j]+=1
                if board[i+1][j+1]=='*':
                    board[i][j]+=1
   
width= int( input("Width Size:") )
height= int ( input("Height Size:") )
mines= int ( input("Number of Mines:") )

board = [[int(0) for x in range(width+1)] for y in range(height+1)]
for i in range (mines):
    board[random.randint(1,width)][random.randint(1,height)] = '*'
                                
addscores()

for i in range (1,width):
    print(board[i])
