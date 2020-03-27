import os
from colorama import *

game=[[0,0,0],
      [0,0,0],
      [0,0,0]]
symb=["","","","","","","","",""]
rstrt=1

init(autoreset=True)

def convert():
    for i in range(0,3):
        for j in range(0,3):
            if game[i][j]==0:symb[3*i+j]="   "
            if game[i][j]==1:symb[3*i+j]=Style.BRIGHT +Fore.RED + " X " +Fore.RESET
            if game[i][j]==2:symb[3*i+j]=Fore.BLUE + " O " +Fore.RESET
       
def display():
    print(Style.BRIGHT +Fore.YELLOW + "    0   1   2 \n" +Fore.RESET)
    print(Style.BRIGHT +Fore.YELLOW + "0  " +Fore.RESET+symb[0]+"|"+symb[1]+"|"+symb[2])
    print("   ———————————")
    print(Style.BRIGHT +Fore.YELLOW + "1  " +Fore.RESET+symb[3]+"|"+symb[4]+"|"+symb[5])
    print("   ———————————")
    print(Style.BRIGHT +Fore.YELLOW + "2  " +Fore.RESET+symb[6]+"|"+symb[7]+"|"+symb[8]+"\n\n")

def play(player,row,column):
    if game[row][column]==0:
        game[row][column]=player
        os.system('cls')
        convert()
        display()
        return 0
    else:
        print("\nError:The select box is already filled!!\n")
        return 1

def rowip(player):
    row_input=int(input(f"Player{player} enter row = "))
    while row_input>2 or row_input<0:
        print("Can only input row as 0,1 or 2!!!")
        row_input=int(input(f"Player{player} enter row = "))
    return row_input

def colip(player):
    column_input=int(input(f"Player{player} enter column = "))
    while column_input>2 or column_input<0:
        print("Can only input column as 0,1 or 2!!!")
        column_input=int(input(f"Player{player} enter column = "))
    return column_input

def check():
    wp=0
    if game[0][0]==game[1][1]==game[2][2]!=0 :wp=game[0][0]
    if game[0][2]==game[1][1]==game[2][0]!=0 :wp=game[2][0]
    else: 
        for i in range(0,3):
            if game[i][0]==game[i][1]==game[i][2]!=0 :wp=game[i][0]
        for i in range(0,3):
            if game[0][i]==game[1][i]==game[2][i]!=0 :wp=game[0][i]
        return wp

def Input(player):
    r=rowip(player)
    c=colip(player)
    same=play(player,r,c)
    return same

while rstrt==1:
    wp=check()
    count=0
    convert()
    display()
    while(wp==0 and count<9):
        same=Input(1)
        while same==1:same=Input(1)
        wp=check()
        if(wp!=0):break
        count+=1
        if(count==9):break
        same=Input(2)
        while same==1:same=Input(2)
        wp=check()
        count+=1
    if wp==1:print("\nThe winner is player 1!!!\n")
    if wp==2:print("\nThe winner is player 2!!!\n")
    if wp==0:print("\nThe match was a draw...\n")
    rstrt=int(input("1.Restart Game\n2.Exit\nEnter choice : "))
    while rstrt>2 or rstrt<1:
        print("Please choose 1 or 2!!")
        rstrt=int(input("1.Restart Game\n2.Exit\nEnter choice : "))
    if rstrt==1:
        game=[[0,0,0],[0,0,0],[0,0,0]]
        os.system('cls')
    if rstrt==2:break