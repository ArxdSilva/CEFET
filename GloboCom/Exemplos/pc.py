class Person(object):

    properties_to_print = ['name', 'age']

    def __init__(self, age, name, eye_color, hair, gender):
        self.age = age
        self.name = name
        self.eye_color = eye_color
        self.hair = hair
        self.gender = gender

    def printing(self):
        text = ''
        for prop in self.properties_to_print:
            text += prop + ' is ' + getattr(self, prop)
        print text


class X(Person):

    properties_to_print = ['name', 'age', 'earings']

    def __init__(self, age, name, eye_color, hair, gender, earings):
        self.earings = earings
        super(X, self).__init__(age, name, eye_color, hair, gender)

    def printer(self):
        self.printing()


class Y(Person):

    def __init__(self, age, name, eye_color, hair, gender, earings):
        super(Y, self).__init__(age, name, eye_color, hair, gender)
        self.earings = earings

    def printer(self):
        self.printing()

genero = ['male', 'female']
# instancia = situacao particular de uma classe onde seus atributos tomam
# certas caracteristicas unicas da instancia.
instancia_de_X = X(age=22, name='X', eye_color='blue',
                   hair='green', gender=genero[1], earings=True)

instanciando_X.printer()

instancia_de_Y = Y(42, 'Y', 'brown', 'red', genero[0], False)

instanciando_Y.printer()


inst_person = Person(age=22, name='X', ...)
# X seria instancia de Person
# instancia => parte do codigo onde eh definido um tipo de uma classe que
# tem certas caracteristicas definidas pela classe.
