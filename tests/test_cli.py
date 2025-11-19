import sys
import pytest
from main import main


def test_cli_success(monkeypatch, capsys, sample_file_one):
    """Проверяет успешный запуск CLI с выводом таблицы"""
    monkeypatch.setattr(
        sys,
        "argv",
        ["main.py", "--files", sample_file_one, "--report", "performance"],
    )
    main()
    out = capsys.readouterr().out
    assert "Backend Developer" in out
    assert "4.8" in out


def test_cli_invalid_report(monkeypatch):
    """Проверяет, что argparse не примет неизвестный отчёт"""
    monkeypatch.setattr(
        sys, "argv", ["main.py", "--files", "a.csv", "--report", "unknown"]
    )
    with pytest.raises(SystemExit):
        main()


def test_cli_file_not_found(monkeypatch):
    """Проверяет обработку FileNotFoundError"""
    fake = "no_such_file.csv"
    monkeypatch.setattr(
        sys, "argv", ["main.py", "--files", fake, "--report", "performance"]
    )
    with pytest.raises(SystemExit) as exc:
        main()
    assert exc.value.code == 1
