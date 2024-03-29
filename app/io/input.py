import pandas as pd


def get_text_from_console():
    """
    Prompts the user for text input from the console and returns it.

    :return: Text entered by the user through the console.
    :rtype: str
    """
    return input("Enter text: ")


def read_text_from_file(filename):
    """
    Reads text content from a file and returns it as a string.

    :param filename: The name of the file to read from.
    :type filename: str
    :return: The text content of the file, or None if an error occurs.
    :rtype: str or None
    """
    try:
        with open(filename, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
        return None


def read_text_from_pandas(filename):
    """
    Reads text content from a file using pandas and returns it as a string.

    :param filename: The name of the file to read from.
    :type filename: str
    :return: The text content of the file (assuming it's a single column), or None if an error occurs.
    :rtype: str or None
    """
    try:
        text = pd.read_csv(filename)
        return text.to_string(index=False)
    except ModuleNotFoundError:
        print("Error: pandas library not installed. Please install pandas to use this function.")
        return None
    except Exception as e:
        print(f"Error reading file '{filename}' with pandas: {e}")
        return None
