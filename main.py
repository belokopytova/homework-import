from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date

if __name__ == '__main__':
    print(f'Текущяя дата: {date.today()}')
    print(calculate_salary())
    print(get_employees())