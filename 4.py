import random

cnt = 0
right = 0

for i in range(100):
    a = random.randint(1, 10)
    b = random.randint(1, 10)

    ans = int(a + b)

    print(a, "+", b, "=", end=" ")
    ans2 = int(input())

    if ans == ans2:
        print("Правильно!")
        right += 1
    else:
        print("Ответ неверный")
        cnt += 1
    if cnt == 3:
        print("Игра окончена. Правильный ответов: ", right)
        exit()