from gendiff.gendiff import generate_diff
import tests.fixtures.expected as expected


def test_tree_yaml():
    assert generate_diff('file_tree1.yaml', 'file_tree2.yaml') == expected.TREE
