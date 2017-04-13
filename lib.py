import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

def main():
	pygame.init()

	size = (SCREEN_WIDTH, SCREEN_HEIGHT)
	screen = pygame.display.set_mode(size)

	done = False

	clock = pygame.time.Clock()
	glyph_matrix = pygame.image.load("cp437-ATI-8x14.png").convert()
	glyph_array = pygame.PixelArray(glyph_matrix)

	glyphTemp = glyph_array[0:8, 56:70] #.replace(WHITE, RED)
	glyphTemp.replace(WHITE, (128, 0, 0))
	glyphTemp.replace(BLACK, WHITE)
	glyph = glyphTemp.make_surface()




	# background_image.set_colorkey(BLACK)
	# glyph = pygame.Surface((8, 14))
	# glyph.set_colorkey(BLACK)
	# glyph.blit(background_image, (0, 0), pygame.Rect(0, 56, 8, 14))

	# glyph2_pa = pygame.PixelArray(glyph.copy())
	# glyph2_pa.replace(WHITE, RED);

	# glyph2 = glyph2_pa.make_surface()

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

		screen.fill(BLACK)



		screen.blit(glyph, [100, 100])
		# screen.blit(glyph2, [108, 100])

		pygame.display.flip()

		clock.tick(60)

	pygame.quit()


if __name__ == '__main__':
	main()