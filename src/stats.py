from src.ui.dialog import Ui_MainWindow


class Stats:
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui

    def get_stats(self, data_dict: dict):
        key_value = ""
        for key, _ in data_dict.items():
            key_value = key
        data_list = data_dict[key_value]
        stats = {}

        for key in data_list[0].keys():
            stats[key] = {}

            if isinstance(data_list[0][key], bool):
                true_count = sum([1 for data in data_list if data[key]])
                false_count = len(data_list) - true_count
                stats[key]["true"] = round(true_count / len(data_list) * 100, 2)
                stats[key]["false"] = round(false_count / len(data_list) * 100, 2)

            elif isinstance(data_list[0][key], (int, float)):
                stats[key]["min"] = min([data[key] for data in data_list])
                stats[key]["max"] = max([data[key] for data in data_list])
                stats[key]["avg"] = round(
                    sum([data[key] for data in data_list]) / len(data_list), 2
                )

            elif isinstance(data_list[0][key], list):
                list_sizes = [len(data[key]) for data in data_list]
                stats[key]["min_size"] = min(list_sizes)
                stats[key]["max_size"] = max(list_sizes)
                stats[key]["average_size"] = round(sum(list_sizes) / len(data_list), 2)

        return stats
