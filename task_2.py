from math import sqrt
def prime(a) :
    for i in range(2, int(sqrt(a)) + 1):
        if a % i == 0:
            return False
    prime(a + 2)
    return True

n = int(input("Введите число: "))
if prime(n) and prime(n - 2) and prime(n + 2):
    print(True)
else :
    print(False)