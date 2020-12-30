import pygame
import sys
import random
from tkinter import *
from tkinter import messagebox

class Main:
	def __init__(self):
		self.width = 600

		# setting score
		self.score = 0

		# Rect
		self.rect_x = 0
		self.rect_y = 0
		self.rect_width = 0
		self.rect_height = 0

		# Colors
		self.black = (0, 0, 0)
		self.red = (255, 0, 0)
		self.white = (255, 255, 255)
		self.green = (0, 255, 0)

		# Other stuff
		self.screen = pygame.display.set_mode((self.width, self.width))
		self.screen_caption = pygame.display.set_caption("Snake Game")
		self.score = 0
		self.clock = pygame.time.Clock()

	def update(self):
		pygame.display.update()
		self.clock.tick(10)

	def drawGrid(self, screen_width, box_size, display_surface):
		self.n_box = screen_width // box_size
		x = 0
		y = 0

		for i in range(box_size):
			x = x + self.n_box
			y = y + self.n_box

			pygame.draw.line(display_surface, self.white, (0, y), (self.width, y))
			pygame.draw.line(display_surface, self.white, (y, 0), (y, self.width))

	def redrawGrid(self):
		self.screen.fill(self.black)
		self.drawGrid(self.width, 30, self.screen)

	def quit(self):
		win = Tk()
		win.withdraw()
		messagebox.showinfo(title="Game Over", message=f"Score: {self.score}")
		print(self.score)
		pygame.quit()
		sys.exit()

class Snake(Main):
	def __init__(self):
		super().__init__()
		super().drawGrid(self.width, 30, self.screen)

		self.start_position_x = (self.width // 2) + 1
		self.start_position_y = (self.width // 2) + 1

		self.snakeLength = []
		self.snakeLengthAllowed = 0

		# Controls
		self.UP = (0, (self.n_box * -1))
		self.DOWN = (0, (self.n_box))
		self.LEFT = (self.n_box, 0)
		self.RIGHT = ((self.n_box * -1), 0)

	def draw_snake(self, SnakeList):
		self.block_width = self.n_box	
		self.block_width -= 1

		self.snakeHead = []
		self.snakeHead.append(self.start_position_x)
		self.snakeHead.append(self.start_position_y)
		self.snakeLength.append(self.snakeHead)

		for x in SnakeList:
			self.snake_rect = pygame.draw.rect(self.screen, self.red, [x[0], x[1], self.block_width, self.block_width])

		for y in SnakeList[:-1]:
			if y == self.snakeHead:
				self.quit()

		# Getting the coordinates of the head of the snake
		self.snake_head_pos = (self.snake_rect.top, self.snake_rect.left)

	def boundaries(self):
		# Adding boundaries to the game 
		if self.snakeHead[0] <= 0:
			self.snakeHead[0] = 1
			self.quit()

		if self.snakeHead[0] >= (self.width - 1):
			self.snakeHead[0] = (self.width - 19)
			self.quit()

		if self.snakeHead[1] <= 0:
			self.snakeHead[1] = 1
			self.quit()

		if self.snakeHead[1] >= (self.width - 1):
			self.snakeHead[1] = (self.width - 19)
			self.quit()

class Food(Snake):
	def __init__(self):
		# Inheriting all of the attributes of the Snake and Main class
		super().__init__()
		super().draw_snake(self.snakeLength)
		super().boundaries()

	def draw_food(self):
		# making sure that food fits in a square in the grid
		thing1 = round(random.randint(0, self.width)) 
		thing2 = round(random.randint(0, self.width)) 
		thing1 = int(20 * round(thing1/20)) + 1
		thing2 = int(20 * round(thing2/20)) + 1


		try:
			if self.random_x == self.random_y:
				pass
		except AttributeError:
			self.random_x = 21
			self.random_y = 21

		self.food = pygame.draw.rect(self.screen, self.green, [self.random_x, self.random_y, self.block_width, self.block_width])

		if len(self.snakeLength) > self.snakeLengthAllowed:
			self.snakeLength.pop(0)

		if self.snake_rect.colliderect(self.food) == True:
			self.score += 1
			self.random_x = thing1
			self.random_y = thing2
			self.snakeLengthAllowed += 1

	def game_loop(self):
		# pressed = pygame.key.get_pressed()	
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.quit()

			# handling currently pressed key
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					self.start_position_y += (self.n_box * -1)

				if event.key == pygame.K_DOWN:
					self.start_position_y += self.n_box

				if event.key == pygame.K_LEFT:
					self.start_position_x += (self.n_box * -1)

				if event.key == pygame.K_RIGHT:
					self.start_position_x += self.n_box

				if event.key == pygame.K_q:
					self.quit()

			# allows snake to continuously move in direction which was previously let go of
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					self.start_position_y += (self.n_box * -1)

				if event.key == pygame.K_DOWN:
					self.start_position_y += self.n_box

				if event.key == pygame.K_LEFT:
					self.start_position_x += (self.n_box * -1)

				if event.key == pygame.K_RIGHT:
					self.start_position_x += self.n_box

				if event.key == pygame.K_q:
					self.quit()

			self.redrawGrid()

			self.draw_food()
			self.draw_snake(self.snakeLength)
			self.boundaries()

			# updating the screen and setting fps
			food_class.update()



food_class = Food()

def main():
	pygame.init()

	# Setting up the screen
	food_class.screen
	food_class.screen_caption

	food_class.snakeLength

	food_class.game_loop()

if __name__ == '__main__':
	main()
