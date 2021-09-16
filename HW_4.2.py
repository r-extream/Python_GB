# Решето Эратосфена

import cProfile

def Eratosfen(n):
    if n < 2:
        return None

    limit = pow(n, 2)
    sv_ = [True] * limit
    sv_[0] = False
    sv_[1] = False

    i = 4
    while i < limit:
        if sv_[i] and i % 2 == 0:
            sv_[i] = False
        elif sv_[i]:
            j = i * 2
            while j < limit:
                sv_[j] = False
                j += i

        i += 1

    return [i for i, f in enumerate(sv_) if f][n]


cProfile.run('sv(1000)')


# Без решета Эратосфена

def is_prime(n):
    if n < 2:
        return False

    if n == 2:
        return True

    limit = pow(n, 0.5)

    i = 2
    while i <= limit:
        if not n % i:
            return False

        i += 1

    return True


def prime(n):
    cnt = 0
    i = 2
    while cnt < n:
        if is_prime(i):
            cnt += 1
        i += 1

    return i - 1


cProfile.run('prime(1000)')
