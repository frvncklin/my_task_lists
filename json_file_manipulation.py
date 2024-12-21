import os
import sys
import json

FILE_PATH = 'mytasklists.json'

first_use = not os.path.exists(FILE_PATH)

def create_new_task_list():
    """
    Creates a new task list and uploads it to the JSON file as following:
    'listx': {'name': 'list name', 'content': [list items], 'cache': [list cache]}

    If it's the first time the user is executing the program, it'll create a new JSON file with.
    A new task list that has a name, chosen by the user, and and empty lists in 'content' and
    'cache'.
    """

    name = input("Please insert a name for our new task list!:\n>>> ")

    if first_use:

        new_list = {
            'list1': {'name': name, 'content': [], 'cache': []}
        }
        with open(FILE_PATH, 'w', encoding='utf8') as file:
            json.dump(new_list, file, indent=2)
    else:
        with open(FILE_PATH, 'r') as file:
            my_task_lists = json.load(file)
        my_task_lists.update({f'list{len(my_task_lists) + 1}': {'name': name, 'content': [], 'cache': []}})
        with open(FILE_PATH, 'w', encoding='utf8') as file:
            json.dump(my_task_lists, file)
    


def collect_data():
    """
    Asks the user to choose a task list within our JSON file and retrieves it's data.

    Returns:
        str: the list's key in the JSON file (ex: 'list1', 'list2')
        list: the list's content.
        list: the list's cache.
        str: the list's name.
    """

    # checks if the user's not executing this program for the first time
    # then asks the user which task list they'll want to manipulate and them retrieves it's 
    # content from the JSON file.
    if not first_use:
        # Opening the file to collect the JSON file data.
        with open(FILE_PATH, 'r') as file:
            my_task_lists = json.load(file)
            my_task_lists_names = [my_task_lists[key]['name'] for key in my_task_lists.keys()]
        
        print("Please select the list you'll work with:\n")

        for index, value in enumerate(my_task_lists_names):
            print(f"{index + 1} -> {value}")

        # Capturing the user's choice and treating it.
        user_choice = input("\n>>> ")
        valid_option = user_choice.isdigit() and 0 < int(user_choice) <= len(my_task_lists)

        if not valid_option:
            os.system('cls')
            print("You've typed an invalid option, please restart the program!")
            sys.exit()
        
        # retrieving the task list.
        selected_list = my_task_lists[f'list{user_choice}']
        selected_list_key = f'list{user_choice}'
    
        os.system('cls')

        # retrieving the task list's content.
        return selected_list_key, selected_list['content'], selected_list['cache'], selected_list['name']
        # Returns, respectively: list key, list content, list cache, list name
    
    else:
        with open(FILE_PATH, 'r') as file:
            my_task_lists = json.load(file)

        os.system('cls')
        return 'list1', my_task_lists['list1']['content'], my_task_lists['list1']['cache'], my_task_lists['list1']['name']
    
def update_file(key, name, content, cache):
    """
    Collects the data from the task list the user was manipulating and updates it's content
    on our JSON file, so it'll will be saved next time we open it.

    Args:
        key (str): The task list's key in the JSON file.
        name (str): The task list's name.
        content (list): The task list's content.
        cache (list): The task list's cache.
    """
    # Collecting the JSON and updating it.
    with open(FILE_PATH, 'r') as file:
        my_task_lists = json.load(file)
        my_task_lists[key] = {'name': name, 'content': content, 'cache': cache}
    # Dumping the JSON back into the file, updated.
    with open(FILE_PATH, 'w', encoding='utf8') as file:
        json.dump(my_task_lists, file, indent=2)