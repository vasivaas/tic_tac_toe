#!/usr/bin/env python
# -*- coding: utf-8 -*-

#step1 - drawing board game
board = [element for element in xrange(1,10)]
def drawing_board(board):
	print "*************"
	for index in xrange(3):
		print "|", board[0+index*3], "|", board[1+index*3], "|", board[2+index*3], "|"
		print "*************"

#step2 - takes in a players input
players = {'player1':'X', 'player2':'O'}
l = []
for k in players:
	l.append(k)
def player1_input():
	wr_data = False
	while not wr_data:
		print "Makes a move {x}".format(x=l[1])
		in_data = raw_input("Where to make your move - {0}? ".format(players['player1']))
		try:
			in_data = int(in_data)
		except:
			print "Incorrect input. Please enter a number"
			continue
		if in_data >= 1 and in_data <= 9:
			if str(board[in_data-1]) != "X" and str(board[in_data-1]) != "O":
				board[in_data - 1] = players['player1']
				wr_data = True
			else:
				print "You cannot move here. The place is already occupied"
		else:
			print "Incorrect input. Please enter a number range 1 to 9 inclusive"

def player2_input():
	wr_data = False
	while not wr_data:
		print "Makes a move {x}".format(x=l[0])
		in_data = raw_input("Where to make your move - {0}? ".format(players['player2']))
		try:
			in_data = int(in_data)
		except:
			print "Incorrect input. Please enter a number"
			continue
		if in_data >= 1 and in_data <= 9:
			if str(board[in_data-1]) != "X" and str(board[in_data-1]) != "O":
				board[in_data-1] = players['player2']
				wr_data = True
			else:
				print "You cannot move here. The place is already occupied"
		else:
			print "Incorrect input. Please enter a number range 1 to 9 inclusive"
			
#step3 - checked game board for check stop game
def check_win(board):
			win_koordinate = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
			for elem in win_koordinate:
				if board[elem[0]] == board[elem[1]] == board[elem[2]]:
					return board[elem[0]]
			return False
			
#step4  -  start game process
def start_game(board):
	stop_game = False
	count = 0
	while not stop_game:
		drawing_board(board)
		if count % 2 == 0:
			player1_input()
		else:
			player2_input()
		count += 1
		if count > 4:
			symbol = check_win(board)
			if symbol:
				print "Winning the player you played for - {e} !".format(e=symbol)
				stop_game = True
				break
			if count == 9:
				print "Whoops, this time it's a draw :)"
				break
	drawing_board(board)
		
start_game(board)	
	
