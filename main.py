import sys
from cayley import CayleyTable
from properties import (
    is_associative, is_commutative, find_neutral,
    is_left_solvable, is_right_solvable, is_invertible
)
from classifier import classify
from utils import parse_int_list

def main():
    print("Анализатор конечных группоидов")
    print("Введите мощность множества (1-10):")
    try:
        n = int(input().strip())
        if not (1 <= n <= 10):
            raise ValueError("Мощность должна быть от 1 до 10.")
    except ValueError as e:
        print(f"Ошибка: {e}")
        sys.exit(1)

    print(f"Введите таблицу Кэли: {n} строк по {n} целых чисел (0-{n-1}), разделенных пробелами.")
    table_data = []
    for i in range(n):
        row_input = input().strip()
        row = parse_int_list(row_input)
        if len(row) != n:
            print(f"Ошибка: Строка {i+1} должна содержать ровно {n} элементов.")
            sys.exit(1)
        table_data.append(row)

    try:
        table = CayleyTable(n, table_data)
    except ValueError as e:
        print(f"Ошибка: {e}")
        sys.exit(1)

    # Check properties
    closed = table.is_closed()
    associative = is_associative(table)
    commutative = is_commutative(table)
    neutral = find_neutral(table)
    left_solvable = is_left_solvable(table)
    right_solvable = is_right_solvable(table)
    solvable = left_solvable and right_solvable
    invertible = is_invertible(table, neutral) if neutral is not None else False

    # Output properties
    print("\nСвойства операции:")
    print(f"Замкнутая: {'Да' if closed else 'Нет'}")
    print(f"Ассоциативная: {'Да' if associative else 'Нет'}")
    print(f"Коммутативная: {'Да' if commutative else 'Нет'}")
    print(f"Имеет нейтральный элемент: {'Да, равен ' + str(neutral) if neutral is not None else 'Нет'}")
    print(f"Разрешимая: {'Да' if solvable else 'Нет'}")
    print(f"Обратимая: {'Да' if invertible else 'Нет'}")

    # Classifications
    classifications = classify(table)
    print("\nКлассификация:")
    if classifications:
        for cls in classifications:
            print(f"- {cls}")
    else:
        print("Не соответствует ни одной стандартной классификации.")

if __name__ == "__main__":
    main()