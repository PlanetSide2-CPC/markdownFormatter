import re
import sys


def is_spacing_required(char: str, next_char: str) -> bool:
    score = 0

    for current_char in [char, next_char]:
        if re.search('[\u4e00-\u9FFF]', current_char):
            score += 2
        elif re.search('[0-9A-Za-z]', current_char):
            score += 1
        else:
            return False

    return True if score % 2 == 1 else False


def text_add_spaces(text: str) -> str:
    new_text = ''
    for index in range(len(text) - 1):
        if is_spacing_required(text[index], text[index + 1]):
            new_text += text[index] + ' '
        else:
            new_text += text[index]

    return new_text + text[len(text) - 1]


def has_next(elements):
    return next(elements, 0) != 0


if __name__ == '__main__':
    input_filepath = sys.argv[1]
    output_filepath = sys.argv[2]

    formatted_content: list[str] = []

    with open(input_filepath, 'r', encoding='utf8') as markdown_file:
        content = markdown_file.readlines()

        for line in content:
            formatted_content.append(text_add_spaces(line))

    with open(output_filepath, 'w', encoding='utf8') as markdown_file:
        markdown_file.writelines(formatted_content)
