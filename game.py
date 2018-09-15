from PIL import Image
from threading import Thread
from threading import Event
import time

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

		self.image = image
		self.rows, self.cols = image.size
		self.board = BitVector2D(self.cols, self.rows)
		self.pboard = BitVector2D(self.cols, self.rows)
		self.init()

	def init(self):
		pixels = self.image.getdata()
		row = 0
		col = 0
		for r,g,b in pixels:
			print(r,g,b)
			if r + g + b == BLACK:
				self.board.set(row, col, BLACK)
			else:
				self.board.set(row, col, WHITE)
			col += 1

			if col > self.cols:
				row += 1
				col = 0
	
	def make_guess(self, row, col, val):
		actual = self.board.get(row, col)
		self.pboard.set(row, col, val)

	def win(self):
		return self.board == self.pboard

img = Image.open('test.png', 'r')
game = Game(img)
l = len(bin(game.board.vector)) - 2