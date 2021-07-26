import gendiff
import json


def test_gendiff_json():    
    data1 = json.load(open('gendiff/files/file1.json', 'r'))
    data2 = json.load(open('gendiff/files/file2.json', 'r'))
    assert gendiff.generate_diff(data1, data2) == open('tests/fixtures/stylish_flat_files.txt', 'r').read()
