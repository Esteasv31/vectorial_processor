import time
from hw.conf.conf import clk as _clk


def split_add(add, add_1, add_2):
    while True:

        a = add.get()

        time.sleep(_clk)

        add_1.put(a)
        add_2.put(a)
