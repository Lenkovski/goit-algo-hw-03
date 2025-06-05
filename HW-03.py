import re

def normalize_phone(phone_number: str) -> str:
    
    # Видаляємо всі символи, крім цифр та плюса
    cleaned = re.sub(r"[^\d+]", "", phone_number)

    # Якщо номер починається з '+'
    if cleaned.startswith('+'):
        if cleaned.startswith('+38'):
            normalized = cleaned
        elif cleaned.startswith('+380'):
            normalized = cleaned
        else:
            normalized = cleaned  # залишаємо як є, якщо інший код
    else:
        if cleaned.startswith('380'):
            normalized = '+' + cleaned
        elif cleaned.startswith('0'):
            normalized = '+38' + cleaned
        else:
            normalized = '+38' + cleaned  # на випадок коротких чи неповних номерів

    return normalized

# Список сирих номерів
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

# Нормалізація кожного номера
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

# Вивід результатів
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)