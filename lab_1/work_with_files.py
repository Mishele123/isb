import json




def read_json(path: str) -> dict:
    """reading data from json file
    parametres:
        path: the path to the file where the text is located"""

    try:
        with open(path, "r", encoding="utf-8") as file:
            s = json.load(file)
        return s
    except FileNotFoundError:
        print("File not found")
    except Exception as ex:
        print(f"error with reading file {str(ex)}")


def read_file(path: str) -> str:
    """"this function read text from path file
    parametres:
        path: the path to the file where the text is located"""

    try:
        with open(path, "r", encoding="utf-8") as file:
            s = file.read()
        return s
    except FileNotFoundError:
        print("File not found")
    except Exception as ex:
        print(f"error with reading file {str(ex)}")


def write_file(path: str, data: str) -> None:
    """write data str in path file
    parametres:
        path: the path to the file where the text should be written
        data: text for writting
    """

    try:
        with open(path, "w", encoding="utf-8") as file:
            file.write(data)

    except Exception as ex:
        print(f"error with writing file {str(ex)}")


def write_json(path: str, data: dict) -> None:
    """write data dict in path json file
    parametres:
        path: the path to the json file where the text should be written
        data: dict for writing"""

    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii = False, indent = 1)
            print("Data written in file")
    except Exception as ex:
        print(f"error with writing file {str(ex)}")