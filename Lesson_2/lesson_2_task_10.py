count = input("Сумма внесения: ")
x = int(count)
years = input("На какой срок: ")
y = int(years)

def bank(x, y):
     if y > 0:
        while y != 0:
            percent = (0.10 * x)
            current_balance = x + percent
            x = current_balance
            y = y - 1
        return x
        
result = bank(x, y)
print(f"Итоговая сумма: {result}")
