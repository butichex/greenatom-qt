# Указываем базовый образ
FROM python:3.9

WORKDIR /data/
# Копируем файл requirements.txt в контейнер
COPY requirements.txt .

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.txt

# Команда, которая будет выполнена при запуске контейнера
CMD ["python", "main.py"]
