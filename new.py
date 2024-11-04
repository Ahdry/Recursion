def get_multiplied_digits(number):
    str_number = str(number)


    # Если длина строки больше 1, продолжаем рекурсию
    if len(str_number) > 1:
        first = int(str_number[0])
        # Если первая цифра не ноль, умножаем ее на результат рекурсивного вызова
        if first != 0:
            return first * get_multiplied_digits(int(str_number[1:]))
        else:
            # Если первая цифра 0, просто пропускаем её
            return get_multiplied_digits(int(str_number[1:]))
    else:
        return int(str_number) if str_number != '0' else 1  # Возвращаем 1, если единственная цифра 0

# Пример использования
result = get_multiplied_digits(40203)
print(result)  # Вывод: 8