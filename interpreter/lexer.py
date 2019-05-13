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
    'OWNEP',
    'SLDVV', 'SLDVS'
    'SRDVV', 'SRDVS'
    'XORDVV', 'XORDVS',
    'OWNDP',
    'COLON', 'SEMI_COLON',
    'OPEN_PAREN', 'CLOSE_PAREN',
    'NUMBER',
    'VEC1', 'VEC2', 'VEC3', 
    'S0', 'S1',  'S2',  'S3',  'S4',  'S5',  'S6',  'S7',  'S8',  'S9',  'S10', 'S11', 'S12', 'S13', 'S14', 'S15',
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
        self.lexer.add('LSI', r'LSI')
        self.lexer.add('LSM', r'LSM')
        self.lexer.add('LVWS', r'LVWS')

        # STORE
        self.lexer.add('SV', r'SV')
        self.lexer.add('SS', r'SS')
        self.lexer.add('SVWS', r'SVWS')

        # CREATE
        # self.lexer.add('CVI', r'CVI')

        # ENCRYPTION
        self.lexer.add('SLEVV', r'SLEVV')
        self.lexer.add('SLEVS', r'SLEVS')

        self.lexer.add('SREVV', r'SREVV')
        self.lexer.add('SREVS', r'SREVS')

        self.lexer.add('XOREVV', r'XOREVV')
        self.lexer.add('XOREVS', r'XOREVS')

        self.lexer.add('OWNEP', r'OWNEP')

        # DESENCRYPTION

        self.lexer.add('SLDVV', r'SLDVV')
        self.lexer.add('SLDVS', r'SLEVS')

        self.lexer.add('SRDVV', r'SRDVV')
        self.lexer.add('SRDVS', r'SRDVS')

        self.lexer.add('XORDVV', r'XORDVV')
        self.lexer.add('XORDVS', r'XORDVS')

        self.lexer.add('OWNDP', r'OWNDP')

        # COLON / SEMI-COLON
        self.lexer.add('COLON', r'\,')
        self.lexer.add('SEMI_COLON', r'\;')

        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')

        # Number
        self.lexer.add('NUMBER', r'\d+')

        # Vector Registers
        self.lexer.add('VEC1', r'v1')
        self.lexer.add('VEC2', r'v2')
        self.lexer.add('VEC3', r'v3')

        # Scalar Registers
        self.lexer.add('S0', r's0')
        self.lexer.add('S1', r's1')
        self.lexer.add('S2', r's2')
        self.lexer.add('S3', r's3')
        self.lexer.add('S4', r's4')
        self.lexer.add('S5', r's5')
        self.lexer.add('S6', r's6')
        self.lexer.add('S7', r's7')
        self.lexer.add('S8', r's8')
        self.lexer.add('S9', r's9')
        self.lexer.add('S10', r's10')
        self.lexer.add('S11', r's11')
        self.lexer.add('S12', r's12')
        self.lexer.add('S13', r's13')
        self.lexer.add('S14', r's14')
        self.lexer.add('S15', r's15')

        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
