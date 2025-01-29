import re

def add(numbers):
    if not numbers:
        return 0
    
    delimiter=",|\n"  #Default delimiters: comma and newline

    #Check for custom delimiter format
    if numbers.startswith("//"):
        match=re.match(r"//(\[.*\])\n(.*)", numbers)
        if match:
            #Extract multi-character delimiters
            delimiter="|".join(re.escape(d[1:-1]) for d in match.group(1).split("]["))
            numbers=match.group(2)
        else:
            parts=numbers.split("\n", 1)
            delimiter=re.escape(parts[0][2:])
            numbers=parts[1]

    #Convert numbers to a list of integers
    num_list=list(map(int, re.split(delimiter,numbers)))

    #Handle negative numbers
    negatives = [i for i in num_list if i<0]
    if negatives:
        raise ValueError(f"negatives not allowed: {','.join(map(str,negatives))}")

    #Ignore numbers greater than 1000
    return sum(i for i in num_list if i<=1000)