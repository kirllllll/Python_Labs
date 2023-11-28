salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

summ = spend

for i in range(2, months + 1):
    spend += spend * increase
    summ = summ + spend
money_capital = summ - salary * months
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {round(money_capital, 2)}")
