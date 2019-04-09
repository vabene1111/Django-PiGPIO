import sys
import re

# Tokens
RESERVED = 'RESERVED'
INT = 'INT'
BOOLEAN = 'BOOLEAN'
ID = 'ID'

# Matching of expressions to tokens
token_exprs = [
    (r'[ \n\t]+', None),
    (r'#[^\n]*', None),
    (r'==', RESERVED),
    (r'\=', RESERVED),
    (r'\(', RESERVED),
    (r'\)', RESERVED),
    (r';', RESERVED),
    (r'\+', RESERVED),
    (r'-', RESERVED),
    (r'\*', RESERVED),
    (r'/', RESERVED),
    (r'<=', RESERVED),
    (r'<', RESERVED),
    (r'>=', RESERVED),
    (r'>', RESERVED),
    (r'!=', RESERVED),
    (r'and\b', RESERVED),
    (r'or\b', RESERVED),
    (r'not\b', RESERVED),
    (r'if\b', RESERVED),
    (r'then\b', RESERVED),
    (r'else\b', RESERVED),
    (r'while\b', RESERVED),
    (r'do\b', RESERVED),
    (r'end\b', RESERVED),
    (r'True', BOOLEAN),
    (r'False', BOOLEAN),
    (r'[0-9]+', INT),
    (r'[A-Za-z][A-Za-z0-9_]*', ID),
]


def lex(characters):
    """
    Generic lexer function to interpret code associated with steps
    :param characters: raw input
    :return: list of tokens found by lexer
    """
    pos = 0
    tokens = []
    while pos < len(characters):
        match = None
        for token_expr in token_exprs:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(characters, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            sys.stderr.write('Illegal character: %s\\n' % characters[pos])
            sys.exit(1)
        else:
            pos = match.end(0)
    return tokens
