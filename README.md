# Анализ рейтинга брендов

Скрипт предназначен для обработки CSV-файлов с данными о товарах и формирования отчётов.  
Текущая реализация поддерживает отчёт average-rating, который вычисляет средний рейтинг по каждому бренду и выводит результат в виде таблицы.

## Пример структуры данных
```csv
name,brand,price,rating
iphone 15 pro,apple,999,4.9
galaxy s23 ultra,samsung,1199,4.8
redmi note 12,xiaomi,199,4.6
```

## Установка зависимостей
Создайте и активируйте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
Установите зависимости:
```bash
pip install -r requirements.txt
```

## Пример запуска
```bash
python main.py --files products1.csv products2.csv --report average-rating
```
### Пример вывода:
<img width="1187" height="265" alt="image" src="https://github.com/user-attachments/assets/f1a0c422-95a5-4fb7-91d6-b282d012640a" />

## Добавление новых отчётов
Чтобы добавить новый тип отчёта:
1. Создайте новый файл в папке reports, например average_price.py
2. Определите класс с методом generate(self, files) по аналогии с AverageRatingReport
3. Добавьте класс в словарь REPORTS в main.py, например:
```bash
REPORTS = {
    "average-rating": AverageRatingReport,
    "average-price": AveragePriceReport, # ваш новый отчёт
}
```

## Тестирование
Запуск тестов и покрытия:
```bash
python -m pytest --cov=reports --cov=main -v
```

Покрытие кода: 98%
<img width="1189" height="721" alt="image" src="https://github.com/user-attachments/assets/e736c035-abb5-4abe-ac5f-ee8f13fc392e" />
