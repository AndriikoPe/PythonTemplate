import os
from app.io.input import read_text_from_file, read_text_from_pandas
import pandas as pd


# Test reading from a file that exists
def test_read_existing_file(tmpdir):
    file = tmpdir.join("test_file.txt")
    expected_content = "Hello, world!"
    file.write(expected_content)

    assert read_text_from_file(str(file)) == expected_content


# Test reading from a non-existent file
def test_read_nonexistent_file():
    non_existent_file = "this_file_does_not_exist.txt"
    assert read_text_from_file(non_existent_file) is None


# Test for reading permission
def test_read_file_permission_error(tmpdir):
    file = tmpdir.join("test_file.txt")
    file.write("Some content")
    file_path = str(file)
    os.chmod(file_path, 0o000)

    assert read_text_from_file(file_path) is None


# Test reading from an empty CSV file
def test_read_empty_csv_file(tmpdir):
    df = pd.DataFrame(columns=['col1', 'col2'])
    file_path = os.path.join(tmpdir, 'empty.csv')
    df.to_csv(file_path, index=False)

    result = read_text_from_pandas(file_path)
    expected_content = df.to_string()
    assert result == expected_content


# Test reading from a non-existent CSV file
def test_read_nonexistent_csv_file():
    non_existent_file = "nonexistent_file.csv"
    assert read_text_from_pandas(non_existent_file) is None


# Test reading from a CSV file with multiple columns
def test_read_csv_multiple_columns(tmpdir):
    df = pd.DataFrame({'col1': ['Hello, world!'], 'col2': ['Another column']})
    file_path = os.path.join(tmpdir, 'multi_column.csv')
    df.to_csv(file_path, index=False)

    result = read_text_from_pandas(file_path)
    expected_content = "col1           col2\nHello, world! Another column"
    assert result.strip() == expected_content.strip()
