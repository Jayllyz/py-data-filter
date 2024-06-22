import json
import csv


class Data:
    def __init__(self):
        pass

    def process(self, file: str):
        ext = file.split(".")[-1]

        if ext == "json":
            return self.json_file(file)
        elif ext == "csv":
            return self.csv_file(file)

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
                student = {}
                for i, value in enumerate(row):
                    if i < len(header) - 1:
                        if header[i] == "age":
                            student[header[i]] = int(value)
                        elif header[i] in {"apprentice"}:
                            student[header[i]] = value.lower() == "true"
                        else:
                            student[header[i]] = value
                    else:
                        student[header[i]] = [
                            int(grade) if grade.isdigit() else float(grade)
                            for grade in value.split(",")
                        ]
                data[file_name].append(student)
        return data
