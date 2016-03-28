// Aula 02 do dia 22 de fevereiro de 2016:

Fracoes parciais

Ocorrencia de raizes repetidas:
H(s)= 2/(sˆ2(s+1))
H(s)= A0 + (A1/sˆ2) + (A1_barra/s) + (A2/(s+1))
A0 = lim(H(s)), s->oo = 0

A1 = H(s).sˆ2,
A1 = 2/(s+1)|s=0,
|A1 = 2|..

A1_barra = d(H(s).sˆ2)/ds|s=0,
A1_barra = -2/(s+1)ˆ2|s=0,
|A1_barra = -2|..

A2 = H(s).(s+1)|s=-1,
A2 = 2/(sˆ2)|s=-1,
|A2 = 2|

H(s) = 0 + 2/(sˆ2) - 2/s + 2/(s+1),
H(s) = 2(1/sˆ2) -2(1/s) +2(1/(s+1)),
\/
h(t) = 2.t -2.1(t) + 2.eˆ(-t), t>=0..

//______________________
Ocorrencia de raizes complexas:
G(s) = 1/((s+2+j).(s+2-j)),
G(s) = A1/(s+2+j) + A1*/(s+2-j),
g(t) = 2.|A1*|.eˆ(-2t).cos(t+A1*_angulo_de_fase)..

// Desenhar o plano complexo
A1* = G(s).(s+2-j)|s=-2+j,
A1* = 1/(s+2+j)|s=-2+j,
A1* = 1/(2j) = -j(1/2)
|A1*| = 1/2..

A1*_angulo_de_fase = -pi/2 ou 3pi/2
g(t) = 2.|1/2|.eˆ(-2t).cos(t-(pi/2)),
g(t) = eˆ(-2t).cos(t-(pi/2))..

//______________________
Resposta ao Impulso:
> Cada sistema tem sua resposta em Impulso.
> Mais facil observar no dominio da frequencia, comparado com o dominio do
> tempo.

>Geralmente tem-se:
  u = variavel de entrada
  y = variavel de saida
  R_ez = Resposta em estado zero

d(V0)/dt = -2.V0 + 2.Vin,

>Aplicar equacao de Laplace
S0{d(V0)/dt} = -2.L{V0} + 2.L{Vin},
S.V0(s) - V0(0) = -2.V0(s) + 2.Vin(s),
//         |=> V0(0) = zero
(s+2).V0(s) = 2.Vin(s),
V0(s) = (2/(s+2)).Vin(s).. // resposta em relacao de entrada-saida
V0(s) = (2/(s+2)).1,
V0(s) = (2/(s+2))..

V0(t) = h(t) = 2.eˆ(-2t)..
(V0(s))/(Vin(s)) = (2/(s+2)),
//Funcao de Transferencia = L{h}
