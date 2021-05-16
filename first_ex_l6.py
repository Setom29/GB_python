import time


class TrafficLight:
    __color = 'green'

    def running(self):
        while True:
            self.__color = 'red'
            print(self.__color)
            time.sleep(7)
            self.__color = 'yellow'
            print(self.__color)
            time.sleep(2)
            self.__color = 'green'
            print(self.__color)
            time.sleep(10)
            self.__color = 'yellow'
            print(self.__color)
            time.sleep(2)


tl = TrafficLight()
tl.running()
