from gendiff.gendiff import generate_diff


def test_gendiff_json():    
    data1 = 'gendiff/files/file1.json'
    data2 = 'gendiff/files/file2.json'
    assert generate_diff(data1, data2) == open('tests/fixtures/stylish_flat_files.txt', 'r').read()
