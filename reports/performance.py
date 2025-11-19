import csv
from collections import defaultdict
from typing import Iterable, List, Dict, TypedDict
from reports.base import Report


class EmployeeRecord(TypedDict):
    """TypedDict для одной строки входного CSV"""

    name: str
    position: str
    completed_tasks: str
    performance: str
    skills: str
    team: str
    experience_years: str


class PerformanceReport(Report):
    """
    Класс для формирования отчёта со средним эффективностью по позициям
    """

    def generate(self, files: Iterable[str]) -> List[Dict]:
        """
        Генерирует отчёт performance» по переданным CSV-файлам
        """
        pos_perf: defaultdict[str, List[float]] = defaultdict(list)

        for path in files:
            with open(path, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for raw in reader:
                    row: EmployeeRecord = raw
                    position = row["position"].strip()
                    perf_value = float(row["performance"])
                    pos_perf[position].append(perf_value)

        # Формируем итоговый список словарей
        results: List[Dict] = []
        for position, perf_list in pos_perf.items():
            avg = round(sum(perf_list) / len(perf_list), 2)
            results.append({"position": position, "average_performance": avg})

        # Сортируем по эффективности
        results.sort(key=lambda x: x["average_performance"], reverse=True)
        return results
