from typing import List
import sys
import argparse
from tabulate import tabulate
from reports.base import Report
from reports.performance import PerformanceReport

# Словарь доступных отчётов
REPORTS: dict[str, type[Report]] = {
    "performance": PerformanceReport,
}


def parse_args(argv: List[str] | None = None) -> argparse.Namespace:
    """
    Разбирает аргументы командной строки
    """
    parser = argparse.ArgumentParser(
        description="Анализ эффективности работы разработчиков"
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Пути к CSV-файлам с данными (можно передать несколько).",
    )
    parser.add_argument(
        "--report",
        required=True,
        choices=list(REPORTS.keys()),
        help="Тип отчёта. Доступные: %(choices)s",
    )
    return parser.parse_args(argv)


def main(argv: List[str] | None = None) -> None:
    """Точка входа в приложение"""
    args = parse_args(argv)

    report_name: str = args.report
    files: List[str] = args.files

    # Получаем класс отчёта по имени и создаём экземпляр
    report_cls = REPORTS[report_name]
    report = report_cls()

    try:
        data = report.generate(files)
    except FileNotFoundError as exc:
        print(f"Ошибка: {exc}", file=sys.stderr)
        sys.exit(1)
    except KeyError as exc:
        print(
            f"Ошибка: в файле отсутствует ожидаемая колонка: {exc}",
            file=sys.stderr,
        )
        sys.exit(1)
    except ValueError as exc:
        print(
            f"Ошибка: неверный формат числа в колонке performance: {exc}",
            file=sys.stderr,
        )
        sys.exit(1)

    # Вывод в консоль в виде таблицы
    if data:
        print(tabulate(data, headers="keys", tablefmt="pretty"))
    else:
        print("Нет данных для отображения.")


if __name__ == "__main__":
    main()
