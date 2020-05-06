# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его
# улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
# Пример работы программ:
# >>> sieve(2)
# 3
# >>> prime(4)
# 7
# >>> sieve(5)
# 11
# >>> prime(1)
# 2
"""В ходе анализа реализаций 2-х функици был сделан вывод, что функция no_eratosfen - является оптимальным решением.

Оба алгоритма одинаково пропорциональны в приросте времени выполнения при увеличении входных данных, однако функция
no_eratosfen выполняется в 2 раза быстрее."""

import cProfile


def test_sieve(func):
    arr_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for n in range(25):
        assert func(n+1) == arr_prime[n]
        print(f'Test {n+1} is Ok')


def eratosfen(n):
    result = [2]
    k = 1
    while n > len(result):
        sieve = [i for i in range(k*n)]
        sieve[1] = 0
        for i in range(2, k*n):
            if sieve[i] != 0:
                j = i * 2
                while j < k*n:
                    sieve[j] = 0
                    j += i
        result = [i for i in sieve if i != 0]
        k += 1
    return result[n - 1]


# test_sieve(eratosfen)

# cProfile.run('eratosfen(100)')
# 23 function calls in 0.001 seconds

# cProfile.run('eratosfen(200)')
# 26 function calls in 0.003 seconds

# cProfile.run('eratosfen(500)')
# 29 function calls in 0.008 seconds

# "les_4_task_2.eratosfen(100)"
# 1000 loops, best of 5: 829 usec per loop

# "les_4_task_2.eratosfen(200)"
# 1000 loops, best of 5: 2.42 msec per loop

# "les_4_task_2.eratosfen(500)"
# 1000 loops, best of 5: 8.73 msec per loop

# "les_4_task_2.eratosfen(1000)"
# 1000 loops, best of 5: 18.2 msec per loop

def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def no_eratosfen(m):
    primes = [2]
    temp = 3
    while m > len(primes):
        if is_prime(temp):
            primes.append(temp)
        temp += 1
    return primes[m-1]


# test_sieve(no_eratosfen)

# cProfile.run('no_eratosfen(100)')
# 1182 function calls in 0.000 seconds

# cProfile.run('no_eratosfen(200)')
# 2646 function calls in 0.002 seconds

# cProfile.run('no_eratosfen(500)')
# 7642 function calls in 0.006 seconds

# "les_4_task_2.no_eratosfen(100)"
# 1000 loops, best of 5: 316 usec per loop

# "les_4_task_2.no_eratosfen(200)"
# 1000 loops, best of 5: 858 usec per loop

# "les_4_task_2.no_eratosfen(500)"
# 1000 loops, best of 5: 3.16 msec per loop

# "les_4_task_2.no_eratosfen(1000)"
# 1000 loops, best of 5: 9.35 msec per loop
