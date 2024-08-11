from gendiff.gendiff import generate_diff
import tests.fixtures.expected as expected


def test_flat_json():
    assert generate_diff('file1.json', 'file2.json') == expected.SIMPLE