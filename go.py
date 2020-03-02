

alphabet = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S'}

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

    print('Enter q to quit')
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
            
