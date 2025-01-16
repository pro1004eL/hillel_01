# Використовуємо офіційний образ Python версії 3.12
FROM python:3.12

# Встановлюємо залежності для тестування
RUN pip install pytest
RUN pip install psycopg2

# Копіюємо файли з локальної директорії в контейнер
COPY . /app

# Задаємо робочу директорію контейнера
WORKDIR /app

# set up requirements
RUN pip install --no-cache-dir -r requirements.txt

# Виконуємо команду для запуску тестів під час створення контейнера
CMD ["pytest", "tests/db_tests/user_dk_tests", "-m", "user_dk", "-v", "--alluredir=/app/allure-results"]
