import random

def get_numbers_ticket(min_num, max_num, quantity):

    if not (isinstance(min_num, int) and isinstance(max_num, int) and isinstance(quantity, int)):
        return []
    if min_num < 1 or max_num > 1000 or min_num > max_num:
        return []
    if quantity < 1 or quantity > (max_num - min_num + 1):
        return []
    
    numbers = random.sample(range(min_num, max_num + 1), quantity)
    numbers.sort()
    return numbers

if __name__ == "__main__":
    min_val = 1
    max_val = 49
    quantity_val = 6
    
    lottery_numbers = get_numbers_ticket(min_val, max_val, quantity_val)
    if lottery_numbers:
        print("Ваші лотерейні числа:", lottery_numbers)
    else:
        print("Некоректні вхідні параметри.")