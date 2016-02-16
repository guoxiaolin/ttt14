from tram14 import tram14
from datetime import datetime
from sense_show import SenseShow
import time

timetable = tram14()
show = SenseShow()

while True:
	show.show(timetable.time_left(datetime.today()))
	# print(timetable.time_left(datetime.today()))
	time.sleep(5)
