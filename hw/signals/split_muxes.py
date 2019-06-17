import time
from hw.conf.conf import clk as _clk


def split_muxes(selector, sel_1, sel_2):
    while True:

        a = selector.get()

        time.sleep(_clk)

        sel_1.put(a[1])
        sel_2.put(a[0])
