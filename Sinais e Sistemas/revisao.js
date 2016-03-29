// Aula REVISAO do dia 01 de marco de 2016:


1) Considere o sistema dinamico:

|x" + 12x' + 35x = r(t)    "(desconsidere este e as proximas)
|x'(0) = (-1)              '
|x(0) = 1
|r(t) = 1(t) -> Degrau unitario.

A) CALCULE A RESPOSTA AO [ESTADO ZERO] (REZ).
B) CALCULE A RESPOSTA A [ENTRADA NULA] (REN).

SOLUCAO:

"   L{x"} = sˆ(2).x(s) - x(s).5 - x'(0)       '
'   L{x'} = s.x(s) - x(s)
    L{1(t)} = (1/s)

Colocando na equacao fornecida
    sˆ(2).x(s) - x(s).5 - x'(0) + 12.s.x(s) -12.x(0) + 35x(s) = (1/s)       '
      x(s).[sˆ(2) + 12s + 35] = (1/s) + x(0).s + 12.x(0) + x'(0)            '

      x(s) = 1/(s.[sˆ(2) + 12s + 35]) +  [x(0).s + 12.x(0) + x'(0)]/[sˆ(2) + 12s + 35]            '

a) X(s) = 1/[s.(s+5).(s+7)] = A0 + A1/s + A2/(s+5) + A3/(s+7)

  A0 = lim X(s) = 0
      s->oo
  A1 = X(s).s| = 1/[(s+5).(s+7)]| = [1/35]
            s=0                s=0
  A2 = X(s).(s+5)| = 1/[s.(s+7)]| = (-[1/10])
                s=-5            s=(-5)
  A3 = X(s).(s+7)| = 1/[s.(s+5)] = [1/14]
                s=(-7)            s=(-7)

Entao:
      | x(t) = 1/35 - (1/10).eˆ(-5.t)+ (1/14).eˆ(-7.t), t>= 0 |
    Excitacao

b) X(s) = [s-1+12]/[(s+5).(s+7)]
        = [s+11]/[(s+5).(s+7)]
        = B0 + B1/(s+5) + B2/(s+7)..

    B0 = lim X(s) = 0
        s->oo

    B1 = X(s).(s+5)| = [s+11]/(s+7)| = (3)..
                  s=-5          s=(-5)
    B2 = X(s).(s+7)| = [s+11]/(s+5)| = (-2)..
                  s=-7          s=(-7)
    Entao:
      | X(t) = 3.eˆ(-5.t) - 2.eˆ(-7.t) , t>= 0 |
  Condicoes Iniciais

____________________________________________________________
2) SABEND OQUE A RESPOSTA AO DEGRAU UNITARIO DA FUNCAO H(s) abaixo(1), determine a resposta ao impulso no tempo da funcao [Y(s)/R(s)]

  (1)   y(t) = eˆ(-5.t) , t >= 0
                     _________
    R(s) => (+) ---> |  H(s) | -> Y(s)
                 |(-) -------- |
                 |<-----------<|

SOLUCAO:
E(s): entrada de H(s)
E(s) = 1/s -> Y(s) = 1/(s+5)

H(s) = Y(s)/E(s) = (1/(s+5))/(1/s) = | (s/(s+5)) |

[Y(s)/R(s)] = (s/(s+5))/[1+(s/(s+5))] = | s/(2.s+5) |

H(s) = L {resposta ao IMPULSO}
Lˆ(-1){H(s)} = resposta ao IMPULSO

Y(s) = (1/2).(s/s+2,5) = A0 + A1/(s+2,5)

  A0 = lim Y(s) = (1/2)
        s->oo

  A1 = Y(s).(s+2,5)| = (1/2).s = (-5/4)
                s=(-2,5)

    Y(s) = 1/s - (5/4).(1/[s+2,5])
      Y(t) = (1/2).d(t) - (5/4).eˆ(-2,5.t) , t>= 0ˆ(-)


____________________________________________________________
3)

--->| H1 |--->(+)---> | H2 |--->|--|--->Y(s)
              /\                |  |
              (+)<--- | H3 |<---|  |
              /\                   |
              /\ <--- | H4 |<--- ---
                  (-)

Y(s)/R(s) = ?
SOLUCAO:
blocos paralelos vao virar um bloco so chamado => | H3 - H4 |
H3 - H4 = H2/(1-H2[H3-H4])

  | Y(s)/R(s) = [H1.H2]/[1-H2.H3 + H2.H4] |

____________________________________________________________
4) determine os valores de a, b , g para que [Y(s)/R(s)] tenha polos em (s = (-2)), (s = (-3)) e um zero em (s = (-1))

                               |--->--->--->--->--->--->-|
                               |                         \/
  --->(+)--->(+)---> | (1/s) |-*->| (1/s) |-*->| g |--->(+)--->Y(s)
       |      |                |            |
       |      /\<---| a |<---<---<---<---<--|
       |                       |
       /\<---<--<---| b |<---<-|

OBS: b nao conecta com a linha q vai ao bloco 'a' na linha 112.

SOLUCAO:
                                              (s+g)
                                               /\
                     C                    ______|_______
                     /\                   |---| s |--->|
            _________|________            |           \/
--->(+)--->(+)---> | (1/s) |-*->| (1/s) |-*->| g |--->(+)--->Y(s)
     |      |                |            |
     /\<---<--<---| a |<---<---<---<---<--|
            |                |
            /\<---| b |<---<-|

C = (1/(s-b))

(1/s) / [1-(b/s)] = 1/(s-b)

--->(+)---> | (1/s.(s-b)) |-*->| (s+g) |--->Y(s)
    |                       |
    /\--<---<---| a |<---<--|

[(1/s.(s-b))]/(1-(a/s(s-b))) = 1/(sˆ(2) - b.s - a)

[Y(s)/R(s)] = (s+g)/(sˆ(2) - b.s - a)
            = (s+2).(s+3)
            = sˆ(2) - 5.s - 6)
            b = (-5)
            a = (-6)
