import unittest
from . import formatter


class Token:

    def __init__(self, kind, text=None, value=None):
        self.kind = kind
        self.text = text
        self.value = value
        self.nextToken = None  # 按照是源文件的顺序，不受lexer中filter的影响

    def __str__(self):
        # return 'kind = %s, text = %s, value = %s' % (self.kind, self.text, self.value)
        if self.value:
            return '%s(%s)' % (self.kind, self.value)
        else:
            return str(self.kind)

    def toLiteral(self):
        if self.kind == "ID":
            return '-%s-' % self.value

    def toCode(self):
        return formatter.token2Code(self)


class Test(unittest.TestCase):

    def test(self):
        from .lex_tokens import TokenType
        print(Token(TokenType.ID, 'Shader', 'Shader'))
