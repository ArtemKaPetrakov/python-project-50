from gendiff.gendiff import generate_diff
import tests.fixtures.expected as expected


def test_tree_json():
    assert generate_diff('file_tree1.json', 'file_tree2.json') == expected.TREE