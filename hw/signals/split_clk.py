import time
from hw.conf.conf import clk as _clk


def split_clk(clk, clk_1, clk_2, clk_3, clk_4, clk_5, clk_6, clk_7):
    while True:

        a = clk.get()

        time.sleep(_clk)

        clk_1.put(a)
        clk_2.put(a)
        clk_3.put(a)
        clk_4.put(a)
        clk_5.put(a)
        clk_6.put(a)
        clk_7.put(a)
