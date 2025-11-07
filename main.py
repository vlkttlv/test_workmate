import argparse
import sys
from tabulate import tabulate
from reports.average_rating import AverageRatingReport


REPORTS = {
    "average-rating": AverageRatingReport,
}


def parse_args():
    """
    Разбирает аргументы командной строки
    """
    parser = argparse.ArgumentParser(description="Анализ рейтингов брендов по CSV-файлам")
    parser.add_argument(
        "--files", nargs="+", required=True, help="Пути к CSV-файлам с данными о товарах"
        )
    parser.add_argument(
        "--report", required=True, help="Тип отчета"
        )
    return parser.parse_args() # возвращаем объект с аргументами


def main():
    args = parse_args()

    # проверка, существует ли запрошенный отчёт в словаре REPORTS
    if args.report not in REPORTS:
        print(f"Неизвестный отчет: {args.report}", file=sys.stderr)
        print(f"Доступные отчеты: {', '.join(REPORTS.keys())}", file=sys.stderr)
        sys.exit(1)

    # получаем класс отчёта и создаём его экземпляр
    report_class = REPORTS[args.report]()
    try:
        data = report_class.generate(args.files)
    except FileNotFoundError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)

    print(tabulate(data, headers="keys", tablefmt="pretty"))


if __name__ == "__main__":
    main()
