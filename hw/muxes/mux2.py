import time
from hw.conf.conf import clk


def mux2(selector, in_x, in_y, out_z, out_x, out_y, out_zz, out_sel):
    while True:

        sel = selector.get()   # GET INPUT FROM QUEUE
        a = in_x.get()   # GET INPUT FROM QUEUE
        b = in_y.get()   # GET INPUT FROM QUEUE

        time.sleep(clk)  # SLEEP FOR SYNC PROCESS

        out_x.put(a)     # WRITE VALUE TO CONTROL SIGNALS
        out_y.put(b)     # WRITE VALUE TO CONTROL SIGNALS
        out_sel.put(sel)

        if sel == '0':
            out_z.put(a)  # WRITE THE OUTPUT VALUE
            out_zz.put(a)
        elif sel == '1':
            out_z.put(b)  # WRITE THE OUTPUT VALUE
            out_zz.put(b)
        else:
            out_z.put("XXXXXXXX")  # WRITE THE OUTPUT VALUE
            out_zz.put("XXXXXXXX")


