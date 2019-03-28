from django.test import TestCase
from PiGPIO.interpreter import *


class InterpreterTestCase(TestCase):

    def test_interpreter(self):
        # test assignments
        tmp = self.run_code('x = 1')
        self.assertEqual(tmp['x'], 1)

        # test basic arithmetic expressions
        tmp = self.run_code('x = 1 + 2 * 3')
        self.assertEqual(tmp['x'], 7)

        # test arithmetic expressions and if statements
        tmp = self.run_code('x = 1 + 2 * 3; if x == 8 then a = True; b = False else a = False; b = True end')
        self.assertFalse(tmp['a'])
        self.assertTrue(tmp['b'])

        # test boolean expressions with boolean vars
        tmp = self.run_code('x = True; if x == True then a = True else a = False end')
        self.assertTrue(tmp['a'])

        # test execution order in boolean expressions and if statements with only one branch
        tmp = self.run_code('x = 1; if (x + 3) == (1 + (6 /2)) then a = True; b = False end')
        self.assertTrue(tmp['a'])
        self.assertFalse(tmp['b'])

    def run_code(self, code):
        tokens = lex(code)
        result = parse(tokens)

        self.assertIsNotNone(result, 'Parser failed parsing: ' + code)

        ast = result.value
        env = {}
        ast.eval(env)
        return env
