'''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый,
с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их ти
к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''


class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'Отлично'
                else:
                    return f'С годом что-то не то!'
            else:
                return f'С месяцем что-то не то!'
        else:
            return f'Что за день такой??'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('19 - 02 - 1933')
print(today)
print(Data.valid(4, 13, 1022))
print(today.valid(6, 1, 2001))
print(Data.extract('111 - 6 - 2611'))
print(today.extract('19 - 119 - 300020'))
print(Data.valid(99, 11, 2000))
