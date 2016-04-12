// Aula 03 do dia 01 de marco de 2016:

  Sistemas de tempo discreto:
    1- Grafico da foto.
x(t) -> chave (on/off) -> x(k.t) -> | Quantizador | -> x_a(t)
        (oscilador)
        (_-_-_-_-_)   [h = 1/(f)]

          f = frequencia de oscilacao
          h: periodo de amostragem.

      * Sinais discretos: -> SEQUENCIAS

        Ex.:
        [forma geral]
          x(n) = { 0 ; -1 ; 2 ; 1 ; -1 ; ... }
                      ____
                        n = 0, coloca-se sempre uma barra abaixo onde tem-se a amostra de indice zero(pro Grafico).

          y(n) = (2)ˆ(n); n>=0
               = { 1 ; 2 ; 4 ; 8 ; ... }

          EXEMPLO 2:
          [forma recursiva]
            W(n+1) = 2.w(n) - 3.w(n-1); n>=0
            Onde: w(0) = 1, w(1) = 1

            Equacao de diferencas = ?
________________________________________________________________________

r(n)->| H |->y(n)
       |>condicoes iniciais

       y_T(n) = y_REZ(n) + y_REN(n)
       H: A0.y(n) + A1.y(n-1) + A2.y(n-2) + ... + An.y(n-k) =
         = B0.x(n) + B1.x(n-1) + B2.x(n-2) + ... + Bn.x(n-p)

    Principais Sequencias:
          [GRAFICOS NAS FOTOS 2-3]
        1) Impulso discreto:
            d(t) =  | 1, n =  0
                    | 0, n != 0

        2) Degrau Unitario discreto:
            1(n) =  | 0, n <  0
                    | 1, n >= 0

        3) Exponencial discreta:
            (a)ˆn = | 0, n < 0
                    | (a)ˆ(n), n >= 0
                OBS: a=1 => degrau unitario.

        [resto da aula nas fotos 4 - ...]
        {acabou a bateria x.x }
