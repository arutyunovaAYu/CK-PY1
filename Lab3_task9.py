salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
money_capital = 0
need_money = money_capital + (- salary + spend) # после первого месяца, который без процентов пока
for i in range(1,10):
    spend += increase * spend
    need_money = need_money + (- salary + spend)
    #if (new_money_capital > 0):
        #month = month + 1

print(round(need_money))