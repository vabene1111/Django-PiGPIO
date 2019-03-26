class Equality:
    def __eq__(self, other):
        return isinstance(other, self.__class__) and \
               self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)


class Aexp(Equality):
    pass


class IntAexp(Aexp):
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return 'IntAexp(%d)' % self.i


class VarAexp(Aexp):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'VarAexp(%s)' % self.name


class BinopAexp(Aexp):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def __repr__(self):
        return 'BinopAexp(%s, %s, %s)' % (self.op, self.left, self.right)


class Bexp(Equality):
    pass


class RelopBexp(Bexp):
    def __init__(self, op, left, right):
        ...


class AndBexp(Bexp):
    def __init__(self, left, right):
        ...


class OrBexp(Bexp):
    def __init__(self, left, right):
        ...


class NotBexp(Bexp):
    def __init__(self, exp):
        ...


class Statement(Equality):
    pass


class AssignStatement(Statement):
    def __init__(self, name, aexp):
        ...


class CompoundStatement(Statement):
    def __init__(self, first, second):
        ...


class IfStatement(Statement):
    def __init__(self, condition, true_stmt, false_stmt):
        ...


class WhileStatement(Statement):
    def __init__(self, condition, body):
        ...
