""" Control Signals

    signals = {
        "0000": add,
        "0001": sub,
        "0010": mul,
        "0011": div,
        "0100": shiftl,
        "0101": shiftr,
        "0110": xor,
        "0111": pow_,
        "1000": sqrt,
        "1001": cshiftl,
        "1010": cshiftr
    }
"""
import time
from hw.conf.conf import clk


def alu(control, in_x, in_y, out_res, out_x, out_y, out_control, out_z):
    while True:

        con = control.get()  # GET THE CONTROL SIGNAL
        a = in_x.get()       # GET INPUT FROM QUEUE
        b = in_y.get()       # GET INPUT FROM QUEUE

        time.sleep(clk)      # SLEEP FOR SYNC PROCESS

        out_x.put(a)         # WRITE VALUE TO CONTROL SIGNALS
        out_y.put(b)         # WRITE VALUE TO CONTROL SIGNALS
        out_control.put(con)

        if con == "0000":
            c = add(a, b)   # ADD
            out_res.put(c)  # WRITE THE OUTPUT VALUE
            out_z.put(c)
        elif con == "0001":
            c = sub(a, b)   # SUB
            out_res.put(c)  # WRITE THE OUTPUT VALUE
            out_z.put(c)
        elif con == "0010":
            c = mul(a, b)   # MULT
            out_res.put(c)  # WRITE THE OUTPUT VALUE
            out_z.put(c)
        elif con == "0011":
            c = div(a, b)   # DIV
            out_res.put(c)  # WRITE THE OUTPUT VALUE
            out_z.put(c)
        elif con == "0100":
            c = shiftl(a, b)  # SHIFT LEFT
            out_res.put(c)  # WRITE THE OUTPUT VALUE
            out_z.put(c)
        elif con == "0101":
            c = shiftr(a, b)  # SHIFT RIGHT
            out_res.put(c)  # WRITE THE OUTPUT VALUE
            out_z.put(c)
        elif con == "0110":
            c = xor(a, b)   # XOR
            out_res.put(c)  # WRITE THE OUTPUT VALUE
            out_z.put(c)
        elif con == "0111":
            c = pow_(a, b)  # POW
            out_res.put(c)  # WRITE THE OUTPUT VALUE
            out_z.put(c)
        elif con == "1000":
            c = sqrt(a, b)  # SQRT
            out_res.put(c)  # WRITE THE OUTPUT VALUE
            out_z.put(c)
        elif con == "1001":
            c = cshiftl(a, b)  # CIRCULAR SHIFT LEFT
            out_res.put(c)  # WRITE THE OUTPUT VALUE
            out_z.put(c)
        elif con == "1010":
            c = cshiftr(a, b)  # CIRCULAR SHIFT RIGHT
            out_res.put(c)  # WRITE THE OUTPUT VALUE
            out_z.put(c)
        else:
            c = "XXXXXXXX"  # DEFAULT VALUE FOR WRONG CONTROL SIGNAL
            out_res.put(c)  # WRITE THE OUTPUT VALUE
            out_z.put(c)


""" ADD """


def add(a, b):
    return a + b


""" SUB """


def sub(a, b):
    return a - b


""" MUL """


def mul(a, b):
    return a * b


""" DIV """


def div(a, b):
    return a / b


""" SHIFT L """


def shiftl(a, b):
    return a << b


""" SHIFT R """


def shiftr(a, b):
    return a >> b


""" XOR """


def xor(a, b):
    return a ^ b


""" POW """


def pow_(a, b):
    return a ** b


""" SQRT """


def sqrt(a, b):
    return int(a ** (1 / b))


""" C SHIFT L """


def cshiftl(a, b):
    binary = "{0:b}".format(a)
    return binary[b:len(binary)] + binary[0:b]


""" C SHIFT R """


def cshiftr(a, b):
    binary = "{0:b}".format(a)
    return binary[-b:len(binary)] + binary[0:-b]
