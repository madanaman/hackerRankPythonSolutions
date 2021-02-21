#!/bin/python3

import math
import os
import random
import re
import sys
import pytz
from datetime import datetime


# Complete the time_delta function below.
def time_delta(time1, time2):
    diff = datetime.strptime(time1, "%a %d %b %Y %H:%M:%S %z") - datetime.strptime(time2, "%a %d %b %Y %H:%M:%S %z")
    print(abs(diff.total_seconds()))


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()

        delta = time_delta(t1, t2)
