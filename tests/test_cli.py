import sys
import tempfile
import csv
import pytest
from main import main


def create_csv_file(data):
    """Создаёт временный CSV-файл и возвращает путь к нему"""
    tmp = tempfile.NamedTemporaryFile(
        mode="w+", newline="", delete=False, encoding="utf-8"
        )
    writer = csv.DictWriter(tmp, fieldnames=["name", "brand", "price", "rating"])
    writer.writeheader()
    writer.writerows(data)
    tmp.flush()
    return tmp.name


def test_cli_average_rating(monkeypatch, capsys):
    """Проверяет успешный запуск CLI и корректный вывод таблицы"""
    data = [
        {"name": "iphone", "brand": "apple", "price": "999", "rating": "4.9"},
        {"name": "samsung", "brand": "samsung", "price": "1199", "rating": "4.8"},
    ]
    path = create_csv_file(data)

    monkeypatch.setattr(
        sys,
        "argv",
        ["main.py", "--files", path, "--report", "average-rating"]
        )

    main()

    output = capsys.readouterr().out
    assert "apple" in output
    assert "samsung" in output
    assert "4.9" in output


def test_cli_invalid_report(monkeypatch, capsys):
    """Проверяет, что при неизвестном типе отчёта CLI завершается с ошибкой"""
    monkeypatch.setattr(
        sys,
        "argv",
        ["main.py", "--files", "file.csv", "--report", "unknown-report"]
        )
    with pytest.raises(SystemExit):
        main()

    err = capsys.readouterr().err
    assert "Неизвестный отчет" in err


def test_cli_file_not_found(monkeypatch, capsys):
    """Проверяет обработку кейса, когда указанный CSV-файл не найден"""
    fake_path = "nonexistent.csv"
    monkeypatch.setattr(
        sys,
        "argv",
        ["main.py", "--files", fake_path, "--report", "average-rating"]
        )

    with pytest.raises(SystemExit) as e:
        main()
    assert e.value.code == 1

    err = capsys.readouterr().err
    assert "Ошибка:" in err
    assert fake_path in err
