import time
from hw.conf.conf import clk


def clock(queue):
    while True:
        queue.put(0)

        time.sleep(clk)

        queue.put(1)

        time.sleep(clk)
