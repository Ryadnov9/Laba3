"""12. Дано дійсне число - ціна 1 кг цукерок. Вивести вартість 1, 2, ..., 10 кг"""

n = float(input())
for i in range(10):
    i = i * n
    print(i)