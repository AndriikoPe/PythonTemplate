import pytest
from app.io.input import read_text_from_file
import os


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
