#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Search and replace all occurrences of an element by
    another in a new list
    my_list: is the initial list
    search: is the element to replace in the list
    replace: is the new element
    You are not allowed to import any module
    """
    return [x if x != search else replace for x in my_list]
