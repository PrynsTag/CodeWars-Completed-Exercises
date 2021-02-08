def filter_list(_list):
    return [element for element in _list if type(element) is int]


if __name__ == '__main__':
    print(filter_list([1, 2, 'a', 'b']) == [1, 2])
    print(filter_list([1, 'a', 'b', 0, 15]) == [1, 0, 15])
    print(filter_list([1, 2, 'aasf', '1', '123', 123]) == [1, 2, 123])
