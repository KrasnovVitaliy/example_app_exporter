from app_exporter.exporter_factory import ExporterFactory

if __name__ == "__main__":
    factory = ExporterFactory(exporters_path="./exporters")
    print("List of all available exporters\n")
    for exporter in factory.exporters:
        print(exporter.name, exporter.description)

    print("\n")
    test_data = '{"key": "value", "item":0}'
    print(factory.get_exporter_by_name("dict_exporter").dump(test_data))
    print(factory.get_exporter_by_name("dummy_exporter").dump(test_data))
