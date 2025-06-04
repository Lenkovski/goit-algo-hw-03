from datetime import datetime

def get_days_from_today(date_str: str) -> int:

    try:
        input_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        current_date = datetime.today().date()
        delta = current_date - input_date
        return delta.days
    except ValueError:
        raise ValueError("Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'.")

# Приклад роботи
if __name__ == "__main__":
    user_date = input("Введіть дату у форматі РРРР-ММ-ДД: ")
    try:
        days_diff = get_days_from_today(user_date)
        if days_diff > 0:
            print(f"Від заданої дати до сьогодні минуло {days_diff} днів.")
        elif days_diff < 0:
            print(f"Задана дата на {-days_diff} днів пізніша за сьогодні.")
        else:
            print("Задана дата співпадає з сьогоднішньою.")
    except ValueError as e:
        print(e)