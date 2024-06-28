"""Example dummy exporter."""

from app_exporter.base_exporter import BaseExporter


class JsonExporterNew(BaseExporter):
    """Dummy exporter.

    Exporter returns the same answer to al imput data
    """

    name = "dummy_exporter"
    description = "Dummy exporter. Returns the same answer"

    def dump(self, data: str) -> dict:  # noqa: ARG002
        """Dump JSON string to the same output."""
        return {"dummy": "exporter"}
