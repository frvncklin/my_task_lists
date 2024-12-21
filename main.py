import list_content_manipulation as lcm
import json_file_manipulation as jfm
import main_menu as mm
import os
import sys
import time

# Defining variables for code influx manipulation.

main_menu = False
new_list_request = False

# Defining function to execute the user's requests.
def actions(choice):
    """Executes the action chosen by the user in the main menu.

    Args:
        choice (int): The number of the option chosen by the user.
    """
    global main_menu
    global new_list_request
    match choice:
        case 1: # list tasks
            os.system('cls')
            lcm.list_tasks(list_name, list_content)
            user_input = input("\npress enter to continue.")
            os.system('cls')
        case 2: # add task
            os.system('cls')
            lcm.add_task(list_content, list_cache)
            os.system("cls")
            print("task(s) added!")
            time.sleep(2)
            os.system("cls")
        case 3: # clear/delete task
            os.system('cls')
            lcm.conclude_or_delete_task(list_content, list_cache)
            os.system("cls")
            print("task(s) cleared!")
            time.sleep(2)
            os.system("cls")
        case 4: # undo/redo operation
            os.system('cls')
            lcm.undo_and_redo_action(list_content, list_cache)
            time.sleep(2)
            os.system('cls')
        case 5: # select another list
            os.system('cls')
            main_menu = False
        case 6: # create new list
            os.system('cls')
            print("Let's create a new list!")
            time.sleep(2)
            main_menu = False   # Exits main menu.
            new_list_request = True # Enables new list creation.
            os.system('cls')
        case 7: # save as txt file
            lcm.save_as_txt(list_name, list_content)
            os.system('cls')
            print("list saved as '.txt' in this directory!")
            time.sleep(2)
            os.system('cls')
        case 8: #exit
            os.system('cls')
            print('exiting..... thank you!')
            time.sleep(2)
            os.system('cls')
            sys.exit()

# Program started
print(f"{"mytasklists".center(len("Welcome to your lists!"))}")
print("Welcome to your lists!")
time.sleep(1.5)
os.system('cls')

# checking if it's the first time that the user uses the program
# If so: create a new JSON file and upload a new and empty task list into it.
if jfm.first_use:
    jfm.create_new_task_list()

# This is the layer outside the main menu, where the user goes to create and load a new list.
while True:

    # if the user, on the main menu, decides to create a new list, he'll go here and create it.
    if new_list_request:
        jfm.create_new_task_list()
    
    # Selecting the task list we'll be working on and collecting it's data for manipulation.
    list_key, list_content, list_cache, list_name = jfm.collect_data()
    list_data = [list_key, list_content, list_cache, list_name]

    main_menu = True

    # This is the main menu, where the user can manipulate the content of the selected list
    # as he wishes.
    while main_menu:

        # Displaying the main menu.
        mm.show_main_menu(list_name)
        # Capturing the user's choice and executing it.
        choice = input(">>> ")
        actions(int(choice))

        # After executing any action, the progarm clears a part of the cache and updates the JSON file.
        lcm.clear_cache(list_cache)
        jfm.update_file(list_key, list_name, list_content, list_cache)
        first_run = False