import pytest
from src.stats import Stats
from src.ui.dialog import Ui_MainWindow


@pytest.fixture
def stats_processor():
    ui = Ui_MainWindow()
    return Stats(ui)


def test_get_stats(stats_processor):
    test_data = {
        "students": [
            {"name": "John", "age": 25, "grades": [80, 90, 70], "passed": True},
            {"name": "Jane", "age": 23, "grades": [85, 95], "passed": True},
            {"name": "Bob", "age": 22, "grades": [70, 60, 80], "passed": False},
        ]
    }

    result = stats_processor.get_stats(test_data)

    assert result["age"]["min"] == 22
    assert result["age"]["max"] == 25
    assert result["age"]["avg"] == 23.33
    assert result["grades"]["min_size"] == 2
    assert result["grades"]["max_size"] == 3
    assert result["grades"]["average_size"] == 2.67
    assert result["passed"]["true"] == 66.67
    assert result["passed"]["false"] == 33.33
