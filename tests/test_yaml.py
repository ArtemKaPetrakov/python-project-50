from gendiff.gendiff import generate_diff
import tests.fixtures.expected as expected


def test_flat_yaml():
    assert generate_diff('file1.yml', 'file2.yml') == expected.PLAIN