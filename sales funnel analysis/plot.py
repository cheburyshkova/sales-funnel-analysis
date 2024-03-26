import matplotlib.pyplot as plt

stages = ['Просмотры', 'Добавления в корзину', 'Покупки']
counts = [592, 311, 97]

plt.figure(figsize=(10, 6)) 
plt.bar(stages, counts, color=['blue', 'orange', 'green'])


plt.title('Воронка продаж интернет-магазина') 
plt.xlabel('Этапы воронки')
plt.ylabel('Количество пользователей')

plt.show()