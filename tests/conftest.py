import csv
import tempfile
from pathlib import Path
from typing import Iterable
import pytest


def _create_tmp_csv(rows: Iterable[dict], fieldnames: list[str]) -> str:
    """Создает временный CSV-файл и возвращает путь"""
    tmp = tempfile.NamedTemporaryFile(
        mode="w+", newline="", delete=False, encoding="utf-8"
    )
    writer = csv.DictWriter(tmp, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
    tmp.flush()
    return tmp.name


@pytest.fixture
def sample_file_one() -> str:
    """Генерирует первый файл для отчета"""
    rows = [
        {
            "name": "Alex Ivanov",
            "position": "Backend Developer",
            "completed_tasks": "45",
            "performance": "4.8",
            "skills": "Python, Django, PostgreSQL, Docker",
            "team": "API Team",
            "experience_years": "5",
        },
        {
            "name": "Maria Petrova",
            "position": "Frontend Developer",
            "completed_tasks": "38",
            "performance": "4.7",
            "skills": "React, TypeScript, Redux, CSS",
            "team": "Web Team",
            "experience_years": "4",
        },
    ]
    return _create_tmp_csv(
        rows,
        [
            "name",
            "position",
            "completed_tasks",
            "performance",
            "skills",
            "team",
            "experience_years",
        ],
    )


@pytest.fixture
def sample_file_two() -> str:
    """Генерирует второй файл для отчета"""
    rows = [
        {
            "name": "John Smith",
            "position": "Data Scientist",
            "completed_tasks": "29",
            "performance": "4.6",
            "skills": "Python, ML, SQL, Pandas",
            "team": "AI Team",
            "experience_years": "3",
        },
        {
            "name": "Anna Lee",
            "position": "DevOps Engineer",
            "completed_tasks": "52",
            "performance": "4.9",
            "skills": "AWS, Kubernetes, Terraform, Ansible",
            "team": "Infrastructure Team",
            "experience_years": "6",
        },
    ]
    return _create_tmp_csv(
        rows,
        [
            "name",
            "position",
            "completed_tasks",
            "performance",
            "skills",
            "team",
            "experience_years",
        ],
    )
