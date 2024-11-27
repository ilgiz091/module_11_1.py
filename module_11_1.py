import requests

# 1. Запрос данных с сайта
url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)

# 2. Проверка кода ответа
if response.status_code == 200:
    print("Запрос успешен!")
else:
    print(f"Ошибка: {response.status_code}")

# 3. Вывод данных в формате JSON
data = response.json()
print(f"Данные: {data}")

# 4.  Обработка заголовков
print(f"Заголовки ответа: {response.headers}")

# 5.  Обработка ошибок
try:
  response = requests.get("https://nonexistentwebsite.com")
  response.raise_for_status() # Вызывает исключение при ошибке
except requests.exceptions.RequestException as e:
  print(f"Произошла ошибка при запросе: {e}")



import pandas as pd

# 1. Чтение данных из CSV файла
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 28],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)
# Сохранение в CSV
df.to_csv('data.csv', index=False)
df = pd.read_csv('data.csv')

# 2. Вывод первых 2 строк
print("Первые две строки:\n", df.head(2))

# 3.  Группировка и агрегирование данных
grouped = df.groupby('City')['Age'].mean()
print("\nСредний возраст по городам:\n", grouped)

# 4. Сортировка данных
sorted_df = df.sort_values(by='Age', ascending=False)
print("\nДанные, отсортированные по возрасту (по убыванию):\n", sorted_df)

# 5. Фильтрация данных
filtered_df = df[df['Age'] > 28]
print("\nЛюди старше 28 лет:\n", filtered_df)


import matplotlib.pyplot as plt
import numpy as np

# 1. Создание простого линейного графика
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("График функции sin(x)")

# 2.  Создание точечной диаграммы (scatter plot)
x = np.random.rand(50)
y = np.random.rand(50)
plt.figure() # Создаем новый график
plt.scatter(x, y)
plt.xlabel("Случайные числа X")
plt.ylabel("Случайные числа Y")
plt.title("Точечная диаграмма")

# 3. Создание гистограммы
data = np.random.randn(1000)
plt.figure()
plt.hist(data, bins=30)
plt.xlabel("Значения")
plt.ylabel("Частота")
plt.title("Гистограмма")


plt.show()