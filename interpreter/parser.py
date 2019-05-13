from rply import ParserGenerator
from ast import Sub


class Parser:

    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            [
                'ADDVV', 'ADDVS',
                'SUBVV', 'SUBVS', 'SUBSV',
                'MULVV', 'MULVS',
                'DIVVV', 'DIVVS', 'DIVSV',
                'LV', 'LVWS',
                'SV', 'SVWS',
                'CVI',
                'SLEVV', 'SLEVS',
                'SREVV', 'SREVS',
                'XOREVV', 'XOREVS',
                'OWNEP',
                'SLDVV', 'SLDVS',
                'SRDVV', 'SRDVS',
                'XORDVV', 'XORDVS',
                'OWNDP',
                'COLON', 'SEMI_COLON',
                'OPEN_PAREN', 'CLOSE_PAREN',
                'NUMBER',
                'VEC1', 'VEC2', 'VEC3',
                'S0', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15',
            ]
        )

    def parse(self):

        @self.pg.production('expression : ADDVV VEC1 COLON VEC2 COLON VEC3 SEMI_COLON')
        @self.pg.production('expression : ADDVV VEC1 COLON VEC3 COLON VEC2 SEMI_COLON')
        @self.pg.production('expression : ADDVV VEC2 COLON VEC1 COLON VEC3 SEMI_COLON')
        @self.pg.production('expression : ADDVV VEC2 COLON VEC3 COLON VEC1 SEMI_COLON')
        @self.pg.production('expression : ADDVV VEC3 COLON VEC1 COLON VEC2 SEMI_COLON')
        @self.pg.production('expression : ADDVV VEC3 COLON VEC2 COLON VEC1 SEMI_COLON')
        def expression(p):
            print("ADDVV 1")
            return 0

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()

