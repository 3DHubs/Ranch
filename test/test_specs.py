from unittest.mock import patch
from ranch import specs


@patch('ranch.specs._get_export_dirs', new=lambda: ['foodir', 'bardir'])
@patch('ranch.specs.os.listdir', new=lambda _: ['foo', 'bar'])
@patch('ranch.specs.os.path.isdir', new=lambda d: d == 'bar')
def test_no_specs_error():
    e = specs.NoSpecsFileError()
    assert 'foodir' in e.searched_dirs.keys()
    assert 'bardir' in e.searched_dirs.keys()

    assert 'foo' in e.searched_dirs['foodir']
    assert 'bar' in e.searched_dirs['foodir']

    s = str(e)
    assert 'foodir/' in s
    assert 'foo' in s
    assert 'bar/' in s
