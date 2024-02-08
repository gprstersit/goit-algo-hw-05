def caching_fibonacci():
    # Створюємо порожній словник для кешування
    cache = {}

    def fibonacci(n):
        # Якщо n <= 0, повертаємо 0
        if n <= 0:
            return 0
        # Якщо n == 1, повертаємо 1
        elif n == 1:
            return 1
        # Якщо n у cache, повертаємо значення з кешу
        elif n in cache:
            return cache[n]
        else:
            # Обчислюємо fibonacci(n) рекурсивно
            result = fibonacci(n - 1) + fibonacci(n - 2)
            # Зберігаємо результат у кеші
            cache[n] = result
            return result

    # Повертаємо функцію fibonacci
    return fibonacci

# Приклад використання
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
