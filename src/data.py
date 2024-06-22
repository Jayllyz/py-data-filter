import json
import csv
import xml.etree.ElementTree as xml
import yaml


class Data:
    def __init__(self):
        pass

    def process(self, file: str):
        ext = file.split(".")[-1]

        if ext == "json":
            return self.json_file(file)
        elif ext == "csv":
            return self.csv_file(file)
        elif ext == "xml":
            return self.xml_file(file)
        elif ext == "yml" or ext == "yaml":
            return self.yml_file(file)

    def json_file(self, file: str):
        data = {}
        with open(file, "r") as f:
            data = json.load(f)
        return data

    def csv_file(self, file: str):
        file_name = file.split("/")[-1].split(".")[0]
        data = {}
        with open(file, "r") as f:
            reader = csv.reader(f, delimiter=";")
            header = next(reader)
            data[file_name] = []
            for row in reader:
                array = {}
                for i, value in enumerate(row):
                    if value.find(",") == -1:
                        array[header[i]] = self.correct_type(value)
                    else:
                        array[header[i]] = [
                            self.correct_type(v) for v in value.split(",")
                        ]
                data[file_name].append(array)
        return data

    def xml_file(self, file: str):
        tree = xml.parse(file)
        root = tree.getroot()
        name = root[0].tag

        data = {name: []}

        for child in root:
            array = {}
            for sub_child in child:
                if len(sub_child) > 0:
                    array[sub_child.tag] = [
                        self.correct_type(sub_sub_child.text)
                        for sub_sub_child in sub_child
                    ]
                else:
                    array[sub_child.tag] = self.correct_type(sub_child.text)
            data[name].append(array)
        return data

    def yml_file(self, file: str):
        with open(file, "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        return data

    def correct_type(self, value: str):
        value = value.strip('"')
        if value.lower() in ["true", "false"]:
            return bool(value.lower() == "true")
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return value
