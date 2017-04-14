from ..rng import RNG
from .geometry import Point, Rectangle, Edge, distance, midpoint

class Map():
	def __init__(self, width, height, rng):
		self.width = width
		self.height = height
		self.grid = [[0 for y in range(height)] for x in range(width)]

		self.rng = rng
		if self.rng == 0:
			self.rng = RNG()

		self.directions = (Point(-1, 0), Point(1, 0), Point(0, -1), Point(0, 1))

	def carve_space(self, left, top, width, height):
		for x in range(left, left + width):
			for y in range(top, top + height):
				self.grid[x][y] = 1

	def create_hall(self, room1, room2, hall_width):
		half_width = hall_width // 2
		halls = []

		if room1.center().x == room2.center().x:
			halls.append(
				Rectangle(
					int(room1.center().x) - half_width,
					min(int(room1.center().y), int(room2.center().y)),
					hall_width,
					abs(int(room1.center().y) - int(room2.center().y))
				))

			return halls

		if room1.center().y == room2.center().y:
			halls.append(
				Rectangle(
					min(int(room1.center().x), int(room2.center().x)),
					int(room1.center().y) - half_width,
					abs(int(room1.center().x) - int(room2.center().x)),
					hall_width
				))

			return halls

		left_room = room1 if room1.center().x < room2.center().x else room2
		right_room = room2 if room1.center().x < room2.center().x else room1
		top_room = room1 if room1.center().y < room2.center().y else room2
		bottom_room = room2 if room1.center().y < room2.center().y else room1

		if self.rng.random() < 0.5:
			halls.append(
				Rectangle(
					int(left_room.center().x),
					int(left_room.center().y - half_width),
					int(right_room.center().x) - int(left_room.center().x) + half_width,
					hall_width
				))

			halls.append(
				Rectangle(
					int(right_room.center().x) - half_width,
					int(top_room.center().y),
					hall_width,
					int(bottom_room.center().y) - int(top_room.center().y) + half_width
				))
		else:
			halls.append(
				Rectangle(
					int(top_room.center().x) - half_width,
					int(top_room.center().y),
					hall_width,
					int(bottom_room.center().y) - int(top_room.center().y) + half_width
				))

			halls.append(
				Rectangle(
					int(left_room.center().x),
					int(bottom_room.center().y) - half_width,
					int(right_room.center().x) - int(left_room.center().x),
					hall_width
				))

		return halls

	def get_gabriel_graph(self, rooms):
		edges = []

		for a in range(len(rooms) - 1):
			roomA = rooms[a]

			for b in range(a + 1, len(rooms)):
				roomB = rooms[b]
				mp = midpoint(roomA.center(), roomB.center())
				radius = distance(roomA.center(), mp)
				skip_edge = False

				for c in range(len(rooms)):
					if c == a or c == b:
						continue

					roomC = rooms[c]
					if distance(mp, roomC.center()) <= radius:
						skip_edge = True
						break

				if not skip_edge:
					edges.append(Edge(roomA, roomB))

		return edges