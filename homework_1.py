class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.occupation = occupation
        self.name = name
        self.birth_date = birth_date
        self.ocupation = occupation
        self.higher_education = higher_education
    def introduce(self, born_place):
        if self.higher_education:
            print(f'меня зовут {self.name}, я родился в городе {born_place}, по профессии '
              f'{self.occupation} высшее образование есть')
        else:
            print(f'меня зовут {self.name}, я родился в городе {born_place}, по профессии '
                  f'{self.occupation} высшего образования нет')

person_1 = Person('Azik','13.10.2003', 'backend', False)
person_2 = Person('Karina','24.04.2002', 'teacher', True)
person_1.introduce('Bishkek')
person_2.introduce('Dubai')