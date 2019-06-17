import time
from hw.conf.conf import clk


def control_unit(op, funct, rd, out_op, out_funct, out_rd,
                 reg_write_d, out_reg_write_d,
                 mem_to_reg, out_mem_to_reg,
                 mem_write_d, out_mem_write_d,
                 alu_control_d, out_alu_control_d,
                 alu_src, out_alu_src,
                 imm_src, out_imm_src,
                 reg_src_d, out_reg_src_d):
    while True:
        data_op = op.get()   # GET INPUT FROM QUEUE
        data_funct = funct.get()   # GET INPUT FROM QUEUE
        data_rd = rd.get()   # GET INPUT FROM QUEUE

        time.sleep(clk)  # SLEEP FOR SYNC PROCESS

        out_op.put(data_op)
        out_funct.put(data_funct)
        out_rd.put(data_rd)

        if data_op == '1000000' and data_funct == '000':
            # 1 - ADDVV

            reg_write_d.put()
            mem_to_reg.put()
            mem_write_d.put()
            alu_control_d.put()
            alu_src.put()
            imm_src.put()
            reg_src_d.put()

            out_reg_write_d.put()
            out_mem_to_reg.put()
            out_mem_write_d.put()
            out_alu_control_d.put()
            out_alu_src.put()
            out_imm_src.put()
            out_reg_src_d.put()

        elif data_op == '1000001' and data_funct == '000':
            # 2 - SUBVV

            reg_write_d.put()
            mem_to_reg.put()
            mem_write_d.put()
            alu_control_d.put()
            alu_src.put()
            imm_src.put()
            reg_src_d.put()

            out_reg_write_d.put()
            out_mem_to_reg.put()
            out_mem_write_d.put()
            out_alu_control_d.put()
            out_alu_src.put()
            out_imm_src.put()
            out_reg_src_d.put()

        elif data_op == '1000010' and data_funct == '000':
            # 3 - MULVV

            reg_write_d.put()
            mem_to_reg.put()
            mem_write_d.put()
            alu_control_d.put()
            alu_src.put()
            imm_src.put()
            reg_src_d.put()

            out_reg_write_d.put()
            out_mem_to_reg.put()
            out_mem_write_d.put()
            out_alu_control_d.put()
            out_alu_src.put()
            out_imm_src.put()
            out_reg_src_d.put()

        elif data_op == '1000011' and data_funct == '000':
            # 4 - DIVVV

            reg_write_d.put()
            mem_to_reg.put()
            mem_write_d.put()
            alu_control_d.put()
            alu_src.put()
            imm_src.put()
            reg_src_d.put()

            out_reg_write_d.put()
            out_mem_to_reg.put()
            out_mem_write_d.put()
            out_alu_control_d.put()
            out_alu_src.put()
            out_imm_src.put()
            out_reg_src_d.put()

        elif data_op == '0000000' and data_funct == '001':
            # 5 - SLEVV

            reg_write_d.put()
            mem_to_reg.put()
            mem_write_d.put()
            alu_control_d.put()
            alu_src.put()
            imm_src.put()
            reg_src_d.put()

            out_reg_write_d.put()
            out_mem_to_reg.put()
            out_mem_write_d.put()
            out_alu_control_d.put()
            out_alu_src.put()
            out_imm_src.put()
            out_reg_src_d.put()

        elif data_op == '0000010' and data_funct == '001':
            # 6 - SREVV

            reg_write_d.put()
            mem_to_reg.put()
            mem_write_d.put()
            alu_control_d.put()
            alu_src.put()
            imm_src.put()
            reg_src_d.put()

            out_reg_write_d.put()
            out_mem_to_reg.put()
            out_mem_write_d.put()
            out_alu_control_d.put()
            out_alu_src.put()
            out_imm_src.put()
            out_reg_src_d.put()

        elif data_op == '0000100' and data_funct == '001':
            # 7 - XOREVV

            reg_write_d.put()
            mem_to_reg.put()
            mem_write_d.put()
            alu_control_d.put()
            alu_src.put()
            imm_src.put()
            reg_src_d.put()

            out_reg_write_d.put()
            out_mem_to_reg.put()
            out_mem_write_d.put()
            out_alu_control_d.put()
            out_alu_src.put()
            out_imm_src.put()
            out_reg_src_d.put()

        elif data_op == '0000110' and data_funct == '001':
            # 8 - OWNEP

            reg_write_d.put()
            mem_to_reg.put()
            mem_write_d.put()
            alu_control_d.put()
            alu_src.put()
            imm_src.put()
            reg_src_d.put()

            out_reg_write_d.put()
            out_mem_to_reg.put()
            out_mem_write_d.put()
            out_alu_control_d.put()
            out_alu_src.put()
            out_imm_src.put()
            out_reg_src_d.put()

        elif data_op == '0000000' and data_funct == '010':
            # 9 - SLDVV

            reg_write_d.put()
            mem_to_reg.put()
            mem_write_d.put()
            alu_control_d.put()
            alu_src.put()
            imm_src.put()
            reg_src_d.put()

            out_reg_write_d.put()
            out_mem_to_reg.put()
            out_mem_write_d.put()
            out_alu_control_d.put()
            out_alu_src.put()
            out_imm_src.put()
            out_reg_src_d.put()

        elif data_op == '0000010' and data_funct == '010':
            # 10 -SRDVV

            reg_write_d.put()
            mem_to_reg.put()
            mem_write_d.put()
            alu_control_d.put()
            alu_src.put()
            imm_src.put()
            reg_src_d.put()

            out_reg_write_d.put()
            out_mem_to_reg.put()
            out_mem_write_d.put()
            out_alu_control_d.put()
            out_alu_src.put()
            out_imm_src.put()
            out_reg_src_d.put()

        elif data_op == '0000100' and data_funct == '010':
            # 11 - XORDVV

            reg_write_d.put()
            mem_to_reg.put()
            mem_write_d.put()
            alu_control_d.put()
            alu_src.put()
            imm_src.put()
            reg_src_d.put()

            out_reg_write_d.put()
            out_mem_to_reg.put()
            out_mem_write_d.put()
            out_alu_control_d.put()
            out_alu_src.put()
            out_imm_src.put()
            out_reg_src_d.put()

        elif data_op == '0000110' and data_funct == '010':
            # 12 - OWNDP

            reg_write_d.put()
            mem_to_reg.put()
            mem_write_d.put()
            alu_control_d.put()
            alu_src.put()
            imm_src.put()
            reg_src_d.put()

            out_reg_write_d.put()
            out_mem_to_reg.put()
            out_mem_write_d.put()
            out_alu_control_d.put()
            out_alu_src.put()
            out_imm_src.put()
            out_reg_src_d.put()

        elif data_op == '1000100' and data_funct == '000':
            # 13 - ADDVS

            reg_write_d.put()
            mem_to_reg.put()
            mem_write_d.put()
            alu_control_d.put()
            alu_src.put()
            imm_src.put()
            reg_src_d.put()

            out_reg_write_d.put()
            out_mem_to_reg.put()
            out_mem_write_d.put()
            out_alu_control_d.put()
            out_alu_src.put()
            out_imm_src.put()
            out_reg_src_d.put()

        elif data_op == '1000101' and data_funct == '000':
            # 14 - SUBVS

            reg_write_d.put()
            mem_to_reg.put()
            mem_write_d.put()
            alu_control_d.put()
            alu_src.put()
            imm_src.put()
            reg_src_d.put()

            out_reg_write_d.put()
            out_mem_to_reg.put()
            out_mem_write_d.put()
            out_alu_control_d.put()
            out_alu_src.put()
            out_imm_src.put()
            out_reg_src_d.put()

        elif data_op == '1000110' and data_funct == '000':
            # 15 - SUBSV

            reg_write_d.put()
            mem_to_reg.put()
            mem_write_d.put()
            alu_control_d.put()
            alu_src.put()
            imm_src.put()
            reg_src_d.put()

            out_reg_write_d.put()
            out_mem_to_reg.put()
            out_mem_write_d.put()
            out_alu_control_d.put()
            out_alu_src.put()
            out_imm_src.put()
            out_reg_src_d.put()

        elif data_op == '1000111' and data_funct == '000':
            # 16 - MULVS

            reg_write_d.put()
            mem_to_reg.put()
            mem_write_d.put()
            alu_control_d.put()
            alu_src.put()
            imm_src.put()
            reg_src_d.put()

            out_reg_write_d.put()
            out_mem_to_reg.put()
            out_mem_write_d.put()
            out_alu_control_d.put()
            out_alu_src.put()
            out_imm_src.put()
            out_reg_src_d.put()

        elif data_op == '1001000' and data_funct == '000':
            # 17 - DIVVS

            reg_write_d.put()
            mem_to_reg.put()
            mem_write_d.put()
            alu_control_d.put()
            alu_src.put()
            imm_src.put()
            reg_src_d.put()

            out_reg_write_d.put()
            out_mem_to_reg.put()
            out_mem_write_d.put()
            out_alu_control_d.put()
            out_alu_src.put()
            out_imm_src.put()
            out_reg_src_d.put()

        elif data_op == '1001001' and data_funct == '000':
            # 18 - DIVSV

            reg_write_d.put()
            mem_to_reg.put()
            mem_write_d.put()
            alu_control_d.put()
            alu_src.put()
            imm_src.put()
            reg_src_d.put()

            out_reg_write_d.put()
            out_mem_to_reg.put()
            out_mem_write_d.put()
            out_alu_control_d.put()
            out_alu_src.put()
            out_imm_src.put()
            out_reg_src_d.put()

        elif data_op == '1001010' and data_funct == '000':
            # 19 - LV

            reg_write_d.put()
            mem_to_reg.put()
            mem_write_d.put()
            alu_control_d.put()
            alu_src.put()
            imm_src.put()
            reg_src_d.put()

            out_reg_write_d.put()
            out_mem_to_reg.put()
            out_mem_write_d.put()
            out_alu_control_d.put()
            out_alu_src.put()
            out_imm_src.put()
            out_reg_src_d.put()

        elif data_op == '1001011' and data_funct == '000':
            # 20 - LSI

            reg_write_d.put()
            mem_to_reg.put()
            mem_write_d.put()
            alu_control_d.put()
            alu_src.put()
            imm_src.put()
            reg_src_d.put()

            out_reg_write_d.put()
            out_mem_to_reg.put()
            out_mem_write_d.put()
            out_alu_control_d.put()
            out_alu_src.put()
            out_imm_src.put()
            out_reg_src_d.put()

        elif data_op == '1001100' and data_funct == '000':
            # 21 - LSM

            reg_write_d.put()
            mem_to_reg.put()
            mem_write_d.put()
            alu_control_d.put()
            alu_src.put()
            imm_src.put()
            reg_src_d.put()

            out_reg_write_d.put()
            out_mem_to_reg.put()
            out_mem_write_d.put()
            out_alu_control_d.put()
            out_alu_src.put()
            out_imm_src.put()
            out_reg_src_d.put()

        elif data_op == '1001101' and data_funct == '000':
            # 22 - LVWS

            reg_write_d.put()
            mem_to_reg.put()
            mem_write_d.put()
            alu_control_d.put()
            alu_src.put()
            imm_src.put()
            reg_src_d.put()

            out_reg_write_d.put()
            out_mem_to_reg.put()
            out_mem_write_d.put()
            out_alu_control_d.put()
            out_alu_src.put()
            out_imm_src.put()
            out_reg_src_d.put()

        elif data_op == '0000001' and data_funct == '001':
            # 23 - SLEVS

            reg_write_d.put()
            mem_to_reg.put()
            mem_write_d.put()
            alu_control_d.put()
            alu_src.put()
            imm_src.put()
            reg_src_d.put()

            out_reg_write_d.put()
            out_mem_to_reg.put()
            out_mem_write_d.put()
            out_alu_control_d.put()
            out_alu_src.put()
            out_imm_src.put()
            out_reg_src_d.put()

        elif data_op == '0000011' and data_funct == '001':
            # 24 - SREVS

            reg_write_d.put()
            mem_to_reg.put()
            mem_write_d.put()
            alu_control_d.put()
            alu_src.put()
            imm_src.put()
            reg_src_d.put()

            out_reg_write_d.put()
            out_mem_to_reg.put()
            out_mem_write_d.put()
            out_alu_control_d.put()
            out_alu_src.put()
            out_imm_src.put()
            out_reg_src_d.put()

        elif data_op == '0000101' and data_funct == '001':
            # 25 - XOREVS

            reg_write_d.put()
            mem_to_reg.put()
            mem_write_d.put()
            alu_control_d.put()
            alu_src.put()
            imm_src.put()
            reg_src_d.put()

            out_reg_write_d.put()
            out_mem_to_reg.put()
            out_mem_write_d.put()
            out_alu_control_d.put()
            out_alu_src.put()
            out_imm_src.put()
            out_reg_src_d.put()

        elif data_op == '0000001' and data_funct == '010':
            # 26 - SLDVS

            reg_write_d.put()
            mem_to_reg.put()
            mem_write_d.put()
            alu_control_d.put()
            alu_src.put()
            imm_src.put()
            reg_src_d.put()

            out_reg_write_d.put()
            out_mem_to_reg.put()
            out_mem_write_d.put()
            out_alu_control_d.put()
            out_alu_src.put()
            out_imm_src.put()
            out_reg_src_d.put()

        elif data_op == '0000011' and data_funct == '010':
            # 27 - SRDVS

            reg_write_d.put()
            mem_to_reg.put()
            mem_write_d.put()
            alu_control_d.put()
            alu_src.put()
            imm_src.put()
            reg_src_d.put()

            out_reg_write_d.put()
            out_mem_to_reg.put()
            out_mem_write_d.put()
            out_alu_control_d.put()
            out_alu_src.put()
            out_imm_src.put()
            out_reg_src_d.put()

        elif data_op == '0000101' and data_funct == '010':
            # 28 - XORDVS

            reg_write_d.put()
            mem_to_reg.put()
            mem_write_d.put()
            alu_control_d.put()
            alu_src.put()
            imm_src.put()
            reg_src_d.put()

            out_reg_write_d.put()
            out_mem_to_reg.put()
            out_mem_write_d.put()
            out_alu_control_d.put()
            out_alu_src.put()
            out_imm_src.put()
            out_reg_src_d.put()

        elif data_op == '1001110' and data_funct == '000':
            # 29 - SV

            reg_write_d.put()
            mem_to_reg.put()
            mem_write_d.put()
            alu_control_d.put()
            alu_src.put()
            imm_src.put()
            reg_src_d.put()

            out_reg_write_d.put()
            out_mem_to_reg.put()
            out_mem_write_d.put()
            out_alu_control_d.put()
            out_alu_src.put()
            out_imm_src.put()
            out_reg_src_d.put()

        elif data_op == '1001111' and data_funct == '000':
            # 30 - SVWS

            reg_write_d.put()
            mem_to_reg.put()
            mem_write_d.put()
            alu_control_d.put()
            alu_src.put()
            imm_src.put()
            reg_src_d.put()

            out_reg_write_d.put()
            out_mem_to_reg.put()
            out_mem_write_d.put()
            out_alu_control_d.put()
            out_alu_src.put()
            out_imm_src.put()
            out_reg_src_d.put()

        elif data_op == '1010000' and data_funct == '000':
            # 31 - SS

            reg_write_d.put()
            mem_to_reg.put()
            mem_write_d.put()
            alu_control_d.put()
            alu_src.put()
            imm_src.put()
            reg_src_d.put()

            out_reg_write_d.put()
            out_mem_to_reg.put()
            out_mem_write_d.put()
            out_alu_control_d.put()
            out_alu_src.put()
            out_imm_src.put()
            out_reg_src_d.put()

        else:
            # NOTHING

            reg_write_d.put()
            mem_to_reg.put()
            mem_write_d.put()
            alu_control_d.put()
            alu_src.put()
            imm_src.put()
            reg_src_d.put()

            out_reg_write_d.put()
            out_mem_to_reg.put()
            out_mem_write_d.put()
            out_alu_control_d.put()
            out_alu_src.put()
            out_imm_src.put()
            out_reg_src_d.put()
