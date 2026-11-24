from fractions import Fraction
from decimal import Decimal, getcontext
import matplotlib.pyplot as plt
import time

# ------------------ ПЕРВОЕ ЗАДАНИЕ ------------------

def epsilon():
    e = 1.0
    while 1.0 + e / 2 > 1.0:
        e = e / 2
    return e


def task1():
    start = time.perf_counter()

    result = get_x(30)

    end = time.perf_counter()

    print("Результат:", result)
    print("Время выполнения:", end - start, "секунд")


# ------------------ ВТОРОЕ ЗАДАНИЕ ------------------

def muller(y, z):
    return 108 - (815 - 1500 / z) / y


def get_x(n):
    if n == 0:
        return 4.0
    if n == 1:
        return 4.25

    x0 = 4.0
    x1 = 4.25

    for i in range(2, n + 1):
        x2 = muller(x1, x0)
        x0, x1 = x1, x2

    return x1


def task2():
    start = time.perf_counter()
    n = int(input("Введите n: "))
    print("x =", get_x(n))
    end = time.perf_counter()
    print("Время выполнения:", end - start, "секунд")


# ------------------ ТРЕТЬЕ ЗАДАНИЕ ------------------

def Ipoteka(S, x, i):
    S = Decimal(S)
    x = Decimal(x)
    i = int(i)

    r = x / Decimal(1200)

    if r == 0:
        return S / i

    t = 1 + r
    return S * (t**i * (t - 1)) / (t**i - 1)


def task3():
    getcontext().prec = 30

    print("\nЗадание 3. Ипотека")

    S = Decimal(input("Сумма кредита: "))
    x = Decimal(input("Годовая ставка (%): "))
    y = int(input("Срок кредита (лет): "))

    if S <= 0 or x < 0 or y <= 0:
        print("Некорректные параметры кредита")
        return

    n = 12 * y
    stavka = x / Decimal(1200)

    # Пункт а
    start = time.perf_counter()
    A = Ipoteka(S, x, n)
    A = A.quantize(Decimal("0.01"))
    print("\nПункт а) Платёж:", A, "рублей")

    # Пункты б, в
    ostatok = S
    months = []
    ost_table = []
    proc_table = []
    total = Decimal(0)

    print("\nПункт в) Таблица платежей")
    print(f"{'Месяц':<10}{'Остаток':<18}"
          f"{'Платёж':<15}{'Проценты':<15}"
          f"{'Осн. долг':<15}")

    for i in range(1, n + 1):
        procent = (ostatok * stavka).quantize(Decimal("0.01"))

        if i == n or A >= ostatok + procent:
            platezh = ostatok + procent
        else:
            platezh = A

        if platezh <= procent and ostatok > 0:
            print("Платёж недостаточен для погашения процентов")
            return

        dolg = platezh - procent
        ostatok = ostatok - dolg
        total += platezh

        print(f"{i:<10}{ostatok:<18.2f}"
              f"{platezh:<15.2f}{procent:<15.2f}"
              f"{dolg:<15.2f}")

        months.append(i)
        ost_table.append(float(ostatok))
        proc_table.append(float(procent))

        if ostatok == 0:
            break

    # Пункт б
    pereplata = total - S
    print("\nПункт б) Переплата:", pereplata, "рублей")

    # Пункт г
    plt.figure(figsize=(10, 5))
    plt.plot([0] + months, [float(S)] + ost_table, color="blue")
    plt.title("Остаток долга по ипотеке")
    plt.xlabel("Месяц")
    plt.ylabel("Остаток долга, руб.")
    plt.grid(True)
    plt.show()

    # Пункт д
    plt.figure(figsize=(10, 5))
    plt.plot(months, proc_table, color="red")
    plt.title("Проценты по ипотеке")
    plt.xlabel("Месяц")
    plt.ylabel("Проценты, руб.")
    plt.grid(True)
    plt.show()
    
    end = time.perf_counter()
    print("Время выполнения:", end - start, "секунд")
# ------------------ ЧЕТВЁРТОЕ ЗАДАНИЕ ------------------

# Пункт а) Decimal

def muller_41(y, z):
    return Decimal(108) - (
        Decimal(815) - Decimal(1500) / z
    ) / y


def get_x_41(n):
    x0 = Decimal(4)
    x1 = Decimal("4.25")

    if n == 0:
        return x0
    if n == 1:
        return x1

    for i in range(2, n + 1):
        x2 = muller_41(x1, x0)
        x0, x1 = x1, x2

    return x1


# Пункт б) Fraction

def muller_42(y, z):
    return Fraction(108) - (
        Fraction(815) - Fraction(1500) / z
    ) / y


def get_x_42(n):
    x0 = Fraction(4, 1)
    x1 = Fraction(17, 4)

    if n == 0:
        return x0
    if n == 1:
        return x1

    for i in range(2, n + 1):
        x2 = muller_42(x1, x0)
        x0, x1 = x1, x2

    return x1


def task4():
    start = time.perf_counter()
    print("\nЗадание 4. Decimal и Fraction")
    n = int(input("Введите n: "))

    getcontext().prec = 100

    print("\nПункт а) Decimal:")
    print(get_x_41(n))

    print("\nПункт б) Fraction:")
    result = get_x_42(n)
    print(result)
    print("Десятичное представление:", float(result))

    end = time.perf_counter()
    print("Время выполнения:", end - start, "секунд")

# ------------------ ГЛАВНОЕ МЕНЮ ------------------

def main():
    while True:
        print("\n==============================")
        print("АРИФМЕТИКА С ПЛАВАЮЩЕЙ ЗАПЯТОЙ")
        print("==============================")
        print("1. Машинный эпсилон")
        print("2. Последовательность Мюллера")
        print("3. Ипотечный калькулятор")
        print("4. Decimal и Fraction")
        print("0. Выход")

        choice = input("\nВыберите задание: ")

        if choice == "1":
            task1()
        elif choice == "2":
            task2()
        elif choice == "3":
            task3()
        elif choice == "4":
            task4()
        elif choice == "0":
            print("Завершение программы")
            break
        else:
            print("Неверный номер задания")


if __name__ == "__main__":
    main()
