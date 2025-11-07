import csv
from collections import defaultdict


class AverageRatingReport:
    """
    Класс для формирования отчёта со средним рейтингом брендов
    """
    def generate(self, files):
        """
        Генерирует отчёт «average-rating» по переданным CSV-файлам
        """
        brand_ratings = defaultdict(list)

        for file_path in files:
            with open(file_path, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    brand = row["brand"].strip()
                    rating = float(row["rating"])
                    brand_ratings[brand].append(rating)

        # формируем список словарей со средними значениями рейтингов
        averages = []
        for brand, ratings in brand_ratings.items():
            avg = round(sum(ratings) / len(ratings), 2)
            averages.append({"brand": brand, "average_rating": avg})

        # сортируем бренды по среднему рейтингу в порядке убывания
        return sorted(averages, key=lambda x: x["average_rating"], reverse=True)
