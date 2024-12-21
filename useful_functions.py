def string_splitter(string):
    if "," in string:
        string = string.split(",")
        for i in range(len(string)):
            string[i] = string[i].strip()
        return string
    return string