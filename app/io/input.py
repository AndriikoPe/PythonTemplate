import pandas as pd

def get_text_from_console():
    """Prompts the user for text input from the console and returns it.

    This function retrieves text entered by the user through the console.
    """

    return input("Enter text: ")  # Get user input using input()

def read_text_from_file(filename):
    """Reads text content from a file and returns it as a string.

    This function takes a filename as input and attempts to read its content.
    It uses Python's built-in capabilities for file operations.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        str: The text content of the file, or None if an error occurs.
    """

    try:
        with open(filename, 'r') as file:  # Open file in read mode
            text = file.read()  # Read entire file content
        return text
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:  # Catch other potential exceptions
        print(f"Error reading file '{filename}': {e}")
        return None

def read_text_from_pandas(filename):
    """Reads text content from a file using pandas and returns it as a string.

    This function takes a filename as input and attempts to read its content
    using the pandas library.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        str: The text content of the file (assuming it's a single column), or None if an error occurs.
    """

    try:
        # Assuming pandas is installed, read the first column as text
        text = pd.read_csv(filename, header=None, squeeze=True)
        return text.to_string(index=False)  # Remove index from output string
    except ModuleNotFoundError:
        print("Error: pandas library not installed. Please install pandas to use this function.")
        return None
    except Exception as e:
        print(f"Error reading file '{filename}' with pandas: {e}")
        return None
