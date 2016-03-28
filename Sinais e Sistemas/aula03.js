// Aula 03 do dia 01 de marco de 2016:

Fracoes parciais
Ocorrencia de raizes repetidas:

H(s)= N(s)/[(s-s1)(s+s2)ˆn]
H(s)= A0 + (A1/s-s1) + (A2/[(s-s2)ˆn]) + (A2/[(s-s2)ˆ(n-1)]) + ... + (A2/[(s-s2)ˆ(1)])

A0 = lim(H(s)), s->oo = 0
A1 = H(s).(s-s1)| s=s1,
A2 = H(s).[(s-s2)ˆn]| s = s2,
A_1k = (1/k!).([dˆk]/[dsˆk]).[H(s).(s-s2)ˆn]|s=s2,

Ex:
    H(s)= 2/(sˆ3(s+1)
    Solucao:
      H(s) = A0 + A1/(s+1) + A2/(sˆ3) + A21/(sˆ2) + A22/(s)
            |>0   |>A1=-2    |>A2=2     |>A21=-2    |>A22=2

      A0 = lim(H(s)), s->oo=>                 |A0= 0|

      A1 = H(s).(s+1)|s=-1 => (2/sˆ3)|s=-1 => |A1=-2|

      A2 = H(s).(sˆ3)|s=0  => (2/(s+1))|s=0=> |A2= 2|

      A21= (1/1!).[d/ds].[2/(s+1)]|s=0 => [0.(s+1)-2.1]/([s+1]ˆ2)
      A21= (-2)/([s+1]ˆ2)|s=0 =>              |A21=-2|

      A22= (1/2!).[d/ds].[-2/(s+1)ˆ2]|s=0 => [{0.(s+1)ˆ2} - (-2).(2s+2)]/[(s+1)ˆ4]
      A22= [4(s+1)/(s+1)ˆ4]|s=0               |A22= 2|

//______________________
Ocorrencia de raizes complexas:
H(s) = N(s)/(s+a+b.j).(s+a-b.j) = A1/(s+a+b.j) + A1*/(s+a-b.j)
  Solucao geral:
    h(t) = 2.|A1*|.(eˆ[-a.t]).cos(b.t+angle(A1*))..
                                      |>FASE
//_____________________
Calcular FASE:
  angle = [tgˆ(-1){Im/Re}]
    O angulo teta eh igual a inversa da tangente do numero Real/Imaginario
    >> Esta formula so entrega o angulo do triangulo
    > Colocar os numeros Im e Re sem sinal, depois decidir angulo a partir do
    >  quadrante do numero que se quer.

Ex2:
  G(s) = 2/[(s-2-2j).(s-2+2j)],
  Solucao:
    G(s) = A1*/(s-2-2j) + A1/(s-2+2j)

    A1* = G(s).(s-2-2j)|(s=2+2j) => 2/(s-2+2j) => 2/(2+2j-2+2j),
    |A1* = -(j/2)|

    g(t) = 2(1/2).eˆ(2t).cos(2t+ 3pi/2)
    |g(t) = eˆ(2t).cos(2t+ 3pi/2)|

EXERCICIO 01:
[primeira FIGURA]
a) Calcule a resposta ao impulso.
//  L{T"}   = sˆ2.T(s) - s.T(0) - T'(0)
//  L{T'}   = s.T(s) - T(0)
//  L{Teta} = T(s)
//  L{Vin}  = Vin(s)
    Onde T = Teta

    // L{T"} = L{-3T'+2Vin}
    // sˆ2T(s) = -3.s.T(s)+2.Vin(s)
    T(s) = (2/s.(s+3)).Vin(s)

    Vin(t) = D(t) => Vin(s) = 1
    T(s) = A0 + A1/s + A2/(s+3)
            |>A0=0 |>A1=2/3 |>A2=-(2/3)

    A0 = lim(T(s)), s->oo=>                 |A0= 0|

    T(t) = 2/3.(1-eˆ3t)(...pegar com alguem o final)

  b)
  //  L{T"}   = sˆ2.T(s) - s.T(0) - T'(0)
  //  L{T'}   = s.T(s) - T(0)
  //  L{T"}  = L{-3T'+2Vin}

  sˆ2.T(s) - s.(pi/2) - 0 = -3(s.T(s)-(pi/2)),
  sˆ2.T(s) + 3.s.T(s) = (3.pi/2) + + (4/s) + (pi/2).s,
  T(s)[sˆ2+3.s] = (pi.s)/2 +(4/s) + (3.pi/2),
  T(s)[s(s+3)]  = (pi/2).(s+3) + (4/s),
  T(s) = (pi/2).(1/s) + (4/[(sˆ2).(s+3)]),
                          |>T1(s)
    T1(s)= A1/(s+3) + A2/(sˆ2) + A21/s
            |>A1=4/3  |> A2=4/2  |>A21=-(4/3)
    A1= T1(s).s.(s+3)|s=-3 =>   |A1=(4/9)|
    A2= T1(s).s.(sˆ2)|s=0  =>   |A2=(4/3)|
    A21=(1/1!).(d/ds).(4/(s+3)) => (0-4)/[(s+3)ˆ2],
                                |A21= -(4/3)|

    T(t) = pi/2 + (4/9).eˆ(-3t) - (4/9) + (4/3).t,
    |T(t) = ([pi/2] - (4/9)) +  (4/9).eˆ(-3t) + (4/3).t, t>=0..|

Ex2: ('figura' 02)
//H" = Fin/M - g
M = 10ˆ(-3)kg
g=10m/sˆ2
Fin = 1 N
h(t) = ??
Fin = f(w)
H(0) = 0,05

// L{H"} = L(Fin/M -g)
// sˆ2.H(s)-s.H(0)-H'(0) = Fin/M -g
   sˆ2.H(s)-s.(0,05) = (1/s).[(1/M)-g],
   sˆ2.H(s) = 990/s + 0,05.s,
   H(s) = 990/sˆ3 + 0,05/s,

   |h(t) = 990.tˆ2 + 0,05, t>=0|
