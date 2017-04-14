import pygame
from RogueLib.rng import RNG
from RogueLib.display import screen
from RogueLib.display.color import Color
from RogueLib.display.font import Font
from RogueLib.map.RandomWalkMap import Map_Generator

def main():
	SCREEN_WIDTH = 100
	SCREEN_HEIGHT = 100

	rng = RNG()
	# rng.set_seed("1492188932.5863888")
	# print(rng.get_seed())

	generator = Map_Generator(SCREEN_WIDTH, SCREEN_HEIGHT, rng)
	map = generator.generate()

	display = screen.Screen(SCREEN_WIDTH, SCREEN_HEIGHT, Font.ATI_8X8)
	display.set_default_fg(Color.YELLOW)
	display.set_default_bg(Color.DARK_GREEN)

	done = False
	clock = pygame.time.Clock()

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

		display.clear()

		## Text Testing Methods

		# display.put_char(('@', Color.WHITE, Color.BLACK), 5, 5)
		# for x in range(10,20):
		# 	for y in range(10,20):
		# 		display.put_char(('#', Color.GOLDENROD, Color.BLACK), x, y)

		# display.put_text_centered('Testing %c{RED}color%c{} codes', 22)

		# display.put_text_centered('%c{YELLOW}A long time ago,', 5)
		# display.put_text_centered('%c{YELLOW}in a galaxy far, far away...', 6)

		# display.put_text("This is text that should be wrapped in a narrow width", 1, 1, 15, 3)
		# display.put_rectangle(12, 12, 10, 10, Color.YELLOW, Color.BLUE, [chr(205), chr(186), chr(205), chr(186)] ,[chr(201), chr(187), chr(188), chr(200)])

		## Map Testing Methods
		wall = ('#', Color.GOLDENROD, Color.BLACK)
		floor = ('.', Color.WHITE, Color.BLACK)

		for x in range(SCREEN_WIDTH):
			for y in range(SCREEN_HEIGHT):
				display.put_char(wall if map[x][y] == 0 else floor, x, y)

		display.update()
		clock.tick(60)

if __name__ == '__main__':
	main()