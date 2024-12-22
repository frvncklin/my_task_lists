import os
import json
import sys
from useful_functions import treat_user_input

def list_tasks(list_name, list_content):
    """Prints all the items present in the user_input list content, enumerating them for the user.

    Args:
        list_content (list): The variable containing the contents of the user_input list we're 
        working on.
    """
    print(list_name, end='\n\n')
    for index, value in enumerate( list_content):
        print(f'{index + 1} -> {value}')

def add_task(list_content, cache, user_input):
    """This function adds a new user_input to our user_input list according to the users input.
    It can be more than just one.
    If the user wants to add more than one new user_input, he can do so by typing the user_inputs
    in succession, and separating them with a comma (',').
    Ex: user_input = 'do the homework, do the dishes, spend time with dog'
    Will appear in the user_input list as following:
    (..., 'do the homework', 'do the dishes', 'spend time with dog')

    Also, these actions are registered in the cache as the following:
    ('add', added items)

    Args:
        list_content (list): The variable containing the contents of the user_input list we're 
        working on.
    """
    # We treat the user's entry with the 'string splitter'. This function treats the string
    # so that, if it has a comma (","), applies the string method 'split' in it,
    # turning it into a list, which serves our purposes.
    user_input = treat_user_input(user_input)

    added_tasks = [item.lower() for item in user_input]
    list_content.append(added_tasks)
    cache.append('add')
    cache.append(added_tasks)

def conclude_or_delete_task(list_content, list_cache, user_input):
    """This function erase a user_input from our user_input lists contents.
    It can be just one or many.
    The deleted user_input's index and content will be added to the cache like this:
    cache = [('del', (1, deleted_element1), (2, deleted_element2))]
    Args:
        list_content (list): the variable containing the contents of our user_input list.
        list_cache (list): the variable ccontaining the contents of our cache.
        user_entry (str): The variable containing the indexes of the user_inputs which the user wants to
        delete.
    """
    
    # Treating the user's entry.
    user_input = treat_user_input(user_input)

    # Deleting the corresponding items and adding the deleted ones to the cache.
    list_cache.append('del')
    deleted_items = [list_content[i - 1] for i in user_input]
    del_cache = [(list_content.index(item), item) for item in deleted_items]
    list_cache.append(del_cache)
    counter = 0
    for i in user_input:
        list_content.pop((i - 1) - counter)
        counter += 1


def undo_and_redo_action(list_content, cache):
    """This function neutralizes the last action done by the user using the cache's data to
    identify it.

    Args:
        list_content (list): The variable containing the list's contents.
        cache (list): The variable containing the cache's contents.
    """

    # First, we must check what was the type of the last action, as it's collected in the cache.

    add_action = cache[0] == 'add'
    delete_action = cache[0] == 'del'

    cache_content = cache[1]

    # If it was an add action, then the added items will be deleted.
    if add_action:
        indexes = [(index + 1) for (index, item) in enumerate(list_content) if item in cache_content]
        conclude_or_delete_task(list_content, cache, indexes)
        print("task(s) deleted!")
    # If it was a delete action, then the deleted items must be restored.
    elif delete_action:
        added_items = []
        for [index, item] in cache_content:
            list_content.insert(index, item)
            added_items.append(item)
        cache.append('add')
        cache.append(added_items)
        print("task(s) readded!")

            

def clear_cache(cache):
    """This function clears our user_input list's cache, only allowing for the cache to have
    information about the last action executed.
    ex: ('add', [1, 2, 3])

    The cache must not retain the information beyond the last user_input executed, therefore
    it cannot be like this:
    ('add', [1, 2, 3], 'del', [2])

    So, with this function applied, the cache will be as the following:
    ('del', [2]).

    This allows for the cache to be used in the 'redo_action' and 'undo_action' functions.

    Args:
        cache (list): Our user_input list cache's contents.
    """
    if len(cache) == 4:
        cache.pop(0)
        cache.pop(0)

def save_as_txt(list_name, list_content):
    """This function creates a new txt file and writes our user_input list's 
    name and content inside it.

    Args:
        list_name (_type_): The name of the user_input list. 
        list_content (_type_): The contents of the user_input list.
    """
    with open (f'{list_name}.txt', 'w') as file:
        file.write(f"{list_name}:\n\n")
        for index, item in enumerate(list_content):
            file.write(f"{index + 1}-> {item}\n")
        file.write("\nmade with love throught mytasklists!")
        