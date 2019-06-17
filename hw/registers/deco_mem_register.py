import time
from hw.conf.conf import clk as _clk


def deco_mem_register(clk, clear, reg_write_d, mem_to_reg, mem_write_d, alu_control_d, alu_src, rd1, rd2, a3, imm,
                                    rwd, mtr, mwd, acd, asrc, d1, d2, a1, immd,
                      out_clk, out_cls, out_reg_wd, out_mem_tr, aout_mem_wd, out_alu_cd, aout_alu_src, out_rd1, out_rd2,
                      out_a3, aout_imm, out_rwd, out_mtr, out_mwd, out_acd, out_asrc, out_d1, out_d2, out_a1, out_immd):
    count = 0
    rwd_list = []
    mtr_list = []
    mwd_list = []
    acd_list = []
    asr_list = []
    d1_list = []
    d2_list = []
    a1_list = []
    imm_list = []

    while True:
        clock = clk.get()
        cls = clear.get()

        time.sleep(_clk)

        out_clk.put(clock)
        out_cls.put(cls)

        if clock == 1:
            if cls == 0:
                if count == 0:
                    count += 1
                elif count == 1:
                    a = reg_write_d.get()
                    b = mem_to_reg.get()
                    c = mem_write_d.get()
                    d = alu_control_d.get()
                    e = alu_src.get()
                    f = rd1.get()
                    g = rd2.get()
                    h = a3.get()
                    i = imm.get()

                    rwd_list.append(a)
                    mtr_list.append(b)
                    mwd_list.append(c)
                    acd_list.append(d)
                    asr_list.append(e)
                    d1_list.append(f)
                    d2_list.append(g)
                    a1_list.append(h)
                    imm_list.append(i)

                    out_reg_wd.put(a)
                    out_mem_tr.put(b)
                    aout_mem_wd.put(c)
                    out_alu_cd.put(d)
                    aout_alu_src.put(e)
                    out_rd1.put(f)
                    out_rd2.put(g)
                    out_a3.put(h)
                    aout_imm.put(i)

                else:
                    a = reg_write_d.get()
                    b = reg_write_d.get()
                    c = mem_write_d.get()
                    d = alu_control_d.get()
                    e = alu_src.get()
                    f = rd1.get()
                    g = rd2.get()
                    h = a3.get()
                    i = imm.get()

                    rwd_list.append(a)
                    mtr_list.append(b)
                    mwd_list.append(c)
                    acd_list.append(d)
                    asr_list.append(e)
                    d1_list.append(f)
                    d2_list.append(g)
                    a1_list.append(h)
                    imm_list.append(i)

                    out_reg_wd.put(a)
                    out_mem_tr.put(b)
                    aout_mem_wd.put(c)
                    out_alu_cd.put(d)
                    aout_alu_src.put(e)
                    out_rd1.put(f)
                    out_rd2.put(g)
                    out_a3.put(h)
                    aout_imm.put(i)

                    a = rwd_list.pop(0)
                    b = mtr_list.pop(0)
                    c = mwd_list.pop(0)
                    d = acd_list.pop(0)
                    e = asr_list.pop(0)
                    f = d1_list.pop(0)
                    g = d2_list.pop(0)
                    h = a1_list.pop(0)
                    i = imm_list.pop(0)

                    rwd.put(a)
                    mtr.put(b)
                    mwd.put(c)
                    acd.put(d)
                    asrc.put(e)
                    d1.put(f)
                    d2.put(g)
                    a1.put(h)
                    immd.put(i)

                    out_rwd.put(a)
                    out_mtr.put(b)
                    out_mwd.put(c)
                    out_acd.put(d)
                    out_asrc.put(e)
                    out_d1.put(f)
                    out_d2.put(g)
                    out_a1.put(h)
                    out_immd.put(i)
            else:
                count = 0
                rwd_list = []
                mtr_list = []
                mwd_list = []
                acd_list = []
                asr_list = []
                d1_list = []
                d2_list = []
                a1_list = []
                imm_list = []
