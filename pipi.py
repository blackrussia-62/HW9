import requests
from bs4 import BeautifulSoup
import datetime

url = "https://www.cbr.ru/currency_base/daily/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', {'class': 'data'})
if table:
    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        if cols and "USD" in cols[1].text:
            usd_rate = float(cols[4].text.replace(',', '.'))
            break
else:
    usd_rate = 90.00
current_date = datetime.datetime.now().strftime("%Y-%m-%d")
with open('exchange_rates.txt', 'a', encoding='utf-8') as file:
    file.write(f"Дата: {current_date}, Курс БАКСЫ/RUB: {usd_rate}\n")

try:
    rub_amount = float(input("Введите сумму в рублях (RUB): "))
    usd_amount = rub_amount / usd_rate
    print(f"сумма зеленых: {usd_amount:.2f}")
except ValueError:
    print("нормал яз!")

print(f"Курс БАКСЫ/RUB на сегодня ({current_date}): {usd_rate} руб./USD. Данные сохранены в файл.")
