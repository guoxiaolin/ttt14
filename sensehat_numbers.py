import font_smalltalk
import time
from sense_hat import SenseHat

numbers = font_smalltalk.font_smalltalk

red = (255, 0, 0)
white = (0, 0, 0)

enlarged_numbers = []
for number in numbers:
	enlarged_number = [];
	enlarged_number.append([0, 0, 0, 0, 0, 0, 0, 0])
	enlarged_number.append([0, 0, 0, 0, 0, 0, 0, 0])
	for i in range(0, len(number)):
		enlarged_number.append([0, 0, 0] + number[i] + [0, 0])
	enlarged_number.append([0, 0, 0, 0, 0, 0, 0, 0])

	for i in range(0, len(enlarged_number)):
		enlarged_number[i] = [white if x == 0 else red for x in enlarged_number[i]]

	enlarged_numbers.append(enlarged_number)

# for n in enlarged_numbers:
# 	for line in n:
# 		print line
# 	print

sense = SenseHat()
sense.clear()

while True:
	for i in range (0, len(enlarged_numbers)):
		sense.set_pixels(sum(enlarged_numbers[i],[]))
		time.sleep(0.5)
