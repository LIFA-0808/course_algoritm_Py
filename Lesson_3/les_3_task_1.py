# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9. Примечание: 8 разных ответов.

results = [0 for _ in range(8)]
for i in range(2, 100):
    for num in range(2, 10):
        if i % num == 0:
            results[num - 2] += 1
for i, item in enumerate(results):
    print(f'{i+2} - {item}')
print(results)