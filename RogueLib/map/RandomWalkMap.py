from .Map import Map

class Map_Generator(Map):
	def __init__(self, width = 100, height = 100, rng = 0):
		super().__init__(width, height, rng)

		self.min_floor_percentage = 0.35
		self.max_floor_percentage = 0.45
		self.high_direction_change_chance = 0.75
		self.min_high_direction_change_steps = 20
		self.max_high_direction_change_steps = 40
		self.low_direction_change_chance = 0.25
		self.min_low_direction_change_steps = 10
		self.max_low_direction_change_steps = 30

	## Setters

	def set_min_floor_percentage(self, percent):
		self.min_floor_percentage = percent

	def set_max_floor_percentage(self, percent):
		self.max_floor_percentage = percent

	def set_high_direction_change_chance(self, chance):
		self.high_direction_change_chance = chance

	def set_min_high_direction_change_steps(self, steps):
		self.min_high_direction_change_steps = steps

	def set_max_high_direction_change_steps(self, steps):
		self.max_high_direction_change_steps = steps

	def set_low_direction_change_chance(self, chance):
		self.low_direction_change_chance = chance

	def set_min_low_direction_change_steps(self, steps):
		self.min_low_direction_change_steps = steps

	def set_max_low_direction_change_steps(self, steps):
		self.max_low_direction_change_steps = steps

	## Methods

	def can_carve(self, x, y, dir):
		if x < 1 or y < 1 or x >= self.width or y >= self.height:
			return False

		edge_distance = 3
		if (x < edge_distance and dir.x == -1) or (y < edge_distance and dir.y == -1) or (x >= self.width - edge_distance and dir.x == 1) or (y >= self.height - edge_distance and dir.y == 1):
			return self.rng.random() > 0.85

		edge_distance = 6
		if (x < edge_distance and dir.x == -1) or (y < edge_distance and dir.y == -1) or (x >= self.width - edge_distance and dir.x == 1) or (y >= self.height - edge_distance and dir.y == 1):
			return self.rng.random() > 0.5

		return True

	def carve(self, x, y):
		if self.grid[x][y] == 0:
			self.grid[x][y] = 1
			return True

		return False

	def generate(self):
		low_width = self.width // 4
		high_width = self.width - low_width
		low_height = self.height // 4
		high_height = self.height - low_height

		x = self.rng.random_range(low_width, high_width)
		y = self.rng.random_range(low_height, high_height)

		dir = self.directions[int(self.rng.random() * len(self.directions))]
		last_dir = dir

		floor_percentage = self.rng.random() * (self.max_floor_percentage - self.min_floor_percentage) + self.min_floor_percentage

		steps = 0
		floor_tiles = 0
		low_chance = False

		while floor_tiles / (self.width * self.height) < floor_percentage:
			if self.carve(x, y):
				floor_tiles += 1

			last_dir = dir
			steps -= 1

			if steps < 0:
				low_chance = self.rng.random() < 0.5
				if low_chance:
					steps = self.rng.random_range(self.min_low_direction_change_steps, self.max_low_direction_change_steps)
				else:
					steps = self.rng.random_range(self.min_high_direction_change_steps, self.max_high_direction_change_steps)

			if self.rng.random() < self.low_direction_change_chance if low_chance else self.high_direction_change_chance:
				dir = self.directions[int(self.rng.random() * len(self.directions))]
			else:
				dir = last_dir

			while not self.can_carve(x + dir.x, y + dir.y, dir):
				dir = self.directions[int(self.rng.random() * len(self.directions))]

			x += dir.x
			y += dir.y

		return self.grid