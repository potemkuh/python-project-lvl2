import pytest
import gendiff
import yaml


def test_gendiff_json():    
    data1 = yaml.safe_load(open('gendiff/files/file1.json', 'r'))
    data2 = yaml.safe_load(open('gendiff/files/file2.json', 'r'))
    assert gendiff.generate_diff(data1, data2) == open('tests/fixtures/test_yml.txt', 'r').read()