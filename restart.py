import os
from colorama import *

game=[[9,10,11,12,13,14,15,16],
	[1,2,3,4,5,6,7,8],
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0],
	[-1,-2,-3,-4,-5,-6,-7,-8,],
	[-9,-10,-11,-12,-13,-14,-15,-16]]

# game=[[0,0,0,0,0,0,0,0],
# 	[0,0,0,0,11,0,0,0],
# 	[0,-1,0,0,0,-1,0,0],
# 	[0,0,0,0,0,0,0,0],
# 	[0,-1,0,-11,0,-1,0,0],
# 	[0,0,0,0,0,0,0,0],
# 	[0,-1,0,0,0,-1,0,0],
# 	[0,0,0,0,0,0,0,0]]

board=[["","","","","","","","",],
		["","","","","","","","",],
		["","","","","","","","",],
		["","","","","","","","",],
		["","","","","","","","",],
		["","","","","","","","",],
		["","","","","","","","",],
		["","","","","","","","",],]

def convert():
	for x in range(0,8):
		for y in range(0,8):
			if -8<=game[x][y]<0:board[x][y]=Style.BRIGHT +Fore.RED +" P "+Fore.RESET
			if game[x][y]==-9 or game[x][y]==-16:board[x][y]=Style.BRIGHT +Fore.RED +" R "+Fore.RESET
			if game[x][y]==-10 or game[x][y]==-15:board[x][y]=Style.BRIGHT +Fore.RED +" k "+Fore.RESET
			if game[x][y]==-11 or game[x][y]==-14:board[x][y]=Style.BRIGHT +Fore.RED +" B "+Fore.RESET
			if game[x][y]==-12:board[x][y]=Style.BRIGHT +Fore.RED +" Q "+Fore.RESET
			if game[x][y]==-13:board[x][y]=Style.BRIGHT +Fore.RED +" K "+Fore.RESET
			if 0<game[x][y]<=8:board[x][y]=Style.BRIGHT +Fore.BLUE +" P "+Fore.RESET
			if game[x][y]==9 or game[x][y]==16:board[x][y]=Style.BRIGHT +Fore.BLUE +" R "+Fore.RESET
			if game[x][y]==10 or game[x][y]==15:board[x][y]=Style.BRIGHT +Fore.BLUE +" k "+Fore.RESET
			if game[x][y]==11 or game[x][y]==14:board[x][y]=Style.BRIGHT +Fore.BLUE +" B "+Fore.RESET
			if game[x][y]==12:board[x][y]=Style.BRIGHT +Fore.BLUE +" Q "+Fore.RESET
			if game[x][y]==13:board[x][y]=Style.BRIGHT +Fore.BLUE +" K "+Fore.RESET
			if game[x][y]==0:board[x][y]="   "
			


def display():
	print("      a   b   c   d   e   f   g   h\n")
	print("    ---------------------------------")
	for x in range(0,8):
		print(str(8-x)+"   ",end="")
		for y in range(0,8):
			print("|"+board[x][y],end="")
		print("|   "+str(8-x))
		print("    ---------------------------------")
	print("\n      a   b   c   d   e   f   g   h\n")

def posToNum(coord):
	switcher = {
		'a':0,
		'b':1,
		'c':2,
		'd':3,
		'e':4,
		'f':5,
		'g':6,
		'h':7,
		'8':0,
		'7':1,
		'6':2,
		'5':3,
		'4':4,
		'3':5,
		'2':6,
		'1':7,
	}
	return (str(switcher.get(coord[1],"Invalid"))+str(switcher.get(coord[0],"Invalid")))

def Input(player):
	if player==-1:
		pno=1
	if player==1:
		pno=2
	print("Player "+str(pno)+"'s turn ::")
	from_str=input(f"Move :: ")
	from_pos=posToNum(from_str)
	if (not canMoveFrom(from_pos,player)):
		return 0
	to_str=input(f"to :: ")
	to_pos=posToNum(to_str)
	if (not canMoveTo(from_pos,to_pos,player)):
		return 0
	move(player,from_pos,to_pos)
	return 1

def validPos(pos):
	if('0'<=pos[0]<='7'and '0'<=pos[1]<='7'):
		return True
	else:
		print("Invalid position!\nValid postions are from 'a1' to 'h8'\n\n")
		return False

def canMoveFrom(from_pos,player):
	if validPos(from_pos):
		if (player*game[int(from_pos[0])][int(from_pos[1])])>0:
			return True
		elif (player*game[int(from_pos[0])][int(from_pos[1])])<0:
			print("\nCannot move opponent's piece. \n")
			return False
		else:
			print("\nThe position is empty. \n")
			return False
	# return True

def canMoveTo(from_pos,to_pos,player):
	currentPiece=game[int(from_pos[0])][int(from_pos[1])]
	fromY=int(from_pos[0])
	fromX=int(from_pos[1])
	toY=int(to_pos[0])
	toX=int(to_pos[1])
	pieceAtToPosition=game[toY][toX]
	if 0<abs(currentPiece)<=8:return canMovePawn(fromX,fromY,toX,toY,pieceAtToPosition,player)
	if abs(currentPiece)==9 or abs(currentPiece)==16:return canMoveRook(fromX,fromY,toX,toY,pieceAtToPosition,player)
	if abs(currentPiece)==10 or abs(currentPiece)==15:return canMoveKnight(fromX,fromY,toX,toY,pieceAtToPosition,player)
	if abs(currentPiece)==11 or abs(currentPiece)==14:return canMoveBishop(fromX,fromY,toX,toY,pieceAtToPosition,player)
	if abs(currentPiece)==12:return canMoveQueen(fromX,fromY,toX,toY,pieceAtToPosition,player)
	if abs(currentPiece)==13:return canMoveKing(fromX,fromY,toX,toY,pieceAtToPosition,player)

def canMovePawn(fromX,fromY,toX,toY,pieceAtToPosition,player):
	if player==1:
		if toX==fromX and pieceAtToPosition==0:
			if (fromY==1 and toY==3) or (toY==fromY+1):
				return True
		if(toY==fromY+1 and (toX==fromX+1 or toX==fromX-1)and pieceAtToPosition<0):
			return True
	if player==-1:
		if toX==fromX and pieceAtToPosition==0:
			if (fromY==6 and toY==4) or (toY==fromY-1):
				return True
		if(toY==fromY-1 and (toX==fromX+1 or toX==fromX-1)and pieceAtToPosition>0):
			return True
	return invalidMove()

def invalidMove():
	print("Invalid move.\n\n")
	return False

def canMoveRook(fromX,fromY,toX,toY,pieceAtToPosition,player):
	if (player==-1 and pieceAtToPosition>=0) or (player==1 and pieceAtToPosition<=0):
		if toX==fromX:
			if fromY>toY:
				for y in range(toY+1,fromY):
					if not game[y][toX]==0:
						return invalidMove()
			if fromY<toY:
				for y in range(fromY+1,toY):
					if not game[y][toX]==0:
						return invalidMove()
			return True

		if toY==fromY: 
			if fromX>toX:
				for x in range(toX+1,fromX):
					if not game[toY][x]==0:
						return invalidMove()
			if fromX<toX:
				for x in range(fromX+1,toX):
					if not game[toY][x]==0:
						return invalidMove()
			return True
	return invalidMove()

def canMoveBishop(fromX,fromY,toX,toY,pieceAtToPosition,player):
	if (player==-1 and pieceAtToPosition>=0) or (player==1 and pieceAtToPosition<=0):
		if(abs(fromX-toX)==abs(fromY-toY)):
			if fromY>toY:
				if toX>fromX:
					for x in range(1,abs(fromY-toY)):
						if not game[fromX+x][fromY-x]==0:
							return invalidMove()
				if fromX>toX:
					for x in abs(fromY-toY):
						if not game[fromX-x][fromY-x]==0:
							return invalidMove()
				return True
			if fromY<toY:
				if toX>fromX:
					for x in range(1,abs(fromY-toY)):
						if not game[fromX+x][fromY+x]==0:
							return invalidMove()
				if fromX>toX:
					for x in abs(fromY-toY):
						if not game[fromX-x][fromY+x]==0:
							return invalidMove()
				return True
	return invalidMove()
			
def move(player,from_pos,to_pos):
	piece=game[int(from_pos[0])][int(from_pos[1])]
	game[int(to_pos[0])][int(to_pos[1])]=piece
	game[int(from_pos[0])][int(from_pos[1])]=0

while 1:
	os.system('cls')
	convert()
	display()
	while(not Input(-1)==1):
		pass
	os.system('cls')
	convert()
	display()
	while(not Input(1)==1):
		pass
	


