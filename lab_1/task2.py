

from work_with_files import *


def frequency_analysis(path_file: str, path_json: str) -> None:
    """Performs a frequency analysis of the text and writes it to the dictionary in another file"""
    text = read_file(path_file)
    frequencies = {}
    count_chars = len(text)

    for sym in text:
        if sym in frequencies:
            frequencies[sym] += 1
        else:
            frequencies[sym] = 1
    
    for sym, count in frequencies.items():
        frequencies[sym] = count / count_chars
    sorted_freq = dict(sorted(frequencies.items(), key=lambda x: x[1], reverse=True))
    write_json(path_json, sorted_freq)



frequency_analysis("D:\\allLabs\\isb\\lab_1\\zadanie2\\text2.txt", "D:\\allLabs\\isb\lab_1\\zadanie2\\letter_frequency.json")