import time
from hw.conf.conf import clk as _clk


def general_register(clk, w_enable, a1, a2, a3, wd3, r15, rd1, rd2,
                     out_clk, out_wen, out_a1, out_a2, out_a3, out_wd3, out_r15, out_rd1, out_rd2):

    reg_list = []
    for i in range(16):
        reg_list.append(0)

    while True:
        clock = clk.get()
        write = w_enable.get()
        pc = r15.get()

        time.sleep(_clk)

        out_clk.put(clock)
        out_wen.put(write)
        out_r15.put(pc)

        reg_list[15] = pc

        if clock == 0:
            if write == '1':
                a = int(a3.get(), 2)
                b = wd3.get()
                if a < 16:
                    reg_list[a] = b
                    out_a1.put('XXXXX')
                    out_a2.put('XXXXX')
                    out_a3.put(a)
                    out_wd3.put(b)
                    out_rd1.put('X' * 32)
                    out_rd2.put('X' * 32)
                else:
                    print('ERROR: GENERAL_REGISTERS write address out of bounds')
                    break
        else:
            a = int(a1.get(), 2)
            b = int(a2.get(), 2)
            rd1.put(reg_list[a])
            rd2.put(reg_list[b])
            out_a1.put(a)
            out_a2.put(b)
            out_a3.put('XXXXX')
            out_wd3.put('X' * 32)
            out_rd1.put(reg_list[a])
            out_rd2.put(reg_list[a])
