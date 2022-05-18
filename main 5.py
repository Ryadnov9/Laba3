""""11. Дано число A (> 1). Вивести найменше з цілих чисел K,
для яких сума 1 + 1/2 + … + 1/K будет більше A, і саму цю суму."""

import random

A = random.randrange(2, 10)
print('A = ', A)

K = 1.0
S = 1.0
while S + 1 / (K + 1) > A:
    K += 1
    x = 1 / K
    S += x
    print("K = {0}, 1/K = {1}, S = {2}".format(K, x, S))

print()
print("K = {0}, S = {1}".format(K, S))
print("K+1 = {0}, S_next = {1}".format(K + 1, S + 1 / (K + 1)))