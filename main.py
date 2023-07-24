# This is the main program for the AgriVoltaics Project
# Author: Rohan Arun
# Date: 2023/07/23

# Description
#
import math

from scipy.stats import norm
import random


DISCOUNT = 0.03
DRIFT = 0.01
VOLATILITY = 0.05
INIT_VAL = 100

NUM_MONTHS = 12.0

def generate_value(input_val, month):
    #1st parameter
    val_1 = (DRIFT - (VOLATILITY**2)/2.0) * month / NUM_MONTHS

    #2nd parameter
    rand_val = random.random()
    norm_inv = norm.ppf(rand_val, 0, math.sqrt(month / NUM_MONTHS))
    val_2 =- VOLATILITY * norm_inv

    val = input_val * math.exp(val_1 + val_2)

    return (val)



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Discount {DISCOUNT}')  # Press ⌘F8 to toggle the breakpoint


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(generate_value(input_val=100, month=1))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
