import queue
import threading

from hw.signals.clock import clock
from hw.registers.pc import pc
from hw.signals.split_clk import split_clk
from hw.execution.adder import adder
from hw.signals.split_pc import split_pc
from hw.memory.instruction_memory import use_instruc_mem
from hw.signals.split_adder import split_add
from hw.registers.instr_deco_register import instr_deco_register
from hw.signals.split_instruction import split_instruc
from hw.control.control_unit import control_unit
from hw.muxes.mux2 import mux2
from hw.signals.split_muxes import split_muxes
from hw.signals.split_rd import split_rd
from hw.execution.imm_extend import imm_ext
from hw.registers.general_registers import general_register
from hw.registers.deco_mem_register import deco_mem_register
from hw.memory.data_memory import use_data_mem
from hw.memory.load_store_unit import load_store_unit
from hw.registers.vector_registers import vector_par, vector_ser
from hw.registers.mem_exe_register import mem_exe_reg
from hw.execution.alu import alu

if __name__ == '__main__':
    """ Queues definition """

    # CLK
    aa = queue.Queue()  # 1 -> clock queue -> SPLIT_CLK

    # PC
    ab = queue.Queue()  # 2 -> in_x <- ADDER
    ac = queue.Queue()  # 3 -> out_z -> SPLIT_PC
    ad = queue.Queue()  # 4 -> CLK_1 <- SPLIT_CLK
    ae = queue.Queue()  # 5 -> enable <- ????
    af = queue.Queue()  # 6 -> out_x -> MONITOR
    ag = queue.Queue()  # 7 -> out_zz -> MONITOR
    ah = queue.Queue()  # 8 -> out_clk -> MONITOR
    ai = queue.Queue()  # 9 -> out_enable -> MONITOR

    # SPLIT_CLK
    ak = queue.Queue()  # 10 -> CLK_2 -> FETCH-DECODE
    al = queue.Queue()  # 11 -> CLK_3 -> REGISTERS
    am = queue.Queue()  # 12 -> CLK_4 -> DECO - MEM
    an = queue.Queue()  # 13 -> CLK_5 -> MEM - EXE
    at = queue.Queue()  # 19 -> CLK_6 -> EXE - WB
    fn = queue.Queue()  # 142 -> CLK_7 -> MEM

    # ADDER
    aj = queue.Queue()  # 14 -> out_x -> MONITOR
    ao = queue.Queue()  # 15 -> out_y -> MONITOR
    ap = queue.Queue()  # 16 -> out_zz -> MONITOR

    # SPLIT_PC
    aq = queue.Queue()  # 17 -> pc_1 - pc_1 -> ADDER
    ar = queue.Queue()  # 18 -> pc_2 - PC_2 -> INSTRUCTION_MEM

    # INSTRUCTION MEMORY
    au = queue.Queue()  # 19 -> rd -> FETC-DECODE-INSTRUC
    av = queue.Queue()  # 20 -> out_rd -> MONITOR
    aw = queue.Queue()  # 21 -> out_a -> MONITOR

    # SPLIT_ADDER
    ax = queue.Queue()  # 22 -> add_1 -> pc_register
    ay = queue.Queue()  # 23 -> add_2 -> general_registers

    # INSTRUCTION_DECO_REGISTER
    az = queue.Queue()  # 24 -> enable -> ?????
    ba = queue.Queue()  # 25 -> clear -> ????
    bb = queue.Queue()  # 26 -> instrucD -> SPLIT_INSTRUCTION
    bc = queue.Queue()  # 27 -> out_clok -> MONITOR
    bd = queue.Queue()  # 28 -> out_en -> MONITOR
    be = queue.Queue()  # 29 -> out_clr -> MONITOR
    bf = queue.Queue()  # 30 -> out_inf -> MONITOR
    bg = queue.Queue()  # 30 -> out_ind -> MONITOR

    # SPLIT_INSTRUCTION
    bh = queue.Queue()  # 31 -> op -> CONTROL_UNIT
    bi = queue.Queue()  # 32 -> funct3 -> CONTROL_UNIT
    bj = queue.Queue()  # 33 -> rd -> SPLIT_RD
    bk = queue.Queue()  # 34 -> rs1 -> MUX2_1
    bl = queue.Queue()  # 35 -> rs2 -> MUX2_2
    bm = queue.Queue()  # 36 -> imm1 -> EXTEND_SIGN
    bn = queue.Queue()  # 37 -> imm2 -> EXTEND_SIGN

    # CONTROL_UNIT
    bo = queue.Queue()  # 38 -> out_op -> MONITOR
    bp = queue.Queue()  # 39 -> out_funct -> MONITOR
    bq = queue.Queue()  # 40 -> out_rd -> MONITOR
    br = queue.Queue()  # 41 -> reg_write_d -> DECO_MEM_REG
    bs = queue.Queue()  # 42 -> out_reg_write_d -> MONITOR
    bt = queue.Queue()  # 43 -> mem_to_reg -> DECO_MEM_REG
    bu = queue.Queue()  # 44 -> out_mem_to_reg -> MONITOR
    bv = queue.Queue()  # 45 -> mem_write_d -> DECO_MEM_REG
    bw = queue.Queue()  # 46 -> out_mem_write_d -> MONIOR
    bx = queue.Queue()  # 47 -> alu_control_d -> DECO_MEM_REG
    by = queue.Queue()  # 48 -> out_alu_control_d -> MONITOR
    bz = queue.Queue()  # 49 -> alu_src -> DECO_MEM_REG
    ca = queue.Queue()  # 50 -> out_alu_src -> MONITOR
    cb = queue.Queue()  # 51 -> imm_src -> IMMEDIATE_EXTEND
    cc = queue.Queue()  # 52 -> out_imm_src -> MONITOR
    cd = queue.Queue()  # 53 -> reg_src_d -> SPLIT_MUXES
    ce = queue.Queue()  # 54 -> out_reg_src_d -> MONITOR

    # SPLIT_MUXES
    cf = queue.Queue()  # 55 -> sel_1 -> MUX2_1
    cg = queue.Queue()  # 56 -> sel_2 -> MUX2_2

    # SPLIT_RD
    ch = queue.Queue()  # 57 -> rd_1 -> CONTROL_UNIT
    ci = queue.Queue()  # 58 -> rd_2 -> MUX2_2
    cy = queue.Queue()  # 74 -> rd_3 -> DECO_MEM_REG

    # MUX2_1
    cj = queue.Queue()  # 59 -> out_z -> REGISTER_BANK
    ck = queue.Queue()  # 60 -> out_x -> MONITOR
    cl = queue.Queue()  # 61 -> out_y -> MONITOR
    cm = queue.Queue()  # 62 -> out_zz -> MONITOR
    cn = queue.Queue()  # 63 -> out_sel -> MONITOR

    # MUX2_2
    co = queue.Queue()  # 64 -> out_z -> REGISTER_BANK
    cp = queue.Queue()  # 65 -> out_x -> MONITOR
    cq = queue.Queue()  # 66 -> out_y -> MONITOR
    cr = queue.Queue()  # 67 -> out_zz -> MONITOR
    cs = queue.Queue()  # 68 -> out_sel -> MONITOR

    # IMMEDIATE_EXTEND
    ct = queue.Queue()  # 69 -> out_z -> DECO_MEM_REG
    cu = queue.Queue()  # 70 -> out_x -> MONITOR
    cv = queue.Queue()  # 71 -> out_y -> MONITOR
    cw = queue.Queue()  # 72 -> out_zz -> MONITOR
    cx = queue.Queue()  # 73 -> out_op -> MONITOR

    # GENERAL_REGISTERS
    cz = queue.Queue()  # 75 -> w_enable <- WB
    da = queue.Queue()  # 76 -> a3 <- WB
    db = queue.Queue()  # 77 -> wd3 <- WB
    dc = queue.Queue()  # 78 -> rd1 -> DECO_MEM_REG
    dd = queue.Queue()  # 79 -> rd2 -> DECO_MEM_REG
    de = queue.Queue()  # 80 -> out_clk -> MONITOR
    df = queue.Queue()  # 81 -> out_wen -> MONITOR
    dg = queue.Queue()  # 82 -> out_a1 -> MONITOR
    dh = queue.Queue()  # 83 -> out_a2 -> MONITOR
    di = queue.Queue()  # 84 -> out_a3 -> MONITOR
    dj = queue.Queue()  # 85 -> out_wd3 -> MONITOR
    dk = queue.Queue()  # 86 -> out_r15 -> MONITOR
    dl = queue.Queue()  # 87 -> out_rd1 -> MONITOR
    dm = queue.Queue()  # 88 -> out_rd2 -> MONITOR

    # DECO_MEM_REGISTER
    dn = queue.Queue()  # 89 -> clear ->
    do = queue.Queue()  # 90 -> rwd -> MEM_EXE_REG
    dp = queue.Queue()  # 91 -> mtr -> MEM_EXE_REG
    dq = queue.Queue()  # 92 -> mwd -> LOAD_STORE_UNIT
    dr = queue.Queue()  # 93 -> acd -> MEM_EXE_REG
    ds = queue.Queue()  # 94 -> asrc -> MEM_EXE_REG
    dt = queue.Queue()  # 95 -> d1 -> LOAD_STORE_UNIT
    du = queue.Queue()  # 96 -> d2 -> LOAD_STORE_UNIT
    dv = queue.Queue()  # 97 -> a1 -> MEM_EXE_REG
    dw = queue.Queue()  # 98 -> immd -> LOAD_STORE_UNIT
    dx = queue.Queue()  # 99 -> out_clk -> MONITOR
    dy = queue.Queue()  # 100 -> out_cls -> MONITOR
    dz = queue.Queue()  # 101 -> out_reg_wd -> MONITOR
    ea = queue.Queue()  # 102 -> out_mem_tr -> MONITOR
    eb = queue.Queue()  # 103 -> out_mem_wd -> MONITOR
    ec = queue.Queue()  # 104 -> out_alu_cd -> MONITOR
    ed = queue.Queue()  # 105 -> out_alu_src -> MONITOR
    ee = queue.Queue()  # 106 -> out_rd1 -> MONITOR
    ef = queue.Queue()  # 107 -> out_rd2 -> MONITOR
    eg = queue.Queue()  # 108 -> out_a3 -> MONITOR
    eh = queue.Queue()  # 109 -> out_imm -> MONITOR
    ei = queue.Queue()  # 110 -> out_rwd -> MONITOR
    ej = queue.Queue()  # 111 -> out_mtr -> MONITOR
    ek = queue.Queue()  # 113 -> out_mwd -> MONITOR
    el = queue.Queue()  # 114 -> out_acd -> MONITOR
    em = queue.Queue()  # 115 -> out_asrc -> MONITOR
    en = queue.Queue()  # 116 -> out_d1 -> MONITOR
    eo = queue.Queue()  # 117 -> out_d2 -> MONITOR
    ep = queue.Queue()  # 118-> out_a1 -> MONITOR
    eq = queue.Queue()  # 119 -> out_immd -> MONITOR

    # LOAD_STORE_UNIT
    er = queue.Queue()  # 120 -> mem_a -> DATA_MEM
    es = queue.Queue()  # 121 -> mem_b -> DATA_MEM
    et = queue.Queue()  # 122 -> mem_wd -> DATA_MEM
    eu = queue.Queue()  # 123 -> mem_we -> DATA_MEM
    ev = queue.Queue()  # 124 -> mem_rd1 <- DATA_MEM
    ew = queue.Queue()  # 125 -> mem_rd2 <- DATA_MEM
    ex = queue.Queue()  # 126 -> vec_1 -> VECTOR_SER_1
    ey = queue.Queue()  # 127 -> vec_2 -> VECTOR_SER_2
    ez = queue.Queue()  # 128 -> wb_data <- WRITE_BACK_MUX_1
    fa = queue.Queue()  # 129 -> wb_dir <- WRITE_BACK_MUX_2
    fb = queue.Queue()  # 130 -> out_a -> MONITOR
    fc = queue.Queue()  # 131 -> out_b -> MONITOR
    fd = queue.Queue()  # 132 -> out_mem_a -> MONITOR
    fe = queue.Queue()  # 133 -> out_mem_b -> MONITOR
    ff = queue.Queue()  # 134 -> out_mem_wd -> MONITOR
    fg = queue.Queue()  # 135 -> out_we -> MONITOR
    fh = queue.Queue()  # 136 -> out_mem_rd1 -> MONITOR
    fi = queue.Queue()  # 137 -> out_mem_rd2 -> MONITOR
    fj = queue.Queue()  # 138 -> out_vec_1 -> MONITOR
    fk = queue.Queue()  # 139 -> out_vec_2 -> MONITOR
    fl = queue.Queue()  # 140 -> out_wb_data -> MONITOR
    fm = queue.Queue()  # 141 -> out_eb_dir -> MONITOR
    ga = queue.Queue()  # 155 -> out_wtm -> MONITOR
    gb = queue.Queue()  # 156 -> num -> MEM_EXE_REG
    gc = queue.Queue()  # 157 -> out_num -> MONITOR

    # DATA_MEM
    fo = queue.Queue()  # 143 -> out_a -> MONITOR
    fp = queue.Queue()  # 144 -> out_b -> MONITOR
    fq = queue.Queue()  # 145 -> out_rd1 -> MONITOR
    fr = queue.Queue()  # 146 -> out_rd2 -> MONITOR
    fs = queue.Queue()  # 147 -> out_wd -> MONITOR
    ft = queue.Queue()  # 148 -> out_we -> MONITOR

    # VECTOR_SER_1
    fu = queue.Queue()  # 149 -> rd -> MEM_EXE_REG
    fv = queue.Queue()  # 150 -> out_a -> MONITOR
    fw = queue.Queue()  # 151 -> out_rd -> MONITOR

    # VECTOR_SER_2
    fx = queue.Queue()  # 152 -> rd -> MEM_EXE_REG
    fy = queue.Queue()  # 153 -> out_a -> MONITOR
    fz = queue.Queue()  # 154 -> out_rd -> MONITOR

    # MEM_EXE_REG
    gd = queue.Queue()  # 158 -> rwd ->
    ge = queue.Queue()  # 159 -> mtr ->
    gf = queue.Queue()  # 160 -> acd ->
    gg = queue.Queue()  # 161 -> asrc ->
    gh = queue.Queue()  # 162 -> v1 ->
    gi = queue.Queue()  # 163 -> v2 ->
    gj = queue.Queue()  # 164 -> n ->
    gk = queue.Queue()  # 165 -> im ->
    gl = queue.Queue()  # 166 -> out_rwd ->
    gm = queue.Queue()  # 167 -> out_mtr ->
    gn = queue.Queue()  # 168 -> out_acd ->
    go = queue.Queue()  # 169 -> out_asr ->
    gp = queue.Queue()  # 170 -> out_v1 ->
    gq = queue.Queue()  # 171 -> out_v2 ->
    gr = queue.Queue()  # 172 -> out_n ->
    gs = queue.Queue()  # 173 -> out_im ->
    gt = queue.Queue()  # 174 -> out_rwd_e ->
    gu = queue.Queue()  # 175 -> out_mtr_e ->
    gv = queue.Queue()  # 176 -> out_acd_e ->
    gw = queue.Queue()  # 177 -> out_asr_e ->
    gx = queue.Queue()  # 178 -> out_v1_e ->
    gy = queue.Queue()  # 179 -> out_v2_e ->
    gz = queue.Queue()  # 180 -> out_n_e ->
    ha = queue.Queue()  # 181 -> out_im_e ->

    """ Threads definition """

    # CLK
    thread_1 = threading.Thread(name='CLK', target=clock, args=aa)

    # PC
    thread_2 = threading.Thread(name='PC', target=pc, args=(ax, ac, ad, ae, af, ag, ah, ai))

    # SPLIT_CLK
    thread_3 = threading.Thread(name='SPLIT_CLK', target=split_clk, args=(aa, ad, ak, al, am, an, at, fn))

    # ADDER
    thread_4 = threading.Thread(name='ADDER', target=adder, args=(aq, ab, aj, ao, ap))

    # SPLIT_PC
    thread_5 = threading.Thread(name='SPLIT_PC', target=split_pc, args=(ac, aq, ar))

    # INSTRUCTION_MEM
    thread_6 = threading.Thread(name='INSTRUCTION_MEM', target=use_instruc_mem, args=(ar, au, aw, av))

    # SPLIT_ADDER
    thread_7 = threading.Thread(name='SPLIT_ADDER', target=split_add, args=(ab, ax, ay))

    # INSTRUCTION_DECO_REGISTER
    thread_8 = threading.Thread(name='INS_DECO_REG', target=instr_deco_register, args=(ak, az, ba, au, bb, bc, bd, be,
                                                                                       bf, bg))

    # SPLIT_INSTRUCTION
    thread_9 = threading.Thread(name='SPLIT_INS', target=split_instruc, args=(bb, bh, bi, bj, bk, bl, bm, bn))

    # CONTROL_UNIT
    thread_10 = threading.Thread(name='CONTROL_UNIT', target=control_unit, args=(bh, bi, ch, bo, bp, bq, br, bs, bt, bu,
                                                                                 bv, bw, bx, by, bz, ca, cb, cc, cd,
                                                                                 ce))

    # MUX2_1
    thread_11 = threading.Thread(name='MUX2_1', target=mux2, args=(cf, bk, '01111', cj, ck, cl, cm, cn))

    # MUX2_2
    thread_12 = threading.Thread(name='MUX2_2', target=mux2, args=(cg, bl, ci, co, cp, cq, cr, cs))

    # SPLIT_MUXES
    thread_13 = threading.Thread(name='SPLIT_MUXES', target=split_muxes, args=(cd, cf, cg))

    # SPLIT_RD
    thread_14 = threading.Thread(name='# SPLIT_RD', target=split_rd, args=(bj, ch, ci, cy))

    # IMMEDIATE_EXTEND
    thread_15 = threading.Thread(name='IMMEDIATE_EXTEND', target=imm_ext, args=(cb, bm, bn, ct, cu, cv, cw, cx))

    # GENERAL_REGISTERS
    thread_16 = threading.Thread(name='GENERAL_REGISTERS', target=general_register, args=(al, cz, cj, co, da, db, ay,
                                                                                          dc, dd, de, df, dg, dh, di,
                                                                                          dj, dk, dl, dm))

    # DECO_MEM_REGISTER
    thread_17 = threading.Thread(name='DECO_MEM_REGISTER', target=deco_mem_register, args=(am, dn, br, bt, bv, bx, bz,
                                                                                           dc, dd, cy, ct, do, dp, dq,
                                                                                           dr, ds, dt, du, dv, dw, dx,
                                                                                           dy, dz, ea, eb, ec, ed, ee,
                                                                                           ef, eg, eh, ei, ej, ek, el,
                                                                                           em, en, eo, ep, eq))

    # LOAD_STORE_UNIT
    thread_18 = threading.Thread(name='LOAD_STORE_UNIT', target=load_store_unit, args=(dt, du, dw, er, es, et, eu, ev,
                                                                                       ew, ex, ey, ez, fa, fb, fc, fd,
                                                                                       fe, ff, fg, fh, fi, fj, fk, fl,
                                                                                       fm, dq, ga, gb, gc))

    # DATA_MEM
    thread_19 = threading.Thread(name='DATA_MEM', target=use_data_mem, args=(fn, er, es, ev, ew, et, eu, fo, fp, fq, fr,
                                                                             fs, ft))

    # VECTOR_SER_1
    thread_20 = threading.Thread(name='VECTOR_SERIAL_1', target=vector_ser, args=(ex, fu, fv, fw))

    # VECTOR_SER_2
    thread_21 = threading.Thread(name='VECTOR_SERIAL_2', target=vector_ser, args=(ey, fx, fy, fz))

    # MEM_EXE_REG
    thread_22 = threading.Thread(name='MEM_EXE_REG', target=mem_exe_reg, args=(do, dp, dr, ds, fu, fx, gb, dv, gd, ge,
                                                                               gf, gg, gh, gi, gj, gk, gl, gm, gn, go,
                                                                               gp, gq, gr, gs, gt, gu, gv, gw, gx, gy,
                                                                               gz, ha))

    # MUX_EXE
    thread_23 = threading.Thread(name='MUX_EXE', target=mux2, args=())

    # ALU_1
    thread_24 = threading.Thread(name='ALU_1', target=alu, args=())

    # ALU_2
    thread_25 = threading.Thread(name='ALU_2', target=alu, args=())

    # ALU_3
    thread_26 = threading.Thread(name='ALU_3', target=alu, args=())

    # ALU_4
    thread_27 = threading.Thread(name='ALU_4', target=alu, args=())

    # ALU_5
    thread_28 = threading.Thread(name='ALU_5', target=alu, args=())

    # ALU_6
    thread_29 = threading.Thread(name='ALU_6', target=alu, args=())

    # ALU_7
    thread_30 = threading.Thread(name='ALU_7', target=alu, args=())

    # ALU_8
    thread_31 = threading.Thread(name='ALU_8', target=alu, args=())

    # ALU_9
    thread_32 = threading.Thread(name='ALU_9', target=alu, args=())

    # VECTOR_PARALLEL
    thread_33 = threading.Thread(name='VECTOR_PARALLEL', target=vector_par, args=())

    #
    # thread_11 = threading.Thread(name='', target=, args=())

    """ Threads Start """
    # thread_1.start()
    # thread_2.start()
    # thread_3.start()
    # thread_4.start()
    # thread_5.start()
    # thread_6.start()
    # thread_7.start()
    # thread_8.start()
    # thread_9.start()
    # thread_10.start()
    # thread_11.start()
    # thread_12.start()
    # thread_13.start()
    # thread_14.start()
    # thread_15.start()
    # thread_16.start()
    # thread_17.start()
    # thread_18.start()
    # thread_19.start()
    # thread_20.start()
    # thread_21.start()
    # thread_22.start()
    # thread_23.start()
    # thread_24.start()
    # thread_25.start()
    # thread_26.start()
    # thread_27.start()
    # thread_28.start()
    # thread_29.start()
    # thread_30.start()
    # thread_31.start()
    # thread_32.start()
