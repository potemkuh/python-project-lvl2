from gendiff.gendiff import generate_diff


def test_gendiff_stylish():
    data1 = 'gendiff/files/file3.json'
    data2 = 'gendiff/files/file4.json'
    assert generate_diff(data1, data2) == open('tests/fixtures/stylish_recursive.txt', 'r').read()


def test_gendiff_plain():
    data1 = 'gendiff/files/file3.json'
    data2 = 'gendiff/files/file4.json'
    assert generate_diff(data1, data2, format='plain') == open('tests/fixtures/plain_flat.txt', 'r').read()


def test_gendiff_json():
    data1 = 'gendiff/files/file3.json'
    data2 = 'gendiff/files/file4.json'
    assert generate_diff(data1, data2, format='json') == open('tests/fixtures/json.txt', 'r').read()
