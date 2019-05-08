from rply import LexerGenerator

"""
    Tokens
    
    [
    'ADDVV', 'ADDVS', 
    'SUBVV', 'SUBVS','SUBSV', 
    'MULVV', 'MULVS',
    'DIVVV', 'DIVVS', 'DIVSV',
    'LV', 'LVWS', 
    'SV', 'SVWS',
    'CVI',
    'SLEVV', 'SLEVS',
    'SREVV', 'SREVS',
    'XOREVV', 'XOREVS',
    'COLON', 'SEMI_COLON',
    'NUMBER'
    ]
    
"""


class Lexer:

    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):

        # ADD
        self.lexer.add('ADDVV', r'ADDVV')
        self.lexer.add('ADDVS', r'ADDVS')

        # SUB
        self.lexer.add('SUBVV', r'SUBVV')
        self.lexer.add('SUBVS', r'SUBVS')
        self.lexer.add('SUBSV', r'SUBSV')

        # MUL
        self.lexer.add('MULVV', r'MULVV')
        self.lexer.add('MULVS', r'MULVS')

        # DIV
        self.lexer.add('DIVVV', r'DIVVV')
        self.lexer.add('DIVVS', r'DIVVS')
        self.lexer.add('DIVSV', r'DIVSV')

        # LOAD
        self.lexer.add('LV', r'LV')
        self.lexer.add('LVWS', r'LVWS')

        # STORE
        self.lexer.add('SV', r'SV')
        self.lexer.add('SVWS', r'SVWS')

        # CREATE
        self.lexer.add('CVI', r'CVI')

        # ENCRYPTION
        self.lexer.add('SLEVV', r'SLEVV')
        self.lexer.add('SLEVS', r'SLEVS')

        self.lexer.add('SREVV', r'SREVV')
        self.lexer.add('SREVS', r'SREVS')

        self.lexer.add('XOREVV', r'XOREVV')
        self.lexer.add('XOREVS', r'XOREVS')

        # COLON / SEMI-COLON
        self.lexer.add('COLON', r'\,')
        self.lexer.add('SEMI_COLON', r'\;')

        # Number
        self.lexer.add('NUMBER', r'\d+')

        # Vector Registers
        # self.lexer.add('', r'')

        # Scalar Registers
        # self.lexer.add('', r'')

        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()