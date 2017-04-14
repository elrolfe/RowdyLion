import pygame
from RogueLib.display import screen
from RogueLib.display.color import Color

def main():
	display = screen.Screen()
	display.set_default_fg(Color.YELLOW)
	display.set_default_bg(Color.DARK_GREEN)

	done = False
	clock = pygame.time.Clock()

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

		display.clear()

		display.put_char(('@', Color.WHITE, Color.BLACK), 5, 5)
		for x in range(10,20):
			for y in range(10,20):
				display.put_char(('#', Color.GOLDENROD, Color.BLACK), x, y)

		display.put_text_centered('Testing %c{RED}color%c{} codes', 22)

		display.put_text_centered('%c{YELLOW}A long time ago,', 5)
		display.put_text_centered('%c{YELLOW}in a galaxy far, far away...', 6)

		display.put_text("This is text that should be wrapped in a narrow width", 1, 1, 15, 3)
		display.put_rectangle(12, 12, 10, 10, Color.YELLOW, Color.BLUE, [chr(205), chr(186), chr(205), chr(186)] ,[chr(201), chr(187), chr(188), chr(200)])

		display.update()
		clock.tick(60)

if __name__ == '__main__':
	main()