def caching_fibonacci(): # Створюємо порожній словник для кешування
    cache = {}
    def fibonacci(n):
        if n <= 0: # Якщо n <= 0, повертаємо 0
            return 0
        elif n == 1: # Якщо n == 1, повертаємо 1
            return 1 # Якщо n у cache, повертаємо значення з кешу
        elif n in cache:
            return cache[n]
        else: # Обчислюємо fibonacci(n) рекурсивно
            result = fibonacci(n - 1) + fibonacci(n - 2)
            cache[n] = result # Зберігаємо результат у кеші
            return result 
    return fibonacci # Повертаємо функцію fibonacci

fib = caching_fibonacci() # Приклад використання

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
