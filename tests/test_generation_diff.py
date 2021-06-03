import pytest
import gendiff
import json


def test_gendiff_json():    
    #assert gendiff.generate_diff('gendiff/file1.json', 'gendiff/file2.json') == open.read('tests/fixtures/test_json.txt', 'r')
    f1 = json.load(open('gendiff/files/file1.json', 'r'))
    f2 = json.load(open('gendiff/files/file2.json', 'r'))
    assert gendiff.generate_diff(f1, f2) == open('tests/fixtures/test_json.txt', 'r').read()