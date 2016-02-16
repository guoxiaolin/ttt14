# TODO: decide holidays

import datetime
# from datetime import datetime
from time import strftime

class tram14:

    def __init__(self, datafile="tram14.dat"):

        # public variables
        # self.datafile = "tram14.dat"

        # private variables
        self.__datafile = datafile
        self.__timetable = self.__generate_timetable()
        self.__timetable_kind = 4 # 0. Monday-Thursday 1. Friday 2. Saturday 3. Sunday and holiday

    def __generate_timetable(self):
        timetable = []
        timetable.append(self.__read_timetable(segment=1, suffix=['a', 'c', 'd']))
        timetable.append(self.__read_timetable(segment=1, suffix=['b', 'c', 'd']))
        timetable.append(self.__read_timetable(segment=2, suffix=['c', 'd']))
        timetable.append(self.__read_timetable(segment=3, suffix=['c', 'd']))
        return timetable

    # a segment starts with line "h ..." and ends with an empty line ""
    def __read_segment(self, segment):
        current_segment = 0
        data = []
        with open(self.__datafile) as f:
            for line in f:
                if line[0] == 'h':
                    current_segment = current_segment + 1
                    continue
                if current_segment == segment:
                    if line == '\n':
                        break
                    else:
                        data.append((line[:-1]).split(' '))
        return data

    # if the first entry in a line is like '10-12' we need to make three lines out of it
    # ['10', ...], ['11', ...] and ['12', ...]
    def __collapse_hour(self, data):
        data1 = []
        for line in data:
            if '-' in line[0]:
                start_hour, end_hour = line[0].split('-')
                for h in range(int(start_hour), int(end_hour) + 1):
                    new_line = [str(h)] + line[1:]
                    data1.append(new_line)
            else:
                data1.append(line)
        return data1        

    def __read_timetable(self, segment, suffix=''):
        data = self.__read_segment(segment)
        data = self.__collapse_hour(data)

        # process suffix

        # len(x) == 2 means pure digits, and we suppose there are at most two suffix
        f = lambda x: len(x) <= 2 or x[2] in suffix or (len(x) == 4 and x[3] in suffix)
        data = [[x[0:2] for x in line if f(x)] for line in data]
        
        # convert hour and minute to datatime.time()
        data = [datetime.datetime.strptime(line[0]+':'+x, '%H:%M').time() for line in data for x in line[1:]]
        return data

    def time_left(self, current_time):
        day = current_time.weekday()
        if (day <= 4):
            L = self.__timetable[0]
        elif (day == 5):
            L = self.__timetable[1]
        elif (day == 6):
            L = self.__timetable[2]
        else:
            L = self.__timetable[3]

        hour_minute = str(current_time.hour) + ':' + str(current_time.minute)
        hour_minute = datetime.datetime.strptime(hour_minute, '%H:%M').time()
        idx = next(i for i,v in enumerate(L) if v > hour_minute)
        if (idx >= len(L)):
            idx = 0

        dt1 = datetime.timedelta(hours=L[idx].hour, minutes=L[idx].minute, seconds=L[idx].second, microseconds=L[idx].microsecond)
        dt2 = datetime.timedelta(hours=hour_minute.hour, minutes=hour_minute.minute, seconds=hour_minute.second, microseconds=hour_minute.microsecond)
        diff = dt1 - dt2

        return (diff.seconds//60)%60
