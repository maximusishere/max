class Employee:
    vacation_days = 28

    def __init__(
            self, first_name, second_name, gender, remaining_vacation_days = vacation_days
            ):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = remaining_vacation_days  # Сюда добавьте новый атрибут remaining_vacation_days

    
    def consume_vacation(self):
        return Employee.vacation_days - self
      # Сюда добавьте методы consume_vacation и get_vacation_details.
        
    def get_vacation_details(self):
        return f'Остаток отпускных дней: {Employee.consume_vacation()} {self}'
        
# emp = Employee()

# Пример использования класса:
print(Employee('Роберт', 'Крузо', 'м', Employee.vacation_days))
Employee.consume_vacation(7)
print(Employee.get_vacation_details())
