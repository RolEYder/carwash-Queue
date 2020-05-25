class carWash:
	def __init__(self, car_per_min):
		self.cpm = car_per_min
		self.current_car = None 
		self.time_remaiming = 0

	def tick(self):
		if self.current_car != None:
			self.time_remaiming = self.time_remaiming - 1
			if self.time_remaiming <= 0:
				self.current_car = None

	def busy(self):
		if self.current_car != None:
			return True
		else:
			return False

	def start_next(self, new_car):
		self.current_car = new_car
		self.time_remaiming = new_car.get_cars()  * 60 / self.cpm
