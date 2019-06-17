import time
from hw.conf.conf import clk as _clk


def split_rd(rd, rd_1, rd_2, rd_3):
    while True:

        a = rd.get()

        time.sleep(_clk)

        rd_1.put(a)
        rd_2.put(a)
        rd_3.put(a)
