import sense_hat
from sense_hat import SenseHat
import time
from enum import Enum

class Colors(Enum):
    Green = (0, 255, 0)
    Yellow = (255, 255, 0)
    Blue = (0, 0, 255)
    Red = (255, 0, 0)
    White = (255,255,255)
    Nothing = (0,0,0)
    Pink = (255,105, 180)
    Orange = (255,165, 0)

class DisplayManager(object):
    def __raspberry(self):
        G = Colors.Green.value
        N = Colors.Nothing.value
        R = Colors.Red.value
        logo = [
        N, G, G, N, N, G, G, N, 
        N, N, G, G, G, G, N, N,
        N, N, R, R, R, R, N, N, 
        N, R, R, R, R, R, R, N,
        R, R, R, R, R, R, R, R,
        R, R, R, R, R, R, R, R,
        N, R, R, R, R, R, R, N,
        N, N, R, R, R, R, N, N,
        ]
        return logo

    def __lego(self):
        W = Colors.White.value
        R = Colors.Red.value
        Y = Colors.Yellow.value
        logo = [
        R, Y, Y, Y, Y, R, R, R, 
        R, Y, W, W, Y, R, R, R,
        R, Y, W, W, Y, R, R, R, 
        R, Y, W, W, Y, R, R, R,
        R, Y, W, W, Y, Y, Y, R,
        R, Y, W, W, W, W, Y, R,
        R, Y, W, W, W, W, Y, R,
        R, Y, Y, Y, Y, Y, Y, R,
        ]
        return logo

    def __figure(self):
        N = Colors.Nothing.value
        Y = Colors.Yellow.value
        B = Colors.Blue.value
        R = Colors.Red.value
        logo = [
        N, N, N, N, N, N, N, N,
        N, N, Y, Y, Y, Y, N, N,
        N, Y, Y, Y, Y, Y, Y, N,
        N, Y, B, Y, Y, B, Y, N,
        N, Y, Y, Y, Y, Y, Y, N,
        N, Y, R, Y, Y, R, Y, N,
        N, N, Y, R, R, Y, N, N, 
        N, N, N, Y, Y, N, N, N,
        ]
        return logo

    def __red4x2(self):
        N = Colors.Nothing.value
        Y = Colors.Red.value
        logo = [
        N, N, N, N, N, N, N, N,
        N, N, N, N, N, N, N, N,
        Y, N, Y, N, Y, N, Y, N,
        Y, Y, Y, Y, Y, Y, Y, N,
        Y, Y, Y, Y, Y, Y, Y, N,
        Y, Y, Y, Y, Y, Y, Y, N,
        N, N, N, N, N, N, N, N, 
        N, N, N, N, N, N, N, N,
        ]
        return logo

    def __yellow4x2(self):
        N = Colors.Nothing.value
        Y = Colors.Yellow.value
        logo = [
        N, N, N, N, N, N, N, N,
        N, N, N, N, N, N, N, N,
        Y, N, Y, N, Y, N, Y, N,
        Y, Y, Y, Y, Y, Y, Y, N,
        Y, Y, Y, Y, Y, Y, Y, N,
        Y, Y, Y, Y, Y, Y, Y, N,
        N, N, N, N, N, N, N, N, 
        N, N, N, N, N, N, N, N,
        ]
        return logo

    def __blue4x2(self):
        N = Colors.Nothing.value
        Y = Colors.Blue.value
        logo = [
        N, N, N, N, N, N, N, N,
        N, N, N, N, N, N, N, N,
        Y, N, Y, N, Y, N, Y, N,
        Y, Y, Y, Y, Y, Y, Y, N,
        Y, Y, Y, Y, Y, Y, Y, N,
        Y, Y, Y, Y, Y, Y, Y, N,
        N, N, N, N, N, N, N, N, 
        N, N, N, N, N, N, N, N,
        ]
        return logo

    def __red2x2(self):
        N = Colors.Nothing.value
        Y = Colors.Red.value
        logo = [
        N, N, N, N, N, N, N, N,
        N, Y, Y, N, N, Y, Y, N,
        N, Y, Y, Y, Y, Y, Y, N,
        N, Y, Y, Y, Y, Y, Y, N,
        N, Y, Y, Y, Y, Y, Y, N,
        N, Y, Y, Y, Y, Y, Y, N,
        N, N, N, N, N, N, N, N, 
        N, N, N, N, N, N, N, N,
        ]
        return logo

    def __yellow2x2(self):
        N = Colors.Nothing.value
        Y = Colors.Yellow.value
        logo = [
        N, N, N, N, N, N, N, N,
        N, Y, Y, N, N, Y, Y, N,
        N, Y, Y, Y, Y, Y, Y, N,
        N, Y, Y, Y, Y, Y, Y, N,
        N, Y, Y, Y, Y, Y, Y, N,
        N, Y, Y, Y, Y, Y, Y, N,
        N, N, N, N, N, N, N, N, 
        N, N, N, N, N, N, N, N,
        ]
        return logo

    def __blue2x2(self):
        N = Colors.Nothing.value
        Y = Colors.Blue.value
        logo = [
        N, N, N, N, N, N, N, N,
        N, Y, Y, N, N, Y, Y, N,
        N, Y, Y, Y, Y, Y, Y, N,
        N, Y, Y, Y, Y, Y, Y, N,
        N, Y, Y, Y, Y, Y, Y, N,
        N, Y, Y, Y, Y, Y, Y, N,
        N, N, N, N, N, N, N, N, 
        N, N, N, N, N, N, N, N,
        ]
        return logo

    def __unknown(self):
        N = Colors.Nothing.value
        R = Colors.Red.value
        logo = [
        N, N, N, R, R, N, N, N,
        N, N, R, N, N, R, N, N,
        N, R, N, N, N, N, R, N,
        N, R, N, N, N, N, R, N,
        N, N, R, N, N, R, N, N,
        N, N, N, N, R, N, N, N,
        N, N, N, N, N, N, N, N,
        N, N, N, N, R, N, N, N,
        ]
        return logo

    def __init__(self):
        self.s = SenseHat()
        self.s.low_light = True
        self.__displayImage(self.__raspberry())#Flash the raspberry pi logo at initialization
        time.sleep(1)
        self.s.clear()

    def __displayImage(self, image):
        self.s.set_pixels(image)

    def displayImage(self, strImage):
        print("Displaying " + strImage)
        if 'yellow-4x2' in strImage.lower():
            self.__displayImage(self.__yellow4x2())
        elif 'yellow-2x2' in strImage.lower():
            self.__displayImage(self.__yellow2x2())
        elif 'red-4x2' in strImage.lower():
            self.__displayImage(self.__red4x2())
        elif 'red-2x2' in strImage.lower():
            self.__displayImage(self.__red2x2())
        elif 'blue-4x2' in strImage.lower():
            self.__displayImage(self.__blue4x2())
        elif 'blue-2x2' in strImage.lower():
            self.__displayImage(self.__blue2x2())
        elif 'figure' in strImage.lower():
            self.__displayImage(self.__figure())
        elif 'none' in strImage.lower():
            self.__displayImage(self.__lego())
        else:
            self.__displayImage(self.__lego())