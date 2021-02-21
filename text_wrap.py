def wrap(string, max_width):
    dummy_string = ""
    for _ in string:
        dummy_string = dummy_string + string[0:max_width] + "\n"
        string = string[max_width:]

    return dummy_string


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
