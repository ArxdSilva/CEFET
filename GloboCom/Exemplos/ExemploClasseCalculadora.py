class Computador(object):

    def __init__(self, id_unico, fabricante, sistema_op):
        self.id_unico = id_unico
        self.fabricante = fabricante
        self.sistema_op = sistema_op  # pode ser uma classe de sistemas

    def print_specs(self):
        print ('Your PC was made by ' + self.fabricante +
               ', Its ID is: ' + str(self.id_unico) + ' and your SO is: ' + self.sistema_op)
computadorApple = Computador(
    id_unico=123456, fabricante='Apple', sistema_op='OS X')
print_pcApple = computadorApple.print_specs()


class OperatingSistems(object):

    def __init__(self, name, version):
        self.name = name
        self.version = version

    def run_sistem(self):
        if (self.name == 'Windows'):
            print('BSOD')
        else:
            print('Starting system')
            print(self.name + ' ' + self.version)

    def print_name_version(self):
        print ('Your SO is ' + self.name + ', version number: ' + str(self.version))


linux_sis = OperatingSistems(name='Debian', version=1.0)
print_debian = linux_sis.print_name_version()

windows_sis = OperatingSistems(name='Windows', version=10)
print_win = windows_sis.print_name_version()
