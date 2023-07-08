from formatters import plain, bold, italic, header, inline_code, link, new_line, ordered_list, unordered_list


FORMATTERS = {
        'plain': plain,
        'bold': bold,
        'italic': italic,
        'header': header,
        'inline-code': inline_code,
        'link': link,
        'new-line': new_line,
        'ordered-list': ordered_list,
        'unordered-list': unordered_list,
    }


def write_text_to_file(text: str) -> str:
    """Write the formatted text to a file"""
    with open('./output.md', 'w') as file:
        file.write(text)
        return file.name


def formatting_prompt():
    """Handle command prompt logic"""
    formatted_text = ""

    while True:
        answer = input("Choose a formatter: ")
        if answer == "!help":
            print(
                "Available formatters: plain bold italic header link ordered-list unordered-list inline-code new-line")
            print("Special commands: !help !done")
        elif answer == "!done":
            write_text_to_file(formatted_text)
            break
        elif answer not in FORMATTERS:
            print('Unknown formatting type or command')
        else:
            formatter_func = FORMATTERS[answer]
            formatted_text += formatter_func()

        print(formatted_text)


def main() -> None:
    formatting_prompt()


if __name__ == "__main__":
    main()
