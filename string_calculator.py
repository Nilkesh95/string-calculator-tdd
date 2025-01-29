import re

def add(numbers):
    if not numbers:
        return 0
    
    delimiter=",|\n"
    if numbers.startswith("//"):
        parts=numbers.split("\n",1)
        delimiter=re.escape(parts[0][2:])
        numbers=parts[1]

    num_list=list(map(int, re.split(delimiter,numbers)))
    negatives=[i for i in num_list if i<0]
    if negatives:
        raise ValueError(f"negatives not allowed: {','.join(map(str,negatives))}")

    return sum(i for i in num_list if i<=1000)