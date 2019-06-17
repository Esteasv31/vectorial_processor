import time
from hw.conf.conf import clk as _clk


def split_pc(pc, pc_1, pc_2):
    while True:

        a = pc.get()

        time.sleep(_clk)

        pc_1.put(a)
        pc_2.put(a)
