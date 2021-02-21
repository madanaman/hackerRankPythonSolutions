"""
reverse: Reverse the list."""


def insert_list(lst, i, e):
    # print("inside insert: inserting", e, "at position", i, "current list len", len(lst))
    if i >= len(lst):
        lst.append(e)
        new_list = lst
        # print("inside appending at end of the list")
    else:
        new_list = lst[0:i] + [e] + lst[i:len(lst)]
    # print("returning ", new_list)
    return new_list


def print_list(lst):
    print(lst)


def move_elems(lst, start_pos):
    for x in range(start_pos, len(lst)):
        if x == len(lst) - 1:
            lst[x] = ""
        else:
            lst[x] = lst[x + 1]
    return lst


def remove_lst(lst, e):
    # print("from remove list", lst)
    result = []
    for idx in range(0, len(lst)):
        if lst[idx] == e:
            # print("element found")
            result = lst[0:idx]+lst[idx+1:len(lst)]
            # print("printing modified result")
            break
    # print("returning ", result)
    return result

def append_list(lst, elem):
    # print("inside append", lst)
    if len(lst) > 0:
        # print("inside > 0")
        lst.append(elem)
        new_list = lst
        # print(new_list)
    else:
        new_list = [elem]
    # print("returning ", new_list)
    return new_list


def sort_list(lst):
    # print("returning", sorted(lst))
    return sorted(lst)


def pop_list(lst):
    lst.pop()
    return lst


def reverse_list(lst):
    return lst[::-1]


if __name__ == '__main__':
    final_list = []
    N = int(input())
    for i in range(N):
        command = input().split()
        if command[0] == 'insert':
            final_list = insert_list(final_list, int(command[1]), int(command[2]))
        elif command[0] == 'print':
            print_list(final_list)
        elif command[0] == 'append':
            final_list = append_list(final_list, int(command[1]))
        elif command[0] == 'sort':
            final_list = sort_list(final_list)
        elif command[0] == 'pop':
            final_list = pop_list(final_list)
        elif command[0] == 'reverse':
            final_list = reverse_list(final_list)
        elif command[0] == 'remove':
            final_list = remove_lst(final_list, int(command[1]))
