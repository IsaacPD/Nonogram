from PIL import Image
from threading import Thread
from threading import Event
import time
import pixelate
import sys
import json

BLACK = 0
WHITE = 1

class ClockTimer(Thread):
	def __init__(self, event):
		Thread.__init__(self)
		self.stopped = event
		self.timer = 0
	
	def run(self):
		while not self.stopped.wait(1.0):
			self.timer += 1
	
class Game:
	def __init__(self, image):
		self.stop = Event()
		self.clock = ClockTimer(self.stop)

		self.won = False
		self.image = image
		self.rows, self.cols = image.size

		self.rhints = [[] for _ in range(self.rows)]
		self.chints = [[] for _ in range(self.cols)]

		self.board = [[0] * self.cols for _ in range(self.rows)]
		self.pboard = [[0] * self.cols for _ in range(self.rows)]
		self.guesses = dict()

		self.init()

	def init(self):
		pixels = self.image.getdata()
		row = 0
		col = 0

		rhi  = 0
		chi = [0 for _ in range(self.cols)]

		for r,g,b in pixels: 
			if r + g + b == BLACK:
				rhi += 1
				chi[col] += 1
				self.board[row][col] = BLACK
			else:
				self.board[row][col] = WHITE
				if chi[col] != 0:
					self.chints[col].insert(0, chi[col])
					chi[col] = 0
				if rhi != 0:
					self.rhints[row].insert(0, rhi)
					rhi = 0

			col += 1
			if col >= self.cols:
				if rhi != 0:
					self.rhints[row].insert(0, rhi)
					rhi = 0
				row += 1
				col = 0
		for i in range(len(chi)):
			if chi[i] != 0:
				self.chints[i].insert(0, chi[i])
	
	def make_guess(self, row, col, val):
		actual = self.board.get(row, col)

		self.guesses[(row, col)] = (actual == val)
		self.pboard[row][col] = val

		if self.win():
			self.stop.set()
			print(self.clock.timer)
			print("You Win")
			game.won = True

	def win(self):
		return self.board == self.pboard
	
	def __str__(self):
		return str(self.pboard)

if __name__ == '__main__':
	img = pixelate.pixelize(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
	game = Game(img)
	print(json.dumps(game.chints), end="|")
	print(json.dumps(game.rhints), end="|")
	print(game.rows, end="|")
	print(game.cols, end="|")
	print(json.dumps(game.board), end="")