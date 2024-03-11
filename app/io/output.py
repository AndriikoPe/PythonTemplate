def write_text_to_console(text):
    """
    Prints the specified text to the console.

    :param text: The text to print.
    :type text: str
    """
    print(text)


def write_text_to_file(filename, text):
    """
    Writes the specified text content to a file.

    This function uses Python's built-in file writing capabilities to save text to the specified file. If the file does
    not exist, it will be created. If the file does exist, its content will be overwritten with the specified text.

    :param filename: The name of the file where the text will be written.
    :type filename: str
    :param text: The text content to write to the file.
    :type text: str
    """
    with open(filename, 'w') as file:
        file.write(text)
