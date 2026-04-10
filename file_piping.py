"""
Read the strings in an input.txt file and output the result into an output.txt file.
"""

def read_input_file(file_path: str):
    """
    Read input file and parse the strings to get the pair of sequences
    parameters:
        file_path (str): a path to the input file
    returns:
        outputs two strings which are the parsed sequences
    """
    s = ""
    t = ""
    f = open(file_path)
    curr_line = f.readline().rstrip('\n')

    s = curr_line
    curr_line = f.readline().rstrip('\n')
    while curr_line.isdigit():
        idx = int(curr_line)+1
        s = s[:idx] + s + s[idx:]
        curr_line = f.readline().rstrip('\n')
    
    t = curr_line
    curr_line = f.readline().rstrip('\n')
    while curr_line.isdigit():
        idx = int(curr_line)+1
        t = t[:idx] + t + t[idx:]
        curr_line = f.readline().rstrip('\n')
    
    f.close()
    return s, t

def write_output_file(file_path: str, output: str):
    """
    Create a new file and write the output. If file already exists, return error.
    parameters:
        file_path (str): a path to the output file
        output (str): the output of either the basic or efficient sequence alignment algorithm
    """
    f = open(file_path, "x")
    for line in output:
        f.write(line + "\n")
    f.close()

if __name__ == "__main__":
    # Unit tests to check that code works
    s, t = read_input_file("input.txt")
    print(s == 'ACACTGACTACTGACTGGTGACTACTGACTGG')
    print(t == 'TATTATACGCTATTATACGCGACGCGGACGCG')