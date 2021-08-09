from gendiff.gendiff import generate_diff
import pytest


test_cases = ['yml', 'json']


@pytest.mark.parametrize('test_format', test_cases)
def test_gendiff_stylish(test_format):
    data1 = f'gendiff/files/file_test1.{test_cases}'
    data2 = f'gendiff/files/file_test2.{test_cases}'
    assert generate_diff(data1, data2) == open('tests/fixtures/stylish_recursive.txt', 'r').read()

@pytest.mark.parametrize('test_format', test_cases)
def test_gendiff_plain(test_format):
    data1 = f'gendiff/files/file_test1.{test_cases}'
    data2 = f'gendiff/files/file_test2.{test_cases}'
    assert generate_diff(data1, data2, format='plain') == open('tests/fixtures/plain_flat.txt', 'r').read()

@pytest.mark.parametrize('test_format', test_cases)
def test_gendiff_json(test_format):
    data1 = f'gendiff/files/file_test1.{test_cases}'
    data2 = f'gendiff/files/file_test2.{test_cases}'
    assert generate_diff(data1, data2, format='json') == open('tests/fixtures/json.txt', 'r').read()
