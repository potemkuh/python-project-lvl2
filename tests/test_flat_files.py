from gendiff.gendiff import generate_diff
import pytest


test_cases = ['yml', 'json']

@pytest.mark.parametrize('test_format', test_cases)
def test_gendiff_json(test_format):
    data1 = f'tests/fixtures/flat_files1.{test_format}'
    data2 = f'tests/fixtures/flat_files2.{test_format}'
    assert generate_diff(data1, data2) == open('tests/fixtures/stylish_flat_files.txt', 'r').read()
