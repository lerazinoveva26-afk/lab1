def num(inp, flag=False):
    while True:
        try:
            if flag:
                return int(input(inp))
            else:
                return float(input(inp))
        except ValueError:
            print("\nВведите корректное число!")

def menu():
    print("\nВыберите конвертер:")
    print("1. Градус Цельсия <-> Градус Фаренгейта")
    print("2. Километры <-> Мили")
    print("3. Килограммы <-> Фунты")
    print("4. Метры <-> Футы")
    print("0. Выход")

def task1():
    print("\nВыберите направление:")
    print("1. Градус Цельсия -> Градус Фаренгейта")
    print("2. Градус Фаренгейта -> Градус Цельсия")
    n = num("\nВаш выбор: ", flag=True)
    if n == 1:
        C = num("Введите температуру: ")
        print(f"\n{C} C = {(C * 9/5) + 32} F")
    elif n == 2:
        F = num("Введите температуру: ")
        print(f"\n{F} F = {(F - 32) * 5/9} C")
    else:
        print("\nНеверный номер!")

def task2():
    print("\nВыберите направление:")
    print("1. Километры -> Мили")
    print("2. Мили -> Километры")
    n = num("\nВаш выбор: ", flag=True)
    if n == 1:
        km = num("Введите расстояние: ")
        print(f"\n{km} км = {km * 0.621371} миль")
    elif n == 2:
        m = num("Введите расстояние: ")
        print(f"\n{m} миль = {m * 1.609344} км")
    else:
        print("\nНеверный номер!")

def task3():
    print("\nВыберите направление:")
    print("1. Килограммы -> Фунты")
    print("2. Фунты -> Килограммы")
    n = num("\nВаш выбор: ", flag=True)
    if n == 1:
        kg = num("Введите вес: ")
        print(f"\n{kg} кг = {kg * 2.20462} фунта")
    elif n == 2:
        f = num("Введите вес: ")
        print(f"\n{f} фунта = {f * 0.453592} кг")
    else:
        print("\nНеверный номер!")

def task4():
    print("\nВыберите направление:")
    print("1. Метры -> Футы")
    print("2. Футы -> Метры")
    n = num("\nВаш выбор: ", flag=True)
    if n == 1:
        m = num("Введите расстояние: ")
        print(f"\n{m} м = {m * 3.28084} фута")
    elif n == 2:
        f = num("Введите расстояние: ")
        print(f"\n{f} фута = {f * 0.3048} м")
    else:
        print("\nНеверный номер!")

def main():
    while True:
        menu()
        choice = num("\nВаш выбор: ", flag=True)
        if choice == 1:
            task1()
        elif choice == 2:
            task2()
        elif choice == 3:
            task3()
        elif choice == 4:
            task4()
        elif choice == 0:
            break
        else:
            print("\nНеверный номер!")

if __name__ == '__main__':
    main()
