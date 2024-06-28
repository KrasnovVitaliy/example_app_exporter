"""Example dict exporter."""

import json

from app_exporter.base_exporter import BaseExporter


class DictExporter(BaseExporter):
    """Dict exporter.

    Simple json str to dict exporter
    """

    name = "dict_exporter"
    description = "JSON string to dict exporter"

    def dump(self, data: str) -> dict:
        """Dump JSON string to dict."""
        return json.loads(data)
