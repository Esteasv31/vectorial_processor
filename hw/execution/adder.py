import time
from hw.conf.conf import clk


def adder(in_x, out_z, out_x, out_y, out_zz):
    while True:
        a = in_x.get()   # GET INPUT FROM QUEUE
        b = 1            # SET DEFAULT VALUE

        time.sleep(clk)  # SLEEP FOR SYNC PROCESS

        out_x.put(a)     # WRITE VALUE TO CONTROL SIGNALS
        out_y.put(b)     # WRITE VALUE TO CONTROL SIGNALS

        c = a + b        # CALC THE OUTPUT

        out_z.put(c)     # WRITE THE OUTPUT VALUE
        out_zz.put(c)    # WRITE THE OUTPUT VALUE
