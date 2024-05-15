import os


def read_data_from_file(file_path):
    """ 
    read data from file
    args:
        file_path (str) : path to file
    return:
        data from file(bytes)
    """
    try:
        with open(file_path, "rb") as file:
            return file.read()
    except Exception as ex:
        print(f"Error with file: {ex}")
    

def write_data_in_file(file_path, data):
    """
    Write data in file
    args:
        file_path (str): path to file
        data (bytes): data to write
    """
    try:
        with open(file_path, "wb") as file:
            file.write(data)
    except Exception as ex:
        print(f"Error with file: {ex}")