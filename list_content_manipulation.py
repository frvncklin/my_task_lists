import os
import json
import sys
from useful_functions import string_splitter

def list_tasks(list_name, list_content):
    """Prints all the items present in the task list content, enumerating them for the user.

    Args:
        list_content (list): The variable containing the contents of the task list we're 
        working on.
    """
    print(list_name, end='\n\n')
    for index, value in enumerate( list_content):
        print(f'{index + 1} -> {value}')

def add_task(list_content, cache):
    """This function adds a new task to our task list according to the users input.
    It can be more than just one.
    If the user wants to add more than one new task, he can do so by typing the tasks
    in succession, and separating them with a comma (',').
    Ex: user_input = 'do the homework, do the dishes, spend time with dog'
    Will appear in the task list as following:
    (..., 'do the homework', 'do the dishes', 'spend time with dog')

    Also, these actions are registered in the cache as the following:
    ('add', added items)

    Args:
        list_content (list): The variable containing the contents of the task list we're 
        working on.
    """
    task = input('please insert your new task\n(you can put more than one task, just separate it with ","\nex: (do homework, do the dishes, finish my favorite anime)):\n\n>>> ')

    # We treat the user's entry with the 'string splitter'. This function treats the string
    # so that, if it has a comma (","), applies the string method 'split' in it,
    # turning it into a list, which serves our purposes.
    task = string_splitter(task)
    if isinstance(task, list):
        added_tasks = []
        for item in task:
            list_content.append(item.lower())
            added_tasks.append(item.lower())
        cache.append('add')
        cache.append(added_tasks)
    else:
        list_content.append(task.lower())
        cache.append('add')
        cache.append(task.lower())

def conclude_or_delete_task(list_content, list_cache):
    """This function erase a task from our task lists contents.
    It can be just one or many.
    First, the user is shown the task list items like this:
    1 ->  do the homwork
    2 -> do the dishes
    3 -> spend time with dog

    Then, we ask the user to select the number of the tasks they want to delete.
    If the user wants to erase more than one item from our task list,
    he can do so by typing the numbers in succesion, separated by a comma (','),
    ex: user_input = '1, 2, 3' -> Erases the tasks 1, 2 and 3.

    Args:
        list_content (list): the variable containing the contents of our task list.
        list_cache (list): the variable ccontaining the contents of our cache.
    """

    # Exibiting the list of tasks so that the user can choose which one he'll delete.
    # Some of the code is done to position the words perfectally in the center.
    lines = []
    max_len = 0
    for task_number, task in enumerate(list_content):
        line = f'{task_number + 1} -> {task}'
        max_len = len(line) if len(line) > max_len else max_len
        lines.append(line)
    print(f"{"conclude/delete tasks".center(max_len)}\n")
    for line in lines:
        print(line)
    chosen_task_number = input("\nplease, select the task that you want to dele from this list:\n(if you want to delete more than one, just put a ',')\n(ex: (1, 4, 6))\n>>> ")
    
    # Treating the user's entry.
    chosen_task_number = string_splitter(chosen_task_number)

    # Deleting the corresponding items and adding the deleted ones to the cache.
    list_cache.append('del')
    deleted_items = [list_content[i - 1] for i in chosen_task_number]
    del_cache = [(list_content.index(item), item) for item in deleted_items]
    list_cache.append(del_cache)
    new_list_content = [item for item in list_content if item not in deleted_items]
    list_content = new_list_content


def undo_and_redo_action(list_content, cache):
    """This function neutralizes the last action done by the user using the cache's data to
    identify it.

    Args:
        list_content (list): The variable containing the list's contents.
        cache (list): The variable containing the cache's contents.
    """

    # First, we must check what was the type of the last action, as it's collected in the cache.

    # cache = ['add' or 'del', items]
    add_action = cache[0] == 'add'
    delete_action = cache[0] == 'del'

    cache_content = cache[1]

    # If it was an add action, then the added items will be deleted.
    if add_action:
        if isinstance(cache_content, list):
            deleted_items = []
            for cache_item in cache_content:
                deleted_element_index = list_content.index(cache_item)
                deleted_element = list_content.pop(deleted_element_index)
                deleted_items.append((deleted_element_index, deleted_element))
            cache.append('del')
            cache.append(deleted_items)
        else:
            deleted_element = list_content.pop()
            cache.append('del')
            cache.append(deleted_element)
        print("tasks deleted!")

    # If it was a delete action, then the deleted items must be restored.
    if delete_action:
        if isinstance(cache_content, list):
            added_items = []
            for [index, item] in cache_content:
                list_content.insert(index, item)
                added_items.append(item)
            cache.append('add')
            cache.append(added_items)
        else:
            list_content.append(cache_content[1])
            cache.append('add')
            cache.append(cache_content)
        print("tasks readded!")

def clear_cache(cache):
    """This function clears our task list's cache, only allowing for the cache to have
    information about the last action executed.
    ex: ('add', [1, 2, 3])

    The cache must not retain the information beyond the last task executed, therefore
    it cannot be like this:
    ('add', [1, 2, 3], 'del', [2])

    So, with this function applied, the cache will be as the following:
    ('del', [2]).

    This allows for the cache to be used in the 'redo_action' and 'undo_action' functions.

    Args:
        cache (list): Our task list cache's contents.
    """
    if len(cache) == 4:
        cache.pop(0)
        cache.pop(0)

def save_as_txt(list_name, list_content):
    """This function creates a new txt file and writes our task list's 
    name and content inside it.

    Args:
        list_name (_type_): The name of the task list. 
        list_content (_type_): The contents of the task list.
    """
    with open (f'{list_name}_mytasklists.txt', 'w') as file:
        file.write(f"{list_name}:\n\n")
        for index, item in enumerate(list_content):
            file.write(f"{index + 1}-> {item}\n")
        file.write("made with love throught mytasklists!")
        