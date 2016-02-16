import font_smalltalk
from sense_hat import SenseHat

class SenseShow:
    def __init__(self):
        self.__font = font_smalltalk.font_smalltalk
        self.__numbers = self.__font
        self.sense = SenseHat()
        self.sense.clear()

    def show(self, num):
        red = (100, 0, 0)
        white = (0, 0, 0)

        if num > 99:
            num = 99

        if num >= 10:
            num1, num2 = divmod(num, 10)
            number1, number2 = self.__numbers[num1], self.__numbers[num2]
        else:
            number = self.__numbers[num]

        enlarged_number = [];
        enlarged_number.append([0, 0, 0, 0, 0, 0, 0, 0])
        enlarged_number.append([0, 0, 0, 0, 0, 0, 0, 0])
        for i in range(0, len(self.__numbers[0])):
            if num >= 10:
                enlarged_number.append([0] + number1[i] + [0] + number2[i])
            else:
                enlarged_number.append([0, 0, 0] + number[i] + [0, 0])
        enlarged_number.append([0, 0, 0, 0, 0, 0, 0, 0])

        for i in range(0, len(enlarged_number)):
            enlarged_number[i] = [white if x == 0 else red for x in enlarged_number[i]]

        self.sense.set_pixels(sum(enlarged_number,[]))

    def clear(self):
        self.sense.clear()

