import pytest
from reports.performance import PerformanceReport


@pytest.mark.parametrize(
    "files, expected",
    [
        (
            ["sample_file_one"],
            [
                {"position": "Backend Developer", "average_performance": 4.8},
                {"position": "Frontend Developer", "average_performance": 4.7},
            ],
        ),
        (
            ["sample_file_one", "sample_file_two"],
            [
                {"position": "DevOps Engineer", "average_performance": 4.9},
                {"position": "Backend Developer", "average_performance": 4.8},
                {"position": "Frontend Developer", "average_performance": 4.7},
                {"position": "Data Scientist", "average_performance": 4.6},
            ],
        ),
    ],
)
def test_performance_generate(files, expected, request):
    """
    Проверяет, что отчет корректно считает среднюю эффективность по позициям
    и сортирует результаты
    """
    resolved_files = [request.getfixturevalue(name) for name in files]

    report = PerformanceReport()
    result = report.generate(resolved_files)

    assert result == expected
