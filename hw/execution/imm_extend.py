import time
import numpy
from hw.conf.conf import clk


def imm_ext(option, in_x, in_y, out_z, out_x, out_y, out_zz, out_op):
    while True:

        op = option.get()
        a = in_x.get()
        b = in_y.get()

        time.sleep(clk)

        out_x.put(a)
        out_y.put(b)
        out_op.put(op)

        if op == '0':
            size = len(a)
            res = a[0] * (32 - size) + a
            out_z.put(res)
            out_zz.put(res)
        elif op == '1':
            size = len(b)
            res = b[0] * (32 - size) + b
            out_z.put(res)
            out_zz.put(res)
        else:
            res = 'XXXXXXXXXXXX'
            out_z.put(res)
            out_zz.put(res)

