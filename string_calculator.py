import re

def add(numbers):
    if not numbers:
        return 0
    return sum(map(int, re.split(",|\n",numbers)))