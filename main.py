# Вложенные циклы

# №1 Найти сумму всех четырехзначных натуральных чисел, сумма цифр которых равна 20.
def count_FD_numbers():
    count = 0
    for a in range(1000, 10000):
        if sum(list(map(int, str(a)))) == 20:
            count += a
    print(count)


# №2 Лесенка чисел
def stair(i):
    st = ""
    for a in range(1, i+1):
        print(st + " " + str(a))
        st = st + " " + str(a)
# stair(5)


# №3 Звёздочки
def stars():
    numbers = input().split()
    for a in numbers:
        print(int(a)*"*")
# stars()


# №4 Постулат Бертрана для простых чисел
def bertran():
    i = int(input())
    count = 0
    for a in range(i + 1, i * 2):
        c = True
        for b in range(2, a // 2 + 1):
            if a % b == 0:
                c = False
                break
        if c:
            count += 1
    print(count)
# bertran()

# №5 Пузырьковая сортировка с количеством действий
def bubble_sort():
    i = int(input())
    numbers = list(map(int, list(input().split())))
    count = 0
    for a in range(i - 1):
        for b in range(i - a - 1):
            if numbers[b] > numbers[b + 1]:
                numbers[b], numbers[b + 1] = numbers[b + 1], numbers[b]
                count += 1
    print(" ".join(map(str, numbers)))
    print(count)
# bubble_sort()


# №6 Нахождение целых пар чисел формул
def eq_system():
    numbers = list(map(int, list(input().split())))
    count = 0
    for a in range(numbers[0]):
        for b in range(numbers[1]):
            if numbers[1] - b**2 == a and numbers[0] - a**2 == b:
                count += 1
    print(count)
# eq_system()


# №5 Сортировка вставками
def insertion_sort():
    i = int(input())
    numbers = list(map(int, list(input().split())))
    for a in range(i - 1):
        for b in range(a + 1, 0, -1):
            if numbers[b] < numbers[b - 1]:
                numbers[b], numbers[b - 1] = numbers[b - 1], numbers[b]
    print(" ".join(map(str, numbers)))
# insertion_sort()