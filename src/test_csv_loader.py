import pytest
from csv_loader import upload_data

def test_read_csv():
    with pytest.raises(UnicodeDecodeError):
        upload_data('sqlite_test_input.xlsx', 'jftdb')

