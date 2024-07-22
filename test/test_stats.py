import pytest
from src.stats import Stats
from src.ui.dialog import Ui_MainWindow


@pytest.fixture
def stats_processor():
    ui = Ui_MainWindow()
    return Stats(ui)


def test_get_stats_existing(stats_processor):
    test_data = {
        "students": [
            {"name": "John", "age": 25, "grades": ["80", "90", "70"], "passed": True},
            {"name": "Jane", "age": 23, "grades": [85, "95"], "passed": True},
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


def test_get_stats_boolean_only(stats_processor):
    test_data = {
        "flags": [
            {"flag1": True, "flag2": False},
            {"flag1": True, "flag2": True},
            {"flag1": False, "flag2": True},
        ]
    }
    result = stats_processor.get_stats(test_data)
    assert result["flag1"]["true"] == 66.67
    assert result["flag1"]["false"] == 33.33
    assert result["flag2"]["true"] == 66.67
    assert result["flag2"]["false"] == 33.33


def test_get_stats_numeric_only(stats_processor):
    test_data = {
        "measurements": [
            {"temp": 20.5, "pressure": 1013},
            {"temp": 25.0, "pressure": 1015},
            {"temp": 22.3, "pressure": 1010},
        ]
    }
    result = stats_processor.get_stats(test_data)
    assert result["temp"]["min"] == 20.5
    assert result["temp"]["max"] == 25.0
    assert result["temp"]["avg"] == 22.6
    assert result["pressure"]["min"] == 1010
    assert result["pressure"]["max"] == 1015
    assert result["pressure"]["avg"] == 1012.67


def test_get_stats_list_only(stats_processor):
    test_data = {
        "collections": [
            {"list1": [1, 2, 3], "list2": [4, 5]},
            {"list1": [1, 2], "list2": [3, 4, 5, 6]},
            {"list1": [1, 2, 3, 4], "list2": [5]},
        ]
    }
    result = stats_processor.get_stats(test_data)
    assert result["list1"]["min_size"] == 2
    assert result["list1"]["max_size"] == 4
    assert result["list1"]["average_size"] == 3.0
    assert result["list2"]["min_size"] == 1
    assert result["list2"]["max_size"] == 4
    assert result["list2"]["average_size"] == 2.33


def test_get_stats_mixed_and_edge_cases(stats_processor):
    test_data = {
        "mixed": [
            {"bool": True, "num": 0, "list": []},
            {"bool": False, "num": -10.5, "list": [1] * 10},
            {"bool": True, "num": 1000000, "list": [1, 2, 3]},
        ]
    }
    result = stats_processor.get_stats(test_data)
    assert result["bool"]["true"] == 66.67
    assert result["bool"]["false"] == 33.33
    assert result["num"]["min"] == -10.5
    assert result["num"]["max"] == 1000000
    assert result["num"]["avg"] == 333329.83
    assert result["list"]["min_size"] == 0
    assert result["list"]["max_size"] == 10
    assert result["list"]["average_size"] == 4.33


@pytest.mark.parametrize(
    "test_function",
    [
        test_get_stats_existing,
        test_get_stats_boolean_only,
        test_get_stats_numeric_only,
        test_get_stats_list_only,
        test_get_stats_mixed_and_edge_cases,
    ],
)
def test_all(stats_processor, test_function):
    test_function(stats_processor)
