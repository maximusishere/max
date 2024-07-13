class Contact:

    def __init__(self, name, year_birth, is_programmer):
        self.name = name        
        self.year_birth = year_birth        
        self.is_programmer = is_programmer

    def age_define(self):
        if 1946 < self.year_birth < 1980:
            return 'Олдскул'
        if self.year_birth >= 1980:
            return 'Молодой'
        return 'Старейшина'

    def programmer_define(self):
        if self.is_programmer:
            return 'Программист'
        return 'нормальный'

    def show_contact(self):
        return (f'{self.name}, '               
                f'категория: {self.age_define()}, '
                f'статус: {self.programmer_define()}')
    
bill_gates = Contact(name='Билл Гейтс', year_birth=1955, is_programmer=True)

# Создаём экземпляр класса Contact
mike = Contact(name='Михаил Булгаков', year_birth=1891, is_programmer=False)

# Заготавливаем строку, которую по ожиданию должен вернуть метод show_contact():
expected_string = 'Михаил Булгаков, категaория: Старейшина, статус: нормальный'

# print(mike.show_contact())
# print(bill_gates.show_contact())
# Пишем утверждение: 
# "вызов метода show_contact объекта mike вернёт строку, сохранённую в expected_string"
assert mike.show_contact() == expected_string, 'Метод show_contact работает некорректно!'   


print(bill_gates.show_contact())
# Билл Гейтс, категория: Олдскул, статус: Программист