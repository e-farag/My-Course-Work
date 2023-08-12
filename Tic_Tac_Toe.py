#Function Part
# Printing the Board Function
def print_board(game):
    '''
    Printing Board Function with the input of Game Board List of Lists
    '''
    print("\n"*20)
    print('---------------------------------------------------\n')
    for row_cells in game:
        for square_cell in row_cells:
            print("|\t{}\t".format(square_cell), end=' ')
        print("|\n")
        print('---------------------------------------------------\n')

# Function to ask the Player move
def play_role(game,type):
    '''
    Ask Player to the marking location input game board list of lists and the type of mark or player
    '''
    flag=True
    while flag==True:
        print('Please To mark your '+type+': ')
        try:
            play_row,play_col=input('choose row,col [Two numbers each between (1-3)]: ').split(',')
        except:
            print('Wrong Data, Choose again')
            continue
        try:
            row=int(play_row)-1
        except:
            print('The row should be a number')
            continue
        try:
            col=int(play_col)-1
        except:
            print('The column should be a number')
            continue

        if (col<0 or col>2):
            print('The column should be between (1-3)')
            continue
        if (row<0 or row>2):
            print('The row should be between (1-3)')
            continue

        if game[row][col]==' ':
            game[row][col]=type
            flag=False
        else:
            print_board(game)
            print('The cell is busy please try again:')

#Function to check the Winner       
def check_win(game,type):
    '''
    Check the winner with input thwe game board list of lists and the type of mark or player
    '''
    flag=True
    checkerh=[0,0,0]
    checkerv=[0,0,0]
    checkerc=[0,0]
    countmain=0
    count=0
    for item in game:
        for cell in item:
            if cell == type:
                checkerh[countmain]+= 2**count
                checkerv[count]+=2**count
                if count==countmain:
                    checkerc[0]+=2**count
                if count+countmain==2:
                    checkerc[1]+=2**count
            count+=1
        count=0
        countmain+=1
    if (checkerh[0]==7 or checkerh[1]==7 or checkerh[2]==7):
        print('3 in horizontal')
        flag=False
    elif (checkerv[0]==3 or checkerv[1]==6 or checkerv[2]==12):
        print('3 in vertical')
        flag=False
    elif (checkerc[0]==7 or checkerc[1]==7):
        print('3 in cross')
        flag=False
    return flag

#Function to check the tie case
def check_tie(trial):
    '''
    Check the tie case with input of the no of trials
    '''
    flag=True
    if trial==9:
        flag=False
    
    return flag


#Main Game

#initate Board
trials=0
game_board=[[' ',' ', ' '],[' ',' ', ' '],[' ',' ', ' ']]

#Playing the game
print_board(game_board)
flagy=True
play_type='O'
while flagy==True:
    if play_type=='X':
        play_type='O'
    else:
        play_type='X'
    trials+=1
    play_role(game_board,play_type)
    print_board(game_board)
    if check_win(game_board,play_type)==False:
        print('Player of '+play_type+' is the winner')
        flagy=False

    if check_tie(trials)==False:
        flagy=False
        print('Game is Tie')