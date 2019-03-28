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

        # test if > operator
        tmp = self.run_code('x = 1; if x > 0 then a = True end')
        self.assertTrue(tmp['a'])

        # test if < operator
        tmp = self.run_code('x = 1; if x < 2 then a = True end')
        self.assertTrue(tmp['a'])

        # test if != operator
        tmp = self.run_code('x = 1; if x != 2 then a = True end')
        self.assertTrue(tmp['a'])

        # test if >= operator
        tmp = self.run_code('x = 1; if x >= 1 then a = True end')
        self.assertTrue(tmp['a'])

        # test while loop
        tmp = self.run_code('x = 1; while x < 3 do x = x + 1 end')
        self.assertEqual(tmp['x'], 3)

    def run_code(self, code):
        tokens = lex(code)
        result = parse(tokens)

        self.assertIsNotNone(result, 'Parser failed parsing: ' + code)

        ast = result.value
        env = {}
        ast.eval(env)
        return env
