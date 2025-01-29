import re

def add(numbers):
    if not numbers:
        return 0

    delimiter=",|\n"  #Default delimiters: comma and newline

    #Check for custom delimiters in the format "//[delim1][delim2]\n..."
    if numbers.startswith("//"):
        match=re.match(r"//(\[.*\])\n(.*)", numbers)
        if match:
            #Extract multiple delimiters from format "//[delim1][delim2]\n..."
            delimiter="|".join(re.escape(d[1:-1]) for d in re.findall(r"\[([^\]]+)\]", match.group(1)))
            numbers=match.group(2)  # Extract actual numbers after the delimiter declaration
        else:
            #Handle case of single-character custom delimiter "//;\n1;2;3"
            parts=numbers.split("\n",1)
            delimiter=re.escape(parts[0][2:])
            numbers=parts[1]

    #Split numbers using delimiters and filter out empty strings
    num_list=[int(i) for i in re.split(delimiter, numbers) if i.strip().isdigit()]

    #Handle negative numbers
    negatives=[i for i in num_list if i<0]
    if negatives:
        raise ValueError(f"negatives not allowed: {','.join(map(str, negatives))}")

    #Ignore numbers greater than 1000
    return sum(i for i in num_list if i<=1000)