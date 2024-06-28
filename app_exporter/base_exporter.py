"""Base exporter."""

from abc import abstractmethod
from typing import Any


class BaseExporter:
    """Base Exporter class.

    Attributes
    ----------
        name            Exporter unique name
        description     Exporter description

    """

    name = "base_exporter"
    description = "Base exporter"

    @abstractmethod
    def dump(self, data: Any) -> Any:  # noqa: ANN401
        """Dump data to needed format."""
        raise Exception("not_implemented")  # noqa: EM101, TRY002
