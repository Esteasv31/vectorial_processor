import time
from hw.conf.conf import clk as _clk


def pc(in_x, out_z, clk, enable, out_x, out_zz, out_clk, out_enable):

    count = 0
    inputs = []

    while True:

        clock = clk.get()
        en = enable.get()

        time.sleep(_clk)

        if en == 1:
            if clock == 1 and count == 0:
                out_z.put(0)
                out_zz.put(0)
                out_clk.put(clock)
                out_enable.put(en)
                count += 1
                a = in_x.get()
                out_x.put(a)
                inputs.append(a)
            elif clock == 1 and count == 1:
                b = inputs.pop(0)
                out_z.put(b)
                out_zz.put(b)
                out_clk.put(clock)
                out_enable.put(en)
                a = in_x.get()
                out_x.put(a)
                inputs.append(a)
        else:
            count = 0
            inputs = []

