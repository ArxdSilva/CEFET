// Aula 03 do dia 29 de fevereiro de 2016:

Funcao de Transferencia:

> A funcao de Transferencia de um sistema dinamico, linear, causal e invariante
no tempo eh uma representacao no dominio da frequencia que descreve 'APENAS' o
comportamento 'Saida/Entrada'.

Ex.:
    #| y" + a.y' + b.y = &.u
    #| y'(0) = A
    #| y(0)  = B

Funcao de Transferencia:
    Y(s)/U(s) = ??
    Solucao:
    # (sˆ2).y(s)-s.y(0) - y'(0) + a(s.y(s)-y(0)) + b.y(s)= &.U(s)
    #              |>ZERO |>ZERO           |>ZERO
    # y(s).[(sˆ2) + a.s + b.s] = &.U(s)..
    Y(s)/U(s) = (&)/((sˆ2) + a.s + b.s)..
    Respostada da relacao entrada/saida

> Classificacao:
        H(s) = (N(s))/(D(s))
Onde:
    N(s) = polinomio do numerador
    grau[N(s)] = n

    D(s) = polinomio do denominador
    grau[D(s)] = m

(1) FT propria:
    grau[N(s)] = grau[D(s)]

(2) FT estritamente propria:
    grau[N(s)] < grau[D(s)]

(3) FT Impropria:
    grau[N(s)] > grau[D(s)]
    OBS: ESTE CASO NAO OCORRE EM AMBIENTES 'REAIS'
#__________________________________
Grau relativo de uma FT (n*):
    (n*) = grau[D(s)] - grau[N(s)]

Ganho DC ou de frequencia 'ZERO':
    Ganho_DC H(s) = H(s=0)

Ex:
    (1) H(s) = (2)/(s+1) + (-1)/[(s+2).(s+1)]
    (2) G(s) = ((sˆ2)+2.s+3)/((sˆ2)+s+5)

Calcule:
    a) O grau relativo de H(s) e de G(s).
    b) Gaho DC de H(s) e G(s).

'Solucao':
    # MMC
    H(s) = [(2)/(s+1)]'/(s+2)' + {(-1)/[(s+2).(s+1)]}'/1'
    H(s) = [(2.(s+2)-1)/(s+1).(s+2) = (2.s + 3)/((sˆ2) + 3.s + 5)

    a)  n*_h = 1;
        n*_g = 0 ..

    b)  H(0) = 3/2;
        G(0) = 3/5 ..

Descricao de sistemas no espaco de Estados:
    Estado (variavel de estado):
        Eh qualquer informacao em 't >= 0' que, juntamente com a entrada e com
        as condicoes iniciais, torna possivel a descricao completa do
        comportamento do sistema para 't >= 0'.

    Representacao de Estados:
        |EDO     | >>> | EDOs   |
        |de ordem|     |de ordem|

    Forma Geral:
        # x'_1 = f1(x1;x2;...;xn;u)
        # x'_2 = f2(x1;x2;...;xn;u)
        # (...)
        # x'_n = fn(x1;x2;...;xn;u)
        # y    = fs(x1;x2;...;xn;u)

Ex:
    # Z"' + a.Z" + b.Z' + c.Z = &.u
    # Z"(0) = a
    # Z'(0) = b
    # Z (0) = c
>> Forma 'companheira / canonica' controlavel
    # y = k1.z' + k2.z

'Solucao':
    # Z1 = z  d/dt  |Z'1 = Z2
    # Z2 = z'------>|Z'2 = z" = Z3
    # Z3 = z"       |Z'3 = z"'
     'foi feita a derivacao dos elementos'

    y = k1.z2 + k2.z1 ..

    # Z'3 = z"' = &.u - a.z" - b.z' - c.z
    # Z'3 = &.u - a.Z3 - b.Z2 - c.Z1 ...

        |Z1|
    Z = |Z2|
        |Z3|

        # |Z'1|   |0     1    0  | |Z1|   |0|
        # |Z'2| = |0     0    1  |.|Z2| + |0|.u
        # |Z'3|   |(-c) (-b) (-a)| |Z3|   |&|
        #           ------------           -
        #             Matriz A             Matriz B

        # y = [k2 k1 0].|Z1| + [0].u
        #      ------   |Z2|   ---
        #         |     |Z3|    |
        #      Matriz C         Matriz D

(1) A: Matriz de transicao de Estados
(2) B: Matriz de entrada/controle
(3) C: Matriz de saida
(4) D: Matriz de transmissao direta
