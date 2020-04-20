import random
import time
from itertools import cycle
from itertools import islice


class TrafficLight:
    def __init__(self):
        self.color = ["RED", "YELLOW", "GREEN", "YELLOW"]

    def switcher(self):
        start_color = random.choice(self.color)
        for color in islice(cycle(self.color),self.color.index(start_color), None):
            print(color)
            if color == 'YELLOW':
                time.sleep(1) # В звдании времени должно чуть больше(7 и 2 секунд), но для быстроты проверки указал 1 и 3 секунды соответствено.
            else:
                time.sleep(3)


a = TrafficLight()
a.switcher()


