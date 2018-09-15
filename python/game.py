from PIL import Image
from threading import Thread
from threading import Event
import time
import pixelate
import sys

BLACK = 0
WHITE = 1

#2D BitVector For representing a 2D Boolean Array
class BitVector2D:
	def __init__(self, rows, cols):
		self.r = rows
		self.c = cols
		self.vector = (1 << (rows*cols)) - 1
	
	def get(self, row, col):
		pos = row * self.c + col
		return (self.vector >> pos) & 1

	def set(self, row, col, val):
		pos = row * self.c + col
		mask = 1 << pos

		if val == WHITE:
			self.vector |= mask
		elif val == BLACK:
			mask = ~mask
			self.vector &= mask
	
	def __str__(self):
		result = ''
		copy = self.vector
		for _ in range(self.r):
			for _ in range(self.c):
				result += str(copy & 1) + ' '
				copy = copy >> 1
			result += '\n'
		return result

	def __eq__(self, other):
		if not isinstance(other, BitVector2D):
			return False
		return self.vector == other.vector and self.c == other.c and self.r == other.r

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

		self.board = BitVector2D(self.cols, self.rows)
		self.pboard = BitVector2D(self.cols, self.rows)
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
				self.board.set(row, col, BLACK)
			else:
				self.board.set(row, col, WHITE)
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
		self.pboard.set(row, col, val)

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
	img = pixelate.pixelize(sys.argv[1])
	game = Game(img)
	print(game.chints, game.rhints, game.rows, game.cols, game.board.vector)