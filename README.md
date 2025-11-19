# Анализ эффективности работы разработчиков

Скрипт предназначен для обработки CSV-файлов с данными о закрытых задачах разработчиков и формирования отчётов.  
Текущая реализация поддерживает отчёт `performance`, который вычисляет среднюю эффективность по каждой позиции и выводит результат в виде таблицы, отсортированной по убыванию эффективности.

## Пример структуры данных
```csv
name,position,completed_tasks,performance,skills,team,experience_years 
Alex Ivanov,Backend Developer,45,4.8,"Python, Django, PostgreSQL, Docker",API Team,5 
Maria Petrova,Frontend Developer,38,4.7,"React, TypeScript, Redux, CSS",Web Team,4 
John Smith,Data Scientist,29,4.6,"Python, ML, SQL, Pandas",AI Team,3 
Anna Lee,DevOps Engineer,52,4.9,"AWS, Kubernetes, Terraform, Ansible",Infrastructure Team,6 
Mike Brown,QA Engineer,41,4.5,"Selenium, Jest, Cypress, Postman",Testing Team,4
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
python main.py --files employees1.csv employees2.csv --report performance
```
### Пример вывода:
<img width="1407" height="358" alt="image" src="https://github.com/user-attachments/assets/522dfd5e-4910-484c-a7e9-6400cb991e50" />


## Добавление новых отчётов
Чтобы добавить новый тип отчёта:
1. Создайте новый файл в папке reports, например skills.py
2. Определите класс с методом generate(self, files) по аналогии с PerformanceReport
3. Добавьте класс в словарь REPORTS в main.py, например:
```bash
REPORTS = {
    "performance": PerformanceReport,
    "skills": SkillsReport,  # ваш новый отчёт
}
```

## Тестирование
Запуск тестов и покрытия:
```bash
python -m pytest --cov=reports --cov=main -v
```

Покрытие кода: 87%
<img width="1627" height="503" alt="image" src="https://github.com/user-attachments/assets/bff7ff29-e294-4edb-9ebf-312a21d7760f" />

