import gendiff


def test_gendiff_json():    
    data1 = 'gendiff/files/file1.json'
    data2 = 'gendiff/files/file2.json'
    assert gendiff.generate_diff(data1, data2) == open('tests/fixtures/stylish_flat_files.txt', 'r').read()
