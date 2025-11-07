import io
import csv
import tempfile
from reports.average_rating import AverageRatingReport


def create_csv_file(data):
    """Создаёт временный CSV-файл и возвращает путь к нему"""
    tmp = tempfile.NamedTemporaryFile(mode="w+", newline="", delete=False, encoding="utf-8")
    writer = csv.DictWriter(tmp, fieldnames=["name", "brand", "price", "rating"])
    writer.writeheader()
    writer.writerows(data)
    tmp.flush()
    return tmp.name


def test_average_rating_report_single_file():
    data = [
        {"name": "iphone", "brand": "apple", "price": "999", "rating": "4.9"},
        {"name": "samsung s23", "brand": "samsung", "price": "1199", "rating": "4.8"},
        {"name": "redmi", "brand": "xiaomi", "price": "199", "rating": "4.6"},
    ]
    path = create_csv_file(data)

    report = AverageRatingReport()
    result = report.generate([path])

    assert result == [
        {"brand": "apple", "average_rating": 4.9},
        {"brand": "samsung", "average_rating": 4.8},
        {"brand": "xiaomi", "average_rating": 4.6},
    ]


def test_average_rating_report_multiple_files():
    data1 = [
        {"name": "iphone", "brand": "apple", "price": "999", "rating": "4.9"},
        {"name": "samsung s23", "brand": "samsung", "price": "1199", "rating": "4.8"},
    ]
    data2 = [
        {"name": "iphone mini", "brand": "apple", "price": "899", "rating": "4.7"},
        {"name": "redmi", "brand": "xiaomi", "price": "199", "rating": "4.6"},
    ]

    path1 = create_csv_file(data1)
    path2 = create_csv_file(data2)

    report = AverageRatingReport()
    result = report.generate([path1, path2])

    # Средние: apple (4.8), samsung (4.8), xiaomi (4.6)
    assert result == [
        {"brand": "apple", "average_rating": 4.8},
        {"brand": "samsung", "average_rating": 4.8},
        {"brand": "xiaomi", "average_rating": 4.6},
    ]


def test_average_rating_report_ignores_whitespace_in_brand():
    data = [
        {"name": "iphone", "brand": "  apple  ", "price": "999", "rating": "4.9"},
    ]
    path = create_csv_file(data)

    report = AverageRatingReport()
    result = report.generate([path])

    assert result[0]["brand"] == "apple"
