from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv


driver = webdriver.Chrome()

url = "https://www.divan.ru/category/divany"
driver.get(url)
time.sleep(5)

prices = driver.find_elements(By.XPATH, "//span[@data-testid='price']")
print(f"Найдено элементов с ценами: {len(prices)}")

with open("sofas.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Цена"])
    for price in prices:
        writer.writerow([price.text])

driver.quit()
