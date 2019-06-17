import time
import os
from hw.conf.conf import clk


instruction_list = []


def use_instruc_mem(a, rd, out_a, out_rd):
    while True:
        instruc = a.get()

        time.sleep(clk)

        mem_data = instruction_list.pop(instruc)

        rd.put(mem_data)
        out_rd.put(mem_data)
        out_a.put(instruc)


def load_instruc_mem(file_path):
    if isinstance(file_path, str) and file_path.endswith('rv32'):
        if os.path.isfile(file_path):
            file = open(file_path, 'r')
            for line in file.readlines():
                instruction_list.append(line.replace('\n', ''))
        else:
            print('ERROR: the instruction file doesnt exist, try again')
