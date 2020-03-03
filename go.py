def print_board(board):
    print('')
    row='     '
    for j in range(19):
        if j<18:
            row+=alphabet[j]+'   '
        else:
            row+=alphabet[j]
    print(row)
    row='     '
    for j in range(19):
        if j<18:
            row+='    '
        else:
            row+='  '
    print(row)

    for i in range(19):
        row=alphabet[i]+'    '
        for j in range(19):
            if j<18:
                row+=board[i][j]+' - '
            else:
                row+=board[i][j]
        print(row)
        if i<18:
            row='     '
            for j in range(19):
                if j<18:
                    row+='|   '
                else:
                    row+='|'
            print(row)

def print_islands(board,B,W,BL,WL,total_BL,total_WL):

    print('')
    print('===========================================')
    print('Black Islands:')
    print_board(B)

    print('')
    print('===========================================')
    print('White Islands:')
    print_board(W)

    print('')
    print('===========================================')
    print('Black Liberties:')
    for i in total_BL:
        print('Island '+str(i)+' liberties: ' + str(total_BL[i]))
    print_board(BL)
    

    print('')
    print('===========================================')
    print('White Liberties:')
    for i in total_WL:
        print('Island '+str(i)+' liberties: ' + str(total_WL[i]))
    print_board(WL)
    print('')
    print('===========================================')


def calculate_liberties(board,total_black_captured,total_white_captured,B,W,num_B_islands,num_W_islands,print_it):
    BL = [' '] * 19
    for i in range(19):
        BL[i]=[' '] * 19
    total_BL={}
    for a in range(num_B_islands):
        for i in range(19):
            for j in range(19):
                if B[i][j]==str(a):
                    if i-1>=0 and board[i-1][j]!='B' and board[i-1][j]!='W':
                        BL[i-1][j]=str(a)
                    if j-1>=0 and board[i][j-1]!='B' and board[i][j-1]!='W':
                        BL[i][j-1]=str(a)
                    if i+1<19 and board[i+1][j]!='B' and board[i+1][j]!='W':
                        BL[i+1][j]=str(a)
                    if j+1<19 and board[i][j+1]!='B' and board[i][j+1]!='W':
                        BL[i][j+1]=str(a)
        total_BL[a]=0
        for i in range(19):
            for j in range(19):
                if BL[i][j]==str(a):
                    total_BL[a]+=1
        if total_BL[a]==0:
            for i in range(19):
                for j in range(19):
                    if B[i][j]==str(a):
                        board[i][j]=' '
                        total_black_captured+=1
                
    WL = [' '] * 19
    for i in range(19):
        WL[i]=[' '] * 19
    total_WL={}
    for a in range(num_W_islands):
        for i in range(19):
            for j in range(19):
                if W[i][j]==str(a):
                    if i-1>=0 and board[i-1][j]!='B' and board[i-1][j]!='W':
                        WL[i-1][j]=str(a)
                    if j-1>=0 and board[i][j-1]!='B' and board[i][j-1]!='W':
                        WL[i][j-1]=str(a)
                    if i+1<19 and board[i+1][j]!='B' and board[i+1][j]!='W':
                        WL[i+1][j]=str(a)
                    if j+1<19 and board[i][j+1]!='B' and board[i][j+1]!='W':
                        WL[i][j+1]=str(a)
        total_WL[a]=0
        for i in range(19):
            for j in range(19):
                if WL[i][j]==str(a):
                    total_WL[a]+=1
        if total_WL[a]==0:
            for i in range(19):
                for j in range(19):
                    if W[i][j]==str(a):
                        board[i][j]=' '
                        total_white_captured+=1
    if print_it=='print_it':
        print_islands(board,B,W,BL,WL,total_BL,total_WL)

    return total_black_captured, total_white_captured
    

def calculate_islands(board,total_black_captured,total_white_captured,print_it):
    num_B_islands=0
    num_W_islands=0
    B = [' '] * 19
    for i in range(19):
        B[i]=[' '] * 19
    W = [' '] * 19
    for i in range(19):
        W[i]=[' '] * 19
    for i in range(19):
        for j in range(19):
            if board[i][j]=='B':
                if i>=1 and j>=1:
                    if board[i-1][j]=='B' and board[i][j-1]=='B':
                        if B[i-1][j]!=B[i][j-1]:
                            if B[i-1][j]<B[i][j-1]:
                                B[i][j]=B[i-1][j]
                                correct_num = B[i-1][j]
                                too_large = B[i][j-1]
                                for k in range(19):
                                    for l in range(19):
                                        if B[k][l]==too_large:
                                            B[k][l]=correct_num
                            else:
                                B[i][j]=B[i][j-1]
                                correct_num = B[i][j-1]
                                too_large = B[i-1][j]
                                for k in range(19):
                                    for l in range(19):
                                        if B[k][l]==too_large:
                                            B[k][l]=correct_num
                        else:
                            if board[i-1][j]=='B':
                                B[i][j]=B[i-1][j]
                            if board[i][j-1]=='B':
                                B[i][j]=B[i][j-1]
                    else:
                        if i>=1:
                            if board[i-1][j]=='B':
                                B[i][j]=B[i-1][j]
                        if j>=1:
                            if board[i][j-1]=='B':
                                B[i][j]=B[i][j-1]
                else:
                    if i>=1:
                        if board[i-1][j]=='B':
                            B[i][j]=B[i-1][j]
                    if j>=1:
                        if board[i][j-1]=='B':
                            B[i][j]=B[i][j-1]
                if B[i][j]==' ':
                    num_B_islands+=1
                    B[i][j]=str(num_B_islands-1)
            if board[i][j]=='W':
                if i>=1 and j>=1:
                    if board[i-1][j]=='W' and board[i][j-1]=='W':
                        if W[i-1][j]!=W[i][j-1]:
                            if W[i-1][j]<W[i][j-1]:
                                W[i][j]=W[i-1][j]
                                correct_num = W[i-1][j]
                                too_large = W[i][j-1]
                                for k in range(19):
                                    for l in range(19):
                                        if W[k][l]==too_large:
                                            W[k][l]=correct_num
                                            
                            else:
                                W[i][j]=W[i][j-1]
                                correct_num = W[i][j-1]
                                too_large = W[i-1][j]
                                for k in range(19):
                                    for l in range(19):
                                        if W[k][l]==too_large:
                                            W[k][l]=correct_num
                                
                        else:
                            if board[i-1][j]=='W':
                                W[i][j]=W[i-1][j]
                            if board[i][j-1]=='W':
                                W[i][j]=W[i][j-1]
                    else:
                        if i>=1:
                            if board[i-1][j]=='W':
                                W[i][j]=W[i-1][j]
                        if j>=1:
                            if board[i][j-1]=='W':
                                W[i][j]=W[i][j-1]
                else:
                    if i>=1:
                        if board[i-1][j]=='W':
                            W[i][j]=W[i-1][j]
                    if j>=1:
                        if board[i][j-1]=='W':
                            W[i][j]=W[i][j-1]
                if W[i][j]==' ':
                    num_W_islands+=1
                    W[i][j]=str(num_W_islands-1)
                    
    total_black_captured, total_white_captured=calculate_liberties(board,total_black_captured,total_white_captured,B,W,num_B_islands,num_W_islands,print_it)

    return total_black_captured, total_white_captured

                   

alphabet = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S'}

total_black_captured=0
total_white_captured=0

board = [' '] * 19
for i in range(19):
    board[i]=[' '] * 19

board[3][3]='o'
board[3][9]='o'
board[3][15]='o'
board[9][3]='o'
board[9][9]='o'
board[9][15]='o'
board[15][3]='o'
board[15][9]='o'
board[15][15]='o'


select = ''
turn = 'B'
while select !='Q':

    print_board(board)
    
    print('Enter q to quit or i to show islands')
    if turn=='B':
        select = input("Black's turn: ").upper()
    else:
        select = input("White's turn: ").upper()
    if len(select)==2:
        row=-1
        col=-1
        for i in alphabet:
            if alphabet[i]==select[0]:
                row=i
                print('row: '+str(i))
            if alphabet[i]==select[1]:
                col=i
                print('col: '+str(i))
        if row>=0 and col>=0:
            if board[row][col]!='B' and board[row][col]!='W':
                if turn=='B':
                    board[row][col]='B'
                    turn='W'
                else:
                    board[row][col]='W'
                    turn='B'
            else:
                print('Spot already taken')
    print('')
    print('***************************************************************')
    total_black_captured, total_white_captured=calculate_islands(board,total_black_captured,total_white_captured,'dont_print')
    print('Total Black Captured: ' + str(total_black_captured))
    print('Total White Captured: ' + str(total_white_captured))
    if select=='I':
        total_black_captured, total_white_captured=calculate_islands(board,total_black_captured,total_white_captured,'print_it')
    
