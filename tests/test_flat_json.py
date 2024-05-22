from gendiff.gendiff import generate_diff
import tests.fixtures.result_json as result


def test_answer():
    assert generate_diff('file1.json', 'file2.json') == result.FLAT_JSON
