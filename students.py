import pandas as pd

data = {
    'Name' : ['Василий', 'Анастасия', 'Георгий', 'Иван', 'Ольга', 'Наталья', 'Петр', 'Егор', 'Василиса', 'Ирина'],
    'Math' : [3, 5, 4, 5, 3, 4, 4, 3, 5, 4],
    'Literature' : [5, 5, 3, 4, 5, 3, 4, 4, 3, 4],
    'Biology' : [3, 4, 5, 3, 4, 5, 3, 4, 5, 3],
    'English' : [4, 4, 4, 3, 5, 4, 4, 3, 5, 4],
    'Geography' : [4, 5, 4, 4, 5, 3, 4, 4, 5, 4]

}

df = pd.DataFrame(data)

print(df.head())

average_value = df[['Math', 'Literature', 'Biology', 'English', 'Geography']].mean()
print(average_value)

median_value = df[['Math', 'Literature', 'Biology', 'English', 'Geography']].median()
print(median_value)

Q1_math = df['Math'].quantile(0.25)
Q3_math = df['Math'].quantile(0.75)
IQR = Q3_math - Q1_math

print(f'Первый квартиль по математике - {Q1_math}')
print(f'Третий квартиль по математике - {Q3_math}')
print(f'Межквартильный размах - {IQR}')

std_value = df ['Math'].std()
print(f'Стандартное отклонение - {std_value}')
