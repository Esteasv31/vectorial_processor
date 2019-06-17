import time
from hw.conf.conf import clk


def mux2(selector, in_x, in_y, in_u, in_v, out_z, out_x, out_y, out_u, out_v, out_zz, out_sel):
    while True:

        sel = selector.get()  # GET INPUT FROM QUEUE
        a = in_x.get()  # GET INPUT FROM QUEUE
        b = in_y.get()  # GET INPUT FROM QUEUE
        c = in_u.get()  # GET INPUT FROM QUEUE
        d = in_v.get()  # GET INPUT FROM QUEUE

        time.sleep(clk)  # SLEEP FOR SYNC PROCESS

        out_x.put(a)  # WRITE VALUE TO CONTROL SIGNALS
        out_y.put(b)  # WRITE VALUE TO CONTROL SIGNALS
        out_u.put(c)  # WRITE VALUE TO CONTROL SIGNALS
        out_v.put(d)  # WRITE VALUE TO CONTROL SIGNALS
        out_sel.put(sel)

        if sel == '1':
            out_z.put(a)  # WRITE THE OUTPUT VALUE
            out_zz.put(a)
        elif sel == '2':
            out_z.put(b)  # WRITE THE OUTPUT VALUE
            out_zz.put(b)
        elif sel == '3':
            out_z.put(c)  # WRITE THE OUTPUT VALUE
            out_zz.put(c)
        elif sel == '4':
            out_z.put(d)  # WRITE THE OUTPUT VALUE
            out_zz.put(d)
        else:
            out_z.put("XXXXXXXX")  # WRITE THE OUTPUT VALUE
            out_zz.put("XXXXXXXX")
