from lexer import Lexer
from parser import Parser


text_input = """
ADDVV v1, v2, v3;
ADDVV v1, v3, v2;
ADDVV v2, v3, v1;
ADDVV v2, v1, v3;
ADDVV v3, v1, v2;
ADDVV v3, v2, v1;
 
ADDVS ,
SUBVV , 
SUBVS , 
SUBSV ,
MULVV , 
MULVS ,
DIVVV , 
DIVVS , 
DIVSV ,
LV , 
LVWS ,
SV , 
SVWS ,
SLEVV , 
SLEVS ,
SREVV , 
SREVS ,
XOREVV , 
XOREVS ,
OWNEP ,
SLDVV ,
SLDVS ,
SRDVV , 
SRDVS ,
XORDVV , 
ORDVS ,
OWNDP ,
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()