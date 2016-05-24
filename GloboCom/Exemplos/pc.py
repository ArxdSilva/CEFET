class Person(object):

    def __init__(self, age, name, eye_color, hair, gender):
        self.age = age
        self.name = name
        self.eye_color = eye_color
        self.hair = hair
        self.gender = gender

    def printing(self):
        print self.age
        print self.name
        print self.eye_color
        print self.hair
        print self.gender

class Jenny(Person):

    def __init__(self, earings):
        super(Person, self).__init__(age, name, eye_color, hair, gender)
        self.earings = earings


class John(Person):

    def __init__(self, earings):
        super(Person, self).__init__(age, name, eye_color, hair, gender)
        self.earings = earings

genero = ['male', 'female']
# parent = Person()
# son = John()
# daughter = Jenny()

instanciando_Jenny = Jenny(age=22, earings=True, name='Jenny', eye_color='blue', hair='green', gender=genero[1])
instanciando_Jenny.printing()

# super usado para principalmente evitar problemas com heranca multipla
