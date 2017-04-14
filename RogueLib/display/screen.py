import pygame
import re
import os
import sys
from .font import Font
from .color import Color

class Screen():
	def __init__(self, width = 80, height = 24, font = Font.ATI_8X14):
		self.grid_width = width
		self.grid_height = height
		self.default_fg = Color.WHITE
		self.default_bg = Color.BLACK
		self.color_regex = re.compile(r'%([bc])\{([^}]*)\}')

		self.load_font(font)

	def check_bounds(self, x, y):
		if x < 0 or x >= self.grid_width:
			raise ValueError('The value of x must be within [0, ' + str(self.grid_width - 1) + ']')

		if y < 0 or y >= self.grid_height:
			raise ValueError('The value of y must be within [0, ' + str(self.grid_height - 1) + ']')

	def clear(self, color = 0, x = 0, y = 0, width = -1, height = -1):
		if color == 0:
			color = self.default_bg
			
		dx = x * self.glyph_width
		dy = y * self.glyph_height

		if width == -1:
			dwidth = (self.grid_width - x) * self.glyph_width
		else:
			dwidth = width * self.glyph_width

		if height == -1:
			dheight = (self.grid_height - y) * self.glyph_height
		else:
			dheight = height * self.glyph_height

		self.screen.fill(color.value, pygame.Rect(dx, dy, dwidth, dheight))

	def color_string_length(self, text):
		length = len(text)

		for m in self.color_regex.finditer(text):
			length -= m.end() - m.start()

		return length

	def get_glyph(self, glyph):
		index = ord(glyph[0])
		fg = glyph[1]
		bg = glyph[2]

		key = str(fg) + glyph[0] + str(bg)

		if not key in self.glyph_dictionary:
			glyph_img = self.glyph_array[index].make_surface()
			glyph_img_arr = pygame.PixelArray(glyph_img)
			if fg != Color.WHITE or bg != Color.BLACK:
				if fg == Color.BLACK:
					tempColor = Color.MAGENTA if bg != Color.MAGENTA else Color.CYAN
					glyph_img_arr.replace(Color.WHITE.value, tempColor.value)
					glyph_img_arr.replace(Color.BLACK.value, bg.value)
					glyph_img_arr.replace(tempColor.value, fg.value)
				else:
					glyph_img_arr.replace(Color.WHITE.value, fg.value)
					glyph_img_arr.replace(Color.BLACK.value, bg.value)

			self.glyph_dictionary[key] = glyph_img

		return self.glyph_dictionary[key]
		
	def load_font(self, font):
		self.glyph_width = font.value['width']
		self.glyph_height = font.value['height']
		self.glyph_dictionary = dict()

		self.screen_width = self.glyph_width * self.grid_width;
		self.screen_height = self.glyph_height * self.grid_height;

		size = (self.screen_width, self.screen_height)
		self.screen = pygame.display.set_mode(size)
		self.clear()

		glyph_image = pygame.image.load(os.path.join(os.path.dirname(sys.modules['RogueLib.display'].__file__), font.value['file'])).convert()
		glyph_matrix = pygame.PixelArray(glyph_image)

		self.glyph_array = []

		for i in range(256):
			x = (i % 16) * self.glyph_width
			y = (i // 16) * self.glyph_height

			self.glyph_array.append(glyph_matrix[x:x + self.glyph_width, y:y + self.glyph_height])

	def process_color_string(self, text):
		current_fg = self.default_fg
		current_bg = self.default_bg
		text_index = 0

		stubs = []

		for m in self.color_regex.finditer(text):
			text_stub = text[text_index:m.start()]
			stubs.append({'text': text_stub, 'fg': current_fg, 'bg': current_bg})
			if m.group(1) == 'b':
				if len(m.group(2)) == 0:
					current_bg = self.default_bg
				else:
					current_bg = Color[m.group(2)]
			else:
				if len(m.group(2)) == 0:
					current_fg = self.default_fg
				else:
					current_fg = Color[m.group(2)]

			text_index = m.end()

		text_stub = text[text_index:]
		stubs.append({'text': text_stub, 'fg': current_fg, 'bg': current_bg})

		return stubs

	def put_char(self, glyph, x, y):
		self.check_bounds(x, y)

		gx = x * self.glyph_width;
		gy = y * self.glyph_height;

		self.screen.blit(self.get_glyph(glyph), [gx, gy])

	def put_rectangle(self, x, y, width, height, fg = -1, bg = -1, walls = ['*', '*', '*', '*'], corners = ['*', '*', '*', '*'], fill = ' '):
		if fg == -1:
			fg = self.default_fg

		if bg == -1:
			bg = self.default_bg

		self.put_char((corners[0], fg, bg), x, y)
		self.put_char((corners[1], fg, bg), x + width - 1, y)
		self.put_char((corners[2], fg, bg), x + width - 1, y + height - 1)
		self.put_char((corners[3], fg, bg), x, y + height - 1)

		for i in range(1, width - 1):
			self.put_char((walls[0], fg, bg), x + i, y)
			self.put_char((walls[2], fg, bg), x + i, y + height - 1)

		for i in range(1, height - 1):
			self.put_char((walls[3], fg, bg), x, y + i)
			self.put_char((walls[1], fg, bg), x + width - 1, y + i)

		if fill != '':
			for i in range(1, width - 1):
				for j in range(1, height - 1):
					self.put_char((fill, fg, bg), x + i, y + j)

	def put_text(self, text, x = 0, y = 0, width = -1, height = -1):
		dx = 0
		dy = 0

		if width == -1:
			width = self.grid_width - x

		if height == -1:
			height = self.grid_height - y

		self.check_bounds(x, y)
		self.check_bounds(x + width - 1, y + height - 1)

		text_data = self.process_color_string(text)

		for i in range(len(text_data)):
			data = text_data[i]
			words = data['text'].split(' ')
			for j in range(len(words)):
				if (dx + len(words[j]) + (0 if j == 0 else 1)) > width:
					dx = 0
					dy += 1
					if dy == height:
						return

				if j > 0 and dx > 0:
					self.put_char((' ', data['fg'], data['bg']), dx + x, dy + y)
					dx += 1

				if len(words[j]) > 0:
					for k in range(len(words[j])):
						self.put_char((words[j][k], data['fg'], data['bg']), dx + x, dy + y)
						dx += 1

	def put_text_centered(self, text, y, x = 0, width = -1):
		if width == -1:
			width = self.grid_width - x

		length = self.color_string_length(text)
		dx = (width - length) // 2

		if dx < 0:
			dx = 0;

		self.put_text(text, dx + x, y, length, 1)

	def set_default_bg(self, bg):
		self.default_bg = bg

	def set_default_fg(self, fg):
		self.default_fg = fg

	def update(self):
		pygame.display.flip()
