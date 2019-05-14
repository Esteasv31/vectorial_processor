class mem_exe_reg:

    def __init__(self):
        """ Inputs """
        self.in_vec_reg_1 = None
        self.in_vec_reg_2 = None

        """ Outputs """
        self.out_vec_reg_1 = None
        self.out_vec_reg_2 = None

    """ Inputs """

    """ Vec Reg 1 """

    def get_in_vec_reg_1(self):
        return self.in_vec_reg_1

    def set_in_vec_reg_1(self, value):
        self.in_vec_reg_1 = value

    def del_in_vec_reg_1(self):
        del self.in_vec_reg_1

    in_vec_reg_1 = property(get_in_vec_reg_1, set_in_vec_reg_1, del_in_vec_reg_1, 'In Vec Reg 1')

    """ Vec Reg 2 """

    def get_in_vec_reg_2(self):
        return self.in_vec_reg_2

    def set_in_vec_reg_2(self, value):
        self.in_vec_reg_2 = value

    def del_in_vec_reg_2(self):
        del self.in_vec_reg_2

    in_vec_reg_2 = property(get_in_vec_reg_2, set_in_vec_reg_2, del_in_vec_reg_2, 'In Vec Reg 2')

    """ Outputs """