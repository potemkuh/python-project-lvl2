import pytest
from gendiff import generate_diff

def test_gendiff_json():    
    assert generate_diff('gendiff/file1.json', 'gendiff/file2.json') == open.read('tests/fixtures/test_json.txt', 'r')