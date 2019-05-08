from lexer import Lexer
from parser import Parser
from code_generator import CodeGen

import datetime


class Compiler:

    def __init__(self):
        self.text_input = None
        self.lexer = None
        self.parser = None
        self.tokens = None
        self.codegen = None

    def compile(self, file_name):

        with open(file_name) as f:
            self.text_input = f.read()

        self.lexer = Lexer().get_lexer()
        self.tokens = self.lexer.lex(self.text_input)

        self.codegen = CodeGen()

        module = self.codegen.module
        builder = self.codegen.builder
        printf = self.codegen.printf

        pg = Parser(module, builder, printf)
        pg.parse()
        parser = pg.get_parser()
        parser.parse(self.tokens).eval()

        self.codegen.create_ir()
        self.codegen.save_ir(datetime.datetime.now() + '')




