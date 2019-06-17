import time
from hw.conf.conf import clk as _clk


def split_instruc(instruction, op, funct3, rd, rs1, rs2, imm1, imm2):
    while True:

        a = instruction.get()

        time.sleep(_clk)

        op.put(a[-7:])
        rd.put(a[-12:-7])
        funct3.put(a[-15:-12])
        rs1.put(a[-20:-15])
        rs2.put(a[-25:-20])
        imm1.put(a[:-20])
        imm2.put(a[:-25] + a[-12:-7])
