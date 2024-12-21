
menu_options = {
    1: "list tasks",
    2: "add task",
    3: "conclude/delete task",
    4: "undo/redo last action",
    5: "select another list",
    6: "create new list",
    7: "save as txt",
    8: "exit"
}

def show_main_menu(list_name):

    # Defining some basic layout for the menu, based on the lenght of the strings
    selected_list_message = f"selected list: {list_name}\n"
    max_len = 0
    for (key, value) in menu_options.items():
        current_len = len(f'{key} -> {value}')
        max_len = current_len if current_len > max_len else max_len
    max_len = len(selected_list_message) if max_len < len(selected_list_message) else max_len
    
    # Printing main menu
    print("-" * max_len, "\n", sep='')
    print(f"{"main menu".center(max_len)}", end="\n\n")
    print(selected_list_message)
    for (key, value) in menu_options.items():
        print(f"{key} -> {value}")
    print("\n", "-" * max_len, sep='')



