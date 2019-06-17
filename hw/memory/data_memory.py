import time
import os
import numpy
from PIL import Image
from hw.conf.conf import clk as _clk


mem_data = []


def use_data_mem(clk, a, b, rd1, rd2, wd, we, out_a, out_b, out_rd1, out_rd2, out_wd, out_we):
    global mem_data
    while True:
        clock = clk.get()
        dir1 = a.get()
        dir2 = b.get()
        new_data = wd.get()
        w_enable = we.get()

        time.sleep(_clk)

        out_a.put(dir1)
        out_b.put(dir2)
        out_wd.put(new_data)
        out_we.put(w_enable)

        if clock == 1:
            mem_data1 = mem_data[dir1]
            mem_data2 = mem_data[dir2]
            rd1.put(mem_data1)
            rd2.put(mem_data2)
            out_rd1.put(mem_data1)
            out_rd2.put(mem_data2)
        else:
            if w_enable == 1:
                mem_data[dir1] = new_data
                rd1.put(0)
                rd2.put(0)
                out_rd1.put(0)
                out_rd2.put(0)


def load_data_mem(file_path):
    if isinstance(file_path, str):
        if os.path.isfile(file_path):
            global mem_data
            img = Image.open(file_path)
            mem_data = numpy.array(img)
        else:
            print('ERROR: the instruction file doesnt exist, try again')
