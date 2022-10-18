import datetime

from application.salary import calculate_salary
from application.db.people import get_employees

def main():
    print(datetime.date.today())
    print(calculate_salary(60000, 50000))
    print(get_employees())


if __name__ == '__main__':
    main()



