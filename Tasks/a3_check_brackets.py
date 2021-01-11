def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    brackets_row = list (brackets_row)
    a = ')'
    b = '('
    check = True
    if len(brackets_row) % 2:
        check = False
    else:
        while len (brackets_row) and check:
            if brackets_row[0] == b and brackets_row[1] == a:
                brackets_row.pop(0)
                brackets_row.pop(0)
            elif brackets_row[-1] == a and brackets_row[-2] == b:
                brackets_row.pop(-1)
                brackets_row.pop(-1)
            elif brackets_row[0] == b and brackets_row[-1] == a:
                brackets_row.pop(0)
                brackets_row.pop(-1)

            else:
                check = False
    return check

