import pytest
from src.data import Data


@pytest.fixture
def data_processor():
    return Data()


def test_json_file(data_processor, tmp_path):
    json_content = (
        '{"student": [{"name": "John", "age": 25}, {"name": "Jane", "age": 24}]}'
    )
    json_file = tmp_path / "test.json"
    json_file.write_text(json_content)

    result = data_processor.process(str(json_file))
    assert result == {
        "student": [{"name": "John", "age": 25}, {"name": "Jane", "age": 24}]
    }


def test_csv_file(data_processor, tmp_path):
    csv_content = "name;age\nJohn;25\nJane;24"
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_content)

    result = data_processor.process(str(csv_file))
    assert result == {
        "test": [{"name": "John", "age": 25}, {"name": "Jane", "age": 24}]
    }


def test_xml_file(data_processor, tmp_path):
    xml_content = """
    <students>
        <student>
            <name>John</name>
            <age>25</age>
        </student>
    </students>
    """
    xml_file = tmp_path / "test.xml"
    xml_file.write_text(xml_content)

    result = data_processor.process(str(xml_file))
    assert result == {"student": [{"name": "John", "age": 25}]}


def test_yml_file(data_processor, tmp_path):
    yml_content = """
    student:
      - name: John
        age: 25
    """
    yml_file = tmp_path / "test.yml"
    yml_file.write_text(yml_content)

    result = data_processor.process(str(yml_file))
    assert result == {"student": [{"name": "John", "age": 25}]}


def test_invalid_file(data_processor, tmp_path):
    bad_content = "bad content"
    bad_file = tmp_path / "bad.yml"
    bad_file.write_text(bad_content)

    result = data_processor.process(str(bad_file))
    assert result == "bad content"
