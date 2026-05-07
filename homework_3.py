from datetime import datetime, date
class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.__occupation = occupation
        self.name = name
        self.__birth_date = birth_date
        self.__higher_education = higher_education
    @property
    def occupation(self):
        return self.__occupation
    @property
    def higher_education(self):
        return self.__higher_education
    @property
    def birth_date(self):
        return self.__birth_date
    @property
    def age(self):
        today = date.today()
        birth = datetime.strptime(self.birth_date, '%d.%m.%Y').date()
        age = today.year - birth.year
        if (today.month,today.day) < (birth.month,birth.day):
            age -= 1
        return age
    def introduce(self):
        if self.higher_education:
            print(f'меня зовут {self.name}, я родился в {self.birth_date}, по профессии '
              f'{self.occupation} высшее образование есть')
        else:
            print(f'меня зовут {self.name}, я родился в {self.birth_date}, по профессии '
                  f'{self.occupation} высшего образования нет')
class Classmate(Person):
    def __init__(self,name, birth_date, occupation, higher_education, group_name,classmate_name):
        super().__init__(name,birth_date,occupation,higher_education)
        self.group_name = group_name
        self.classmate_name = classmate_name
    def introduce(self):
        person_higher_education = "высшее образование есть" if self.higher_education else "высшего образования нет"
        print(f'Привет меня зовут {self.name}, мой одноклассник {self.classmate_name}, мы в группе {self.group_name}, '
              f'я родился в {self.birth_date}, по профессии {self.occupation}, {person_higher_education}')

class Friend(Person):
    def __init__(self,name, birth_date, occupation, higher_education, hobby,friend_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby
        self.friend_name = friend_name
    def introduce(self):
        person_higher_education = "высшее образование есть" if self.higher_education else "высшего образования нет"
        print(f'Привет меня зовут {self.name}, мой друг {self.friend_name}, мое хобби {self.hobby}, '
              f'я родился в {self.birth_date}, по профессии {self.occupation}, {person_higher_education}')
classmate_1 = Classmate("Пётр", '11.11.2000', 'Переводчик', True,'11','Саша' )
classmate_2 = Classmate("Саша", '03.05.2001', 'Учитель', True,'11','Пётр' )

friend_1 = Friend('Андрей', '19.12.2003','Пожарный',True,'Бокс','Фёдор')
friend_2 = Friend('Иван', '01.01.2002','Таксист',False,'нарды','Семён')

person_1 = Person('Azik','13.10.2003', 'backend', False)
person_2 = Person('Karina','24.04.2002', 'teacher', True)
# classmate_1.introduce()
# classmate_2.introduce()
# friend_1.introduce()
# friend_2.introduce()
# person_1.introduce()
# person_2.introduce()
all_people = [person_1, person_2, classmate_1, classmate_2, friend_1, friend_2]
for people in all_people:
    people.introduce()

class BestFriend(Friend):
    def __init__(self, name, birth_date, occupation, higher_education, hobby, friend_name,shared_memory):
        super().__init__(name, birth_date, occupation, higher_education,hobby,friend_name)
        self.shared_memory = shared_memory
    def introduce(self):
        super().introduce()
        print(f'наше общее воспоминание c {self.friend_name}: {self.shared_memory}')

best_friend_1 = BestFriend('Кирилл','23.10.2004','репетитор',False,
                       'английски','Миша','Совместная поездка в Англию')
best_friend_1.introduce()
print(f'возраст {person_1.name}: {person_1.age}')
print(f'возраст {classmate_1.name}: {classmate_1.age}')