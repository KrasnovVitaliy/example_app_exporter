"""Exporter factory."""

import importlib.util
import inspect
import os
import sys
from typing import Any, Iterator

from .base_exporter import BaseExporter


class ExporterFactory:
    """Exporter factory.

    Uses to manage all available exporters in provided base path.
    """

    def __init__(self, exporters_path: str) -> None:
        """Export factory init."""
        self.exporters_path = exporters_path

    @property
    def exporters(self) -> Iterator[BaseExporter]:
        """Available exporters list."""
        return self.__get_exporters()

    def get_exporter_by_name(self, name: str) -> BaseExporter:
        """Get exporter instance by exporter name."""
        for exporter_class in self.__get_exporters():
            if exporter_class.name == name:
                return exporter_class()
        return None

    def __get_exporters(self) -> Iterator[BaseExporter]:
        for pyfile in self.__get_all_py_files(self.exporters_path):
            yield from self.__get_classes(pyfile, BaseExporter)

    def __get_all_py_files(self, base_path: str) -> Iterator[str]:
        for dirpath, _dirnames, filenames in os.walk(base_path):
            for filename in filenames:
                if filename.endswith(".py"):
                    filepath = os.path.join(dirpath, filename)  # noqa: PTH118
                    yield filepath

    def __get_classes(self, file_path: str, base_class: Any) -> Iterator[BaseExporter]:  # noqa: ANN401
        module_name = os.path.splitext(os.path.basename(file_path))[0]  # noqa: PTH122, PTH119
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)

        for _name, member in inspect.getmembers(module, inspect.isclass):
            if issubclass(member, base_class) and member.__module__ == module_name:
                yield member
