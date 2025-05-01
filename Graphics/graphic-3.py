import pandas as pd
import matplotlib.pyplot as plt

file_path = 'sofa_prices.csv'
data = pd.read_csv(file_path)
average_price = data['Цена'].mean()
print(f"Средняя цена на диваны: {average_price:.2f} руб.")


plt.hist(data, bins=20, edgecolor='black')
plt.title('Гистограмма цен на диваны с сайта divan.ru')
plt.xlabel('Цена (руб.)')
plt.ylabel('Количество')

plt.grid(True)
plt.show()
