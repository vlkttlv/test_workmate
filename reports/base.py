from abc import ABC, abstractmethod
from typing import Iterable, List, Dict


class Report(ABC):
    """Абстрактный базовый класс для отчётов"""

    @abstractmethod
    def generate(self, files: Iterable[str]) -> List[Dict]:
        """
        Формирует отчёт на основании переданных CSV-файлов
        """
        raise NotImplementedError
