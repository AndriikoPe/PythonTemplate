import app.io.input as app_input
import app.io.output as app_output


def main():
    console_text = app_input.get_text_from_console()
    file_text_simple = app_input.read_text_from_file("data/input_plain_text.txt")
    file_text_pandas = app_input.read_text_from_pandas("data/input_csv.csv")

    app_output.write_text_to_console("User text:\n" + console_text + "\n")
    app_output.write_text_to_console("Text read from using python built-in funcs:\n" + file_text_simple + "\n")
    app_output.write_text_to_console("Text read from using pandas:\n" + file_text_pandas + "\n")

    app_output.write_text_to_file("data/output_file_user_text.txt", console_text)
    app_output.write_text_to_file("data/output_file_simple.txt", file_text_simple)
    app_output.write_text_to_file("data/output_file_pandas.txt", file_text_pandas)


if __name__ == "__main__":
    main()
