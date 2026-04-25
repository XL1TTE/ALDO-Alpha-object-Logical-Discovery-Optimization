from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..generator import PatternModel

class BaseFormatter(ABC):
    @abstractmethod
    def format(self, model: PatternModel) -> str:
        """Formats a PatternModel object into a string."""
        pass

    @abstractmethod
    def get_extension(self) -> str:
        """Returns the file extension for this formatter."""
        pass

    def get_header(self) -> str:
        """Returns an optional header for the entire file."""
        return ""

    def get_separator(self) -> str:
        """Returns a separator between models."""
        return "\n"
