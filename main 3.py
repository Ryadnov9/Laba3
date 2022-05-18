"""Визначити, чи є задане натуральне число досконалим, тобто рівним сумі всіх своїх дільників,
крім самого цього числа (наприклад, число 6 досконале: 6 = 1 + 2 + 3)."""

numb = int(input("Введіть ціле число: "))

deletellist = {1}
sumlist = 1
i = 2
while i * i <= numb and sumlist <= numb:
    if numb % i == 0:
        sumlist += i + (numb // i if i != numb // i else 0)
        deletellist.update({i, numb // i})
    i += 1

if sumlist == numb:
    print(*sorted(deletellist))
else:
    print(0)
