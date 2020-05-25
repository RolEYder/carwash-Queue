from Queue import *
from carWash import *
from Car import *
import random

def main(num_seconds, cars_per_minute):
	car_wash = carWash(cars_per_minute)
	queue = Queue()
	w_time = []

	for  second in range(num_seconds):
		car = Car(second)
		queue.enqueue(car)

		if new_car():
			cara = Car(second)
			queue.enqueue(cara)

		if (not car_wash.busy()) and (not queue.is_empty()):
			
			next_car = queue.dequeue()
			w_time.append(next_car.wait_time(second))
			car_wash.start_next(next_car)

		car_wash.tick()

	average_wait = sum(w_time) / len(w_time)

	print("Average wait %s secs %d cars remaining." % (average_wait, queue.size()))

def new_car():
	n = random.randrange(1, 30)
	if n == 30:
		return True
	else:
		return False

for i in range(10):
	main(100, 14)

