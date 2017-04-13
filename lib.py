import pygame
from RogueLib.display import screen, font
from RogueLib.display.color import Color

def main():
	display = screen.Screen()
	done = False
	clock = pygame.time.Clock()

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

		display.put_char(('@', Color.WHITE, Color.BLACK), 5, 5)
		for x in range(10,20):
			for y in range(10,20):
				display.put_char(('#', Color.GOLDENROD, Color.BLACK), x, y)

		display.put_text('Testing', 10, 22)

		display.update()
		clock.tick(60)

if __name__ == '__main__':
	main()