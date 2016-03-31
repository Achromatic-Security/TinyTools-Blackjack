# -*- coding: utf-8 -*-
import time
import curses
import math
from random import randint

cardMap = {'c2':0,'c3':1,'c4':2,'c5':3,'c6':4,'c7':5,'c8':6,'c9':7,'c10':8,'cj':9,'cq':10,'ck':11,'ca':12}
cards = {'c2':0,'c3':0,'c4':0,'c5':0,'c6':0,'c7':0,'c8':0,'c9':0,'c10':0,'cj':0,'cq':0,'ck':0,'ca':0}
cardArray = ['2','3','4','5','6','7','8','9','10','j','q','k','a']
draw = []

cr1 = [".------.",".------.",".------.",".------.",".------.",".------.",".------.",".------.",".------.",".------.",".------.",".------.",".------."]
cr2 = ["|2.--. |","|3.--. |","|4.--. |","|5.--. |","|6.--. |","|7.--. |","|8.--. |","|9.--. |","|10--. |","|J.--. |","|Q.--. |","|K.--. |","|A.--. |"]
cr3 = ["| (\/) |","| :(): |","| :/\: |","| :/\: |","| (\/) |","| :(): |","| :/\: |","| :/\: |","| :/\: |","| :(): |","| (\/) |","| :/\: |","| (\/) |"]
cr4 = ["| :\/: |","| ()() |","| :\/: |","| (__) |","| :\/: |","| ()() |","| :\/: |","| (__) |","| :\/: |","| ()() |","| :\/: |","| :\/: |","| :\/: |"]
cr5 = ["| '--'2|","| '--'3|","| '--'4|","| '--'5|","| '--'6|","| '--'7|","| '--'8|","| '--'9|","| '--10|","| '--'J|","| '--'Q|","| '--'K|","| '--'A|"]
cr6 = ["`------'","`------'","`------'","`------'","`------'","`------'","`------'","`------'","`------'","`------'","`------'","`------'","`------'"]

cb1 = ".------."
cb2 = "| XXXX |"
cb3 = "| XXXX |"
cb4 = "| XXXX |"
cb5 = "| XXXX |"
cb6 = "`------'"

c1f1 = ".----.  "
c1f2 = "| XX |  "
c1f3 = "| XX |  "
c1f4 = "| XX |  "
c1f5 = "| XX |  "
c1f6 = "`----'  "

c2f1 = ".-.     "
c2f2 = "|X|     "
c2f3 = "|X|     "
c2f4 = "|X|     "
c2f5 = "|X|     "
c2f6 = "`-'     "

c3f1 = ".       "
c3f2 = "|       "
c3f3 = "|       "
c3f4 = "|       "
c3f5 = "|       "
c3f6 = "'       "

c4f1 = ".-.     "
c4f2 = "| |     "
c4f3 = "| |     "
c4f4 = "| |     "
c4f5 = "| |     "
c4f6 = "`-'     "

c5f1 = ".----.  "
c5f1 = "| .. |  "
c5f1 = "| () |  "
c5f1 = "| :: |  "
c5f1 = "| '' |  "
c5f1 = "`----'  "

c6f1 = ".------."
c6f1 = "|?.--. |"
c6f1 = "| (  ) |"
c6f1 = "| |  | |"
c6f1 = "| '--'?|"
c6f1 = "`------'"

suit = 0
decks = 1.0

def fillDraw():
	global decks
	global cardArray
	global cards
	global draw
	draw = []
	totalCards = 13 * decks * 4
	i = 0
	while i <= int(totalCards):
		k = randint(0,12)
		if cards['c' + cardArray[k]] < (4 * int(decks)):
			draw.append(cardArray[k])
			cards['c' + cardArray[k]] += 1 
			i += 1
			if i == 52:
				i += 1
	cards = {'c2':0,'c3':0,'c4':0,'c5':0,'c6':0,'c7':0,'c8':0,'c9':0,'c10':0,'cj':0,'cq':0,'ck':0,'ca':0}


def getCard(c):
	global cardMap
	global cards
	return cards[int(cardMap[c])]


def animateflip(card,x,y,curse):
	global cardMap
	global cards
	time.sleep(0.1)
	curse.addstr(y, x, c1f1)
	curse.addstr(y+1, x, c1f1)
	curse.addstr(y+2, x, c1f1)
	curse.addstr(y+3, x, c1f1)
	curse.addstr(y+4, x, c1f1)
	curse.addstr(y+5, x, c1f1)
	myscreen.refresh()
	time.sleep(0.1)
	curse.addstr(y, x, c2f1)
	curse.addstr(y+1, x, c2f1)
	curse.addstr(y+2, x, c2f1)
	curse.addstr(y+3, x, c2f1)
	curse.addstr(y+4, x, c2f1)
	curse.addstr(y+5, x, c2f1)
	myscreen.refresh()
	time.sleep(0.1)
	curse.addstr(y, x, c3f1)
	curse.addstr(y+1, x, c3f1)
	curse.addstr(y+2, x, c3f1)
	curse.addstr(y+3, x, c3f1)
	curse.addstr(y+4, x, c3f1)
	curse.addstr(y+5, x, c3f1)
	myscreen.refresh()
	time.sleep(0.1)
	curse.addstr(y, x, c4f1)
	curse.addstr(y+1, x, c4f1)
	curse.addstr(y+2, x, c4f1)
	curse.addstr(y+3, x, c4f1)
	curse.addstr(y+4, x, c4f1)
	curse.addstr(y+5, x, c4f1)
	myscreen.refresh()
	time.sleep(0.1)
	curse.addstr(y, x, c5f1)
	curse.addstr(y+1, x, c5f1)
	curse.addstr(y+2, x, c5f1)
	curse.addstr(y+3, x, c5f1)
	curse.addstr(y+4, x, c5f1)
	curse.addstr(y+5, x, c5f1)
	myscreen.refresh()
	time.sleep(0.1)
	curse.addstr(y, x, c6f1)
	curse.addstr(y+1, x, c6f1)
	curse.addstr(y+2, x, c6f1)
	curse.addstr(y+3, x, c6f1)
	curse.addstr(y+4, x, c6f1)
	curse.addstr(y+5, x, c6f1)
	myscreen.refresh()
	renderCard(card,x,y,curse)
	myscreen.refresh()



def renderCard(card,x,y,curse):
	global cardMap
	global cards
	if card != 'back':
		i = int(cardMap[card])
		curse.addstr(y, x, cr1[i])
		curse.addstr(y+1, x, cr2[i])
		curse.addstr(y+2, x, cr3[i])
		curse.addstr(y+3, x, cr4[i])
		curse.addstr(y+4, x, cr5[i])
		curse.addstr(y+5, x, cr6[i])
	else:
		curse.addstr(y, x, cb1)
		curse.addstr(y+1, x, cb2)
		curse.addstr(y+2, x, cb3)
		curse.addstr(y+3, x, cb4)
		curse.addstr(y+4, x, cb5)
		curse.addstr(y+5, x, cb6)

def renderMenu(curse):
	global stage
	if stage == 1:
		curse.addstr(16, 4, "1 - increase bet")
		curse.addstr(17, 4, "2 - decrease bet")
		curse.addstr(18, 4, "d - deal")
		curse.addstr(20, 4, "x - Exit")
		curse.addstr(20, 4, "")
	elif stage == 2:
		curse.addstr(16, 4, "h - Hit         ")
		curse.addstr(17, 4, "s - Stand       ")
		curse.addstr(18, 4, "                ")
#curse.addstr(18, 4, "1 - split")
		curse.addstr(20, 4, "x - Exit")
		curse.addstr(20, 4, "")
	elif stage == 3:
		curse.addstr(16, 4, "                ")
		curse.addstr(17, 4, "                ")
		curse.addstr(18, 4, "                ")
#curse.addstr(18, 4, "1 - split")
		curse.addstr(20, 4, "x - Exit")
		curse.addstr(20, 4, "")

def cScore(crd):
	cardVals = {'a':1,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'9':9,'10':10,'j':10,'q':10,'k':10}
	return cardVals[crd]

def resetCards(curse):
	r = "                                             "
	i = 4
	while i < 20:
		curse.addstr(i, 22, r)
		i += 1



myscreen = curses.initscr()
myscreen.border(0)
bet = 0
pot = 0
win = 0
bank = 200
stage = 1
k = ''
ci = 0
pdrawn = 0
ddrawn = 0
pscore = 0
dscore = 0
paces = 0
daces = 0

while 1:
	myscreen.addstr(2, 2, "BET: " + str(bet) + "      ")
	myscreen.addstr(2, 28, "BANK: " + str(bank) + "      ")
	myscreen.addstr(2, 52, "POT: " + str(pot) + "      ")
	renderMenu(myscreen)
	if k == ord('x'):
		curses.endwin()
		exit()
	if stage == 1:
		resetCards(myscreen)
		renderCard('back',22,14,myscreen)
		renderCard('back',31,14,myscreen)
		renderCard('back',22,4,myscreen)
		renderCard('back',31,4,myscreen)
		if k == ord('1'):
			if bet < 100:
				if (bank - 1) >= 0:
					bet += 1
					bank -= 1
					pot = bet * 2
		if k == ord('2'):
			if bet > 0:
				if (bank + 1) >= 0:
					bet -= 1
					bank += 1
					pot = bet * 2
		if k == ord('d'):
			if bet > 0:
				fillDraw()
				stage = 2
				pscore += cScore(draw[0]) + cScore(draw[1])
				animateflip('c' + draw[0],22,14,myscreen)
				animateflip('c' + draw[1],31,14,myscreen)
				if pscore == 21:
					myscreen.addstr(12, 15, "Player: 21!!!!    ")
					stage = 3
				else:
					myscreen.addstr(12, 15, "Player: " + str(pscore) + "       ")
				dscore = cScore(draw[2])
				animateflip('c' + draw[2],22,4,myscreen)
				myscreen.addstr(11, 15, "Dealer: " + str(dscore) + "       ")
				ci = 3
				pdrawn = 2
				ddrawn = 1
				#renderCard('back',31,4,myscreen)
				renderMenu(myscreen)
	elif stage == 2:
		if k == ord('h'):
			pos = (pdrawn * 9) + 22
			animateflip('c' + draw[ci],pos,14,myscreen)
			pscore += cScore(draw[ci])
			ci += 1
			pdrawn += 1
			if pscore < 21:
				myscreen.addstr(12, 15, "Player: " + str(pscore) + "       ")
			elif pscore == 21:
				myscreen.addstr(12, 15, "Player: 21!!!!    ")
				stage = 3
			else:
				bet = 0
				pot = 0
				myscreen.addstr(12, 15, "Player: BUST!!!          ")
				myscreen.addstr(11, 15, "Dealer: WINS!!!          ")
				dscore = 0
				pscore = 0
				stage = 1
		if k == ord('s'):
			stage = 3
	elif stage == 3:
		animateflip('c' + draw[ci],31,4,myscreen)
		dscore += cScore(draw[ci])
		myscreen.addstr(11, 15, "Dealer: " + str(dscore) + "       ")
		ci += 1
		ddrawn += 1
		stage = 4
		if dscore > 16 and dscore <= 21:
			stage = 5
		elif dscore > pscore and dscore <= 21:
			stage = 5
	elif stage == 4:
		pos = (ddrawn * 9) + 22
		animateflip('c' + draw[ci],pos,4,myscreen)
		dscore += cScore(draw[ci])
		myscreen.addstr(11, 15, "Dealer: " + str(dscore) + "       ")
		ci += 1
		ddrawn += 1
		if dscore > 16 and dscore <= 21:
			stage = 5
		elif dscore > pscore and dscore <= 21:
			stage = 5
		elif dscore > 21:
			myscreen.addstr(11, 15, "Dealer: BUST!!!          ")
			myscreen.addstr(12, 15, "Player: WINS!!!          ")
			stage = 1
			bank += pot
			bet = 0
			pot = 0
			dscore = 0
			pscore = 0
	elif stage == 5:
		if dscore == pscore:
			myscreen.addstr(11, 15, "Dealer: DRAW!!!          ")
			myscreen.addstr(12, 15, "Player: DRAW!!!          ")
			stage = 1
			bank += bet
			bet = 0
			pot = 0	
		elif dscore > pscore:
			myscreen.addstr(12, 15, "Player: LOST!!!          ")
			myscreen.addstr(11, 15, "Dealer: WINS!!!          ")
			stage = 1
			bet = 0
			pot = 0

		elif dscore < pscore:
			myscreen.addstr(12, 15, "Player: WINS!!!          ")
			myscreen.addstr(11, 15, "Dealer: LOST!!!          ")	
			stage = 1
			bank += pot
			bet = 0
			pot = 0
		dscore = 0
		pscore = 0

	myscreen.refresh()
	k = myscreen.getch()
