money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

new_money_capital = money_capital + (salary - spend) # после первого месяца, который без процентов пока
for i in range(1,10):
    spend += increase * spend
    new_money_capital = new_money_capital + (salary - spend)
    if (new_money_capital > 0):
        month = month + 1

print(month+1) #прибавляем первый месяц