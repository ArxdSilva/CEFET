A = 2


def soma_e_multiplica(a, b):
    A = a + b
    B = multiplica(a, b) + a + b
    return A + B


def multiplica(a, b):
    B = (a * b) * A
    return B


####################################################################

# Constante, global
GRAVIDADE = 9.6

# variavel, global
_plugins = []


def calcula(x):
    # x eh local nesta funcao, foi passado como parametro
    # y tambem eh local
    y = x * 2
    return y * GRAVIDADE


def concatena(x):
    # x eh local nesta funcao, foi passado como parametro
    # y tambem eh local
    y = x + x
    return y


def registra(plugin):
    global _plugins
    _plugins.append(plugin)

calcula(1)
concatena("abc")  # "abcabc"


class Somador(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calcula():
        c = self.a + self.b
        return c


s = Somador(1, 2)
n = s.calcula()  # 3


i = 0
achei = False
while i < 1000:
    i += 1
    if (i % 2) == 0:
        continue
    # ...


for i in range(1000):
    if (i % 2) == 0:
        achei = True
        break
