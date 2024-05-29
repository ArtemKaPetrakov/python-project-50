from gendiff.gendiff import generate_diff
import tests.fixtures.expected as expected


def test_flat_yaml():
    assert generate_diff('./tests/fixtures/file1.yml', './tests/fixtures/file2.yml') == expected.SIMPLE