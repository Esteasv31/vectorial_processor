import time
import numpy
from hw.conf.conf import clk as _clk


def instr_deco_register(clk, enable, clear, instrucF, instrucD, out_clk, out_en, out_clr, out_inf, out_ind):

    count = 0
    inst_list = []

    while True:
        en = enable.get()
        clock = clk.get()
        cls = clear.get()

        time.sleep(_clk)

        if en == 1:
            if cls == 0:
                if clock == 1 and count == 0:
                    z = numpy.binary_repr(0, 32)
                    instrucD.put(z)
                    out_ind.put(z)
                    out_en.put(en)
                    out_clk.put(clock)
                    out_clr.put(cls)
                    count += 1
                    a = instrucF.get()
                    inst_list.append(a)
                    out_inf.put(a)
                elif clock == 1 and count == 1:
                    z = inst_list.pop(0)
                    instrucD.put(z)
                    out_ind.put(z)
                    out_en.put(en)
                    out_clk.put(clock)
                    out_clr.put(cls)
                    a = instrucF.get()
                    inst_list.append(a)
                    out_inf.put(a)
            else:
                count = 0
                inst_list = []



