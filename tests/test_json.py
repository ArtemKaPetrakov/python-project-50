from gendiff.gendiff import generate_diff
import tests.fixtures.expected as expected


def test_flat_json():
    assert generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json') == expected.SIMPLE