rio de janeiro, 21 de marco de 2016
13:00 horas, ServoMecanismos

Forma geral:
    | x1' = f1(x1,...,xn,u)
    | ...
    | Xn' = fn(x1,...,xn,u)
    | y = f0(x1,...,xn,u)

m = grau de diferenciabilidade maximo da variavel x
n = grau de diferenciabilidade maximo da variavel u.

CASO 2:
    Ocorrencia de derivadas de ordem superior da entrada na EDO.

Ex.:
    #| x" + ax' + b.x = u' + du
    #| x(0) = 0
    #| x'(0) = x(0) = 0
Obtenha A, B, C e D.

a) Escolha os estados:
    m - n = n* = grau relativo
    m - n + 1 = 2

    derivar todos uma vez em realacao ao tempo:

    x1 = x
    x2 = x' +du
            |
            \/
        x1' = x' = x2- du
        x2' = x" +du'
              |
              \/
            = u' + du - ax' -bx + du'
            = (1+x).u' +du - ax' -bx
                             |
                             \/
                         (x2 - du)
            = (1+x).u' +du - a.x2 + a.du - b.x1
                |
                \/
             (x = -1)
             x2' = (d - a).u - a.x2 - b.x1

             SOLUCAO:
                         'A'             'B'
             |x1'| = | 0   (1) |.|x1|+|   1   |.(u)
             |x2'| = |(-b) (-a)|.|x2|+|(d - a)|

             y = |(1) (0)|.|x1| + |(0)|.(u)
                    'C'    |x2|    'D'
Ex2.:
        > m = 3  > n = 2
        |       |
    #| x"' =    u" + u' + u
    #| x"(0) = x'(0) = x(0) = 0
    #| u'(0) = u(0) = 0
    #| y = x' + x
        ENCONTRE UMA REPRESENTACAO DE ESTADOS a, b, c e d.
SOLUCAO:
    x1 = x
    x2 = x' + (alpha).u
    x3 = x" + (alpha).u' + (beta).u
    Derivar uma vez em relacao ao tempo (d/dt):

    m - n + 1 = 3 - 2 + 1 = |2|
    (alpha)= A
    (beta) = B

    x1' = x' = x2 - A.u
    x2' = x" + A.u' = x3 - B.u
    x3' = x'" + A.u" + B.u'
    \/
    x3' = A.u" + b.u' + u" + u' + u
    x3' = (1+A).u" + (1+B).u' + u
            |
            \/
        |A = B = (-1)|
    |x3' = u|

    Assim:
    x1' = x2 + u
    x2' = x3 + u
    x3' = u

    | y = x' + u = x2+ u + x1 |

                'A'         'B'
     |x1'| = | 0 1 0 |.|x1|+|1|.(u)
     |x2'| = | 0 0 1 |.|x2|+|1|
     |x3'| = | 0 0 0 |.|x3|+|1|

     y = |(1) (1) (0)|.|x1| + | 1 |.(u)
            'C'        |x2|    'D'
                       |x3|

Ex3.: [FAZER EM CASA]
        > m = 3  > n = 2
        |       |
    #| x' + a.x = u' + b.u
    #| x(0) = 0
    #| u(0) = 0
    #| y = x
        ENCONTRE UMA REPRESENTACAO DE ESTADOS a, b, c e d.

______________________
OBTENCAO DA FUNCAO DE TRANSFERENCIA A PARTIR DE UMA REPRESENTACAO DE ESTADOS:
    | x'= A.x + B.u |
    | y = C.x + D.u | --> | H(s) = [Y(s)/U(s)] |

    Aplicar transformada de Laplace em ambos os lados:
    L{x'} = L{ A.x + B.u}
    L{y}  = L{ C.x + D.u}

                      > =0
    L{x'} = S.X(s) - X(0)
            /\       /\
            vetor  >>|
    s.X(s) = A.X(s) + B.U(s)
    Y(s)   = C.X(s) + D.U(s)

    Colocando em evidencia:
    s.X(s) - A.X(s) = B.U(s)
        Nao pode-se colocar escalar e matrizes juntos, para isso necessita-se multiplicar o escalar pela matriz identidade.
    > X(s).[s.I - A] = B.U(s)

        multiplicar ambos os lados pela matriz inversa do argumento a esquerda.
    > X(s) = {[s.I - A]ˆ(-1)}.B.U(s)

    Y(s) = C.{[s.I - A]ˆ(-1).B + D}.U(S)

    ASSIM:
    [Y(s)/U(s)] = C({[s.I - A]ˆ(-1)}.B) + D

Revisao rapida (multiplicacao matriz-vetor)
    O resultado sempre sera um vetor do mesmo tipo do vetor de entrada.
    > tecnica dos cofatores (estudar)

Exemplo:
    | x' = |  1   3|.x + | 0 |.u
    |      |(-1)  2|     | 1 |
    |
    | y  = | 1  0 |.x

    OBTENHA [Y(s)/U(s)].

SOLUCAO:
    [Y(s)/U(s)] = C({[s.I - A]ˆ(-1)}.B) + D
    [s.I - A] = s.| 1 0 | - |   1  3 |
                  | 0 1 |   | (-1) 2 |

                = | s 0 | - |   1  3 |
                  | 0 s |   | (-1) 2 |

                = | (s-1)   (-3) |
                  |   1    (s-2) |

    [s.I - A]ˆ(-1) = (|(s-2)   3   |) /
                     (|(-1)  (s-1) |) /[(s-1).(s-2) - (-3)]

    [s.I - A]ˆ(-1) = (|(s-2)   3   |) /
                     (|(-1)  (s-1) |) /[(s^2 - 3.s + 5)]

        C({[s.I - A]ˆ(-1)}.B) = | 1  0 |.[(|(s-2)   3   |).| 0 |] /
                                         [(|(-1)  (s-1) |).| 1 |] /[(s^2 - 3.s + 5)]
                              = (| 1  0 |.|  3  |)/
                                (         |(s-1)|)/[(s^2 - 3.s + 5)]
                              = 3/[(s^2 - 3.s + 5)]

            [Y(s)/U(s)] = {3/(s^2 - 3.s + 5)}

Ex5:
                > A           > B
    | x' = |  0   1   |.x + | 0 |.u
    |      |(-6)  (-5)|     | 1 |
    |
    | y  = | 1  1 |.x
              > C , |D = 0|
    [Y(s)/U(s)] = ?

SOLUCAO:

    [Y(s)/U(s)] = C({[s.I - A]ˆ(-1)}.B) + D

    [s.I - A] = | s 0 | - |   0    1 | = | s (-1) |
                | 0 s |   | (-6) (-5)|   | 6 (s+5)|

    [s.I - A]ˆ(-1) = [| (s+5) 1 |]/
                     [| (-6)  s |]/[s^2 - 5.s + 6]

    [Y(s)/U(s)] = (s+1)/[s^2 - 5.s + 6]


Ex6:
    | x' = |  0   1   |.x + | 0 |.u
    |      |(k1)  (k2)|     | 1 |
    |
    | y  = | 1  0 |.x

    determine os valores de k1 e k2 de modo que os polos da Funcao de Transferencia (F.T.) sejam s = (-3) e s= (-5)

SOLUCAO:

    [Y(s)/U(s)] = C({[s.I - A]ˆ(-1)}.B) + D

    [s.I - A] = | s 0 | - |   0    1 | = |   s    (-1) |
                | 0 s |   | (k1) (k2)|   | (-k1) (s-k2)|

    [s.I - A]ˆ(-1) = [| (s-k2) 1 |]/
                     [| (k1)  s  |]/[s(s-k2)-k1]

                   = [| (s-k2) 1 |]/
                     [| (k1)  s  |]/[(sˆ2)-s.k2-k1]

        [Y(s)/U(s)] = | 1  0 |.[| (s-k2) 1 |].| 0 |/
                               [| (k1)  s  |].| 1 |/[(sˆ2)-s.k2-k1]

                    = [| 1  0|.|1|]/
                      [        |s|]/[(sˆ2)-s.k2-k1]

                    = 1/[(sˆ2)-s.k2-k1]

                    (s+3)(s+5) = (sˆ2)+8s+15

                    k1 = (-15)
                    k2 = (-8)

________________________________________________________
Ex7: Considere o sistema

    | x' = | 0  1 |.x + | 0 |.u
    |      | 0  0 |     | k |
    |
    | y  = | 1  0 |.x

    > Existe valor de K pertencente aos numeros R (reais) tal que os polos da Funcao de Transferencia (F.T.) sejam reais? Justifique sua resposta.

    SOLUCAO:

        [Y(s)/U(s)] = C({[s.I - A]ˆ(-1)}.B) + D

        [s.I - A] = | s 0 | - | 0  1 | = |  s (-1) |
                    | 0 s |   | 0  0 |   |  0   s  |

        [s.I - A]ˆ(-1) = [| s  1 |]/
                         [| 0  s |]/[sˆ2 - 1]

        [Y(s)/U(s)] = | 1  0 |.[| s  1 |].| 0 |/
                               [| 0  s |].| k |/[sˆ2 - 0]

                    = | 0  1 |.| 0 |/
                               | k |/[sˆ2]

        [Y(s)/U(s)] = (k/[sˆ2])
                s1 = s2 = 0

        r.: nao existe valor de k.
