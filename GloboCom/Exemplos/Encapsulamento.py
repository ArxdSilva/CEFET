class A:
    a = 1  # atributo publico
    __b = 2  # atributo privado a class A


class B(A):
    __c = 3  # atributo privado a B

    def __init__(self):
        print self.a
        print self.__c

a = A()
print a.a  # imprime 1

b = B()
print b.__b  # Erro, pois __b é privado a classe A.
print b.__c  # Erro, __c é um atributo privado, somente chamado pela classe.

# Executa a classe B, (inicia variaveis privadas/protegidas) (...)? e inicia a variavel privada a classe B __c.
print b._B__c  # Imprime __c = 3, muito pouco utilizada, masq existe.
