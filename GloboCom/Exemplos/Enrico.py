class Veiculo(object):
    pass


class Carro(Veiculo):

    def __init__(self, id):
        self.janelas = 6
        self.rodas = '4'
        self.id = id

    def bater(self):
        self.rodas = 0

    def instalar_radio(self, modelo):
        self.radio = Radio(modelo=modelo)


class Fusca(Carro):

    def __init__(self, id):
        super(Fusca, self).__init__(id)
        self.rodas = 'branca'

id = '12344'

fusca_do_enrico = Fusca(id='12344')


class PC(object):

    def remover_placa(self, placa):
        pos = self.placas.find(placa)
        self.placas.remove(pos)
        self.num_placas = self.num_placas - 1

    def trocar_placa(self, atual, nova):
        self.remover_placa(atual)
        self.instalar_placa(nova)


class Placa(object):

    def __init__(self, tipo, modelo):
        self.tipo = tipo
        self.modelo = modelo


placa_original = Placa('video', 'nvidia')
placa_nova = Placa('video', 'logitech')
meu_pc = PC(placa_video=placa_original)
meu_pc.trocar_placa(placa_original, placa_nova)
