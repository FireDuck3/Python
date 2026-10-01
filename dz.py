# 1
a = 17
b = 5
print("Сума:", a + b)
print("Різниця:", a - b)
print("Добуток:", a * b)
print("Частка:", a / b)

# 2
print("Цілочисельне ділення (//):", a // b)
print("Залишок від ділення (%):", a % b)
# // виконує ділення націло (відкидає залишок, округлюючи вниз), а / дає звичайний результат з дробом.

# 3
print("2 у 10-му степені:", 2 ** 10)
print("10 у 3-му степені:", 10 ** 3)

# 4
price = 249.99
count = 3
print("Загальна вартість:", price * count)

# 5
print("Тип 7 / 2:", type(7 / 2))
print("Тип 7 // 2:", type(7 // 2))
print("Тип 7.0 // 2:", type(7.0 // 2))
# / завжди дає float. // зберігає int, якщо обидва операнди цілі, або дає float, якщо хоча б один float.

# 6
name = "Python"
print(name * 3)

# 7
str1 = "Привіт, "
str2 = "світ!"
result_str = str1 + str2
print(result_str)

# 8
students = 28
per_row = 6
print("Повних рядів:", students // per_row, "| Залишилось учнів:", students % per_row)

# 9
total_seconds = 3725
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print(hours, "годин,", minutes, "хвилин,", seconds, "секунд")

# 10
total_minutes = 150
print(total_minutes // 60, "годин,", total_minutes % 60, "хвилин")

# 11
c = 36.6
f = c * 9 / 5 + 32
print("Температура у Фаренгейтах:", f)

# 12
width = 12.5
height = 8
print("Площа:", width * height, "| Периметр:", 2 * (width + height))

# 13
r = 7
pi = 3.14159
print("Площа кола:", pi * (r ** 2), "| Довжина кола:", 2 * pi * r)

# 14
initial_price = 1200
discount = initial_price * 0.15
print("Знижка:", discount, "грн | Фінальна ціна:", initial_price - discount, "грн")

# 15
salary = 25000
tax = salary * 0.195
print("Зарплата на руки:", salary - tax, "грн")

# 16
speed = 90
time = 2.5
print("Пройдена відстань:", speed * time, "км")

# 17
print("Середнє арифметичне:", (10 + 11 + 8) / 3)

# 18
n = 7
print("Залишок від ділення на 2:", n % 2)

# 19
n = 473
print("Остання цифра:", n % 10)

# 20
n = 473
print("Сотні:", n // 100, "| Десятки:", (n // 10) % 10, "| Одиниці:", n % 10)

# 21
n = 859
print("Сума цифр:", (n // 100) + ((n // 10) % 10) + (n % 10))

# 22
original = 123
reversed_num = (original % 10) * 100 + ((original // 10) % 10) * 10 + (original // 100)
print("Перевернуте число:", reversed_num)

# 23
print("Квадратний корінь з 144:", 144 ** 0.5)

# 24
print("Кількість секунд у році:", 365 * 24 * 60 * 60)

# 25
x = "5"
y = "3"
print("Рядки:", x + y)
print("Числа:", int(x) + int(y))
# Рядки склеїлися, а числа додалися математично.

# 26
print("9.99 в int:", int(9.99))
# Дробова частина відкинулася.

# 27
print(True + True + True, type(True + True + True))
print(True * 10, type(True * 10))
# Тип int, оскільки bool є підкласом int (True = 1).

# 28
a = 5
b = 10
a = a + b
b = a - b
a = a - b
print("a =", a, "b =", b)

# 29
deposit = 10000
rate = 0.12
years = 3
print("Сума депозиту:", deposit * (1 + rate) ** years)

# 30
dash = "-"
print(dash * 20)
print("Результат: ", end="")
print(2 ** 20)
