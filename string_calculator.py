import re

def add(numbers):
    if not numbers:
        return 0
    
    delimiter=",|\n"
    if numbers.startswith("//"):
        parts=numbers.split("\n",1)
        delimiter=re.escape(parts[0][2:])
        numbers=parts[1]

    return sum(map(int, re.split(delimiter,numbers)))