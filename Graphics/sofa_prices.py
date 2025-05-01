import csv


def clean_price(price):
    cleaned = price.replace('руб.', '').replace(' ','')
    return int(cleaned) if cleaned.isdigit() else None

input_file = 'sofas.csv'
output_file = 'sofa_prices.csv'

cleaned_rows = []

with open(input_file, mode='r', encoding='utf-8') as infile:
   reader = csv.reader(infile)
   header = next(reader)
   for row in reader:
       if row and row[0].strip():
           price = clean_price(row[0])
           if price is not None:
               cleaned_rows.append([price])


with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['Цена'])
    writer.writerows(cleaned_rows)

output_file

print(f'Обработанные данные сохранены в файле {output_file}')