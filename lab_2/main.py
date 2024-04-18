import json
import argparse
import math
import re
import scipy

from typing import Tuple


PI = [0.2148, 0.3672, 0.2305, 0.1875]


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


def test_same_bits(bits_sequence: str) -> float:
    """Same bit test
    PARAMETERS:
    bits_sequence - secuence to be processed
    return:
    The value of the P value
    """
    try:
        N = len(bits_sequence)
        count_1 = bits_sequence.count("1")
        C = (1 / N) * count_1
        V = 0
        if abs(C - 1 / 2) < (2 / math.sqrt(N)):
            V = 0
            for i in range(0, N - 1):
                if (bits_sequence[i] != bits_sequence[i + 1]):
                    V += 1

            P = math.erfc((abs(V - 2 * N * C * (1 - C))) / (2 * math.sqrt(2 * N) * C * (1 - C)))  
            return P
        else:
            P = 0
        return P
    except Exception as ex:
        print(f"Error : {str(ex)}")


def units_test(bits_sequence: str) -> float:
    """checking the long sequence of 1 in a block
    PARAMETERS:
    bits_sequence - secuence to be processed
    return:
    The value of the P value
    """
    try:
        divided_bits_sequence = re.findall(r'.{%s}' % 8, bits_sequence)
        v1 = v2 = v3 = v4 = 0
        for sec in divided_bits_sequence:
            count = 0
            max_count = 0
            for i in sec:
                if i == "1":
                    count += 1
                else:
                    count = 0
                max_count = max(count, max_count)
            match max_count:
                case 0:
                    v1 += 1
                case 1:
                    v1 += 1
                case 2:
                    v2 += 1
                case 3:
                    v3 += 1
                case _:
                    v4 += 1
        v = [v1, v2, v3, v4]
        x_square = 0
        for i in range(4):
            x_square += (pow(v[i] - 16 * PI[i], 2)) / (16 * PI[i])
        P = scipy.special.gammainc(3 / 2,  x_square / 2)
        return P
    except Exception as ex:
        print(f"Error : {str(ex)}")


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description="Parse Arguments")
        parser.add_argument("random_bits_json", help="Path to the json file")
        args = parser.parse_args()
        cpp_row, java_row, path_to_res_file = work_with_json_file(args.random_bits_json)
        with open(path_to_res_file, "w", encoding = "utf-8") as results:
            results.write("NIST TEST RESULTS:\n")
            results.write("for c++:\n")
            results.write(f"Frequency bit test = {frequency_bit_test(cpp_row)}\n")
            results.write(f"Identical bits test = {test_same_bits(cpp_row)}\n")
            results.write(f"Sequence of units test = {units_test(cpp_row)}\n")
            results.write("for java:\n")
            results.write(f"Frequency bit test = {frequency_bit_test(java_row)}\n")
            results.write(f"Identical bits test = {test_same_bits(java_row)}\n")
            results.write(f"Sequence of units test = {units_test(java_row)}\n")
        
    except Exception as ex:
        print(f"Error: {str(ex)}")