import json
import argparse
import math
import re
import scipy


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
            if i == 1:
                x = 1
            else:
                x = -1
            S += 1 / math.sqrt(N) * x
        P = math.erfc(s / math.sqrt(2))
        return P
    except Exception as ex:
        print(f"Error : {str(ex)}")