import random

class Car():
	def __init__(self, time):
		self.timestamp = time
		self.cars = random.randrange(1,3)

	def get_stmap(self):
		return self.timestamp

	def get_cars(self):
		return self.cars

	def wait_time(self, current_time):
		return current_time - self.timestamp