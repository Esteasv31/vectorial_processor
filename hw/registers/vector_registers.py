import time
from hw.conf.conf import clk as _clk


def vector_ser(a, rd, out_a, out_rd):
    while True:
        a0 = a.get()

        time.sleep(_clk)

        out_a.put(a0)
        rd.put(a0)
        out_rd.put(a0)


def vector_par(a0, a1, a2, a3, a4, a5, a6, a7, a8, rd,
               out_a0, out_a1, out_a2, out_a3, out_a4, out_a5, out_a6, out_a7, out_a8, out_rd):

    while True:
        a = a0.get()
        b = a1.get()
        c = a2.get()
        d = a3.get()
        e = a4.get()
        f = a5.get()
        g = a6.get()
        h = a7.get()
        i = a8.get()

        time.sleep(_clk)

        out_a0.put(a)
        out_a1.put(b)
        out_a2.put(c)
        out_a3.put(d)
        out_a4.put(e)
        out_a5.put(f)
        out_a6.put(g)
        out_a7.put(h)
        out_a8.put(i)

        data = [a, b, c, d, e, f, g, h, i]

        rd.put(data)
        out_rd.put(data)
