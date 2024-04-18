import json
import argparse
import math

from typing import Tuple


def work_with_json_file(path: str) -> Tuple[str, str, str]:
    """Function get c++ \ java secuences \ path to result file from json file
    parameters:
    path: path to json file
    return: (cpp_row, java_row, path_to_result)"""
    try:
        with open(path, "r", encoding="utf-8") as file:
            json_data = json.load(file)
            return (json_data["c++"], json_data["java"], json_data["path_to_result_file"])
    except Exception as ex:
        print(f"Error with file: {str(ex)}")


def frequency_bit_test(bits_sequence: str) -> float:
    """Frequence bit test
    PARAMETERS:
    bits_sequence - secuence to be processed
    return:
    The value of the P value
    """
    try:
        N = len(bits_sequence)
        S = 0
        for i in bits_sequence:
            if i == "1":
                x = 1
            else:
                x = -1
            S += 1 / math.sqrt(N) * x
        P = math.erfc(S / math.sqrt(2))
        return P
    except Exception as ex:
        print(f"Error : {str(ex)}")


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description="Parse Arguments")
        parser.add_argument("random_bits_json", help="Path to the json file")
        args = parser.parse_args()
        print(args.random_bits_json)
        cpp_row, java_row, path_ro_res_file = work_with_json_file(args.random_bits_json)
        print(cpp_row)
        print(frequency_bit_test(cpp_row))
    except Exception as ex:
        print(f"Error: {str(ex)}")