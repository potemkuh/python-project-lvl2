import gendiff
import json


def test_gendiff_stylish():    
    data1 = json.load(open('gendiff/files/file3.json', 'r'))
    data2 = json.load(open('gendiff/files/file4.json', 'r'))
    assert gendiff.generate_diff(data1, data2) == open('tests/test_recursive .py', 'r').read()

def test_gendiff_plain():    
    data1 = json.load(open('gendiff/files/file3.json', 'r'))
    data2 = json.load(open('gendiff/files/file4.json', 'r'))
    assert gendiff.generate_diff(data1, data2) == open('tests/fixtures/plain_flat.txt', 'r').read()

def test_gendiff_json():    
    data1 = json.load(open('gendiff/files/file3.json', 'r'))
    data2 = json.load(open('gendiff/files/file4.json', 'r'))
    assert gendiff.generate_diff(data1, data2) == open('tests/fixtures/json.txt', 'r').read()