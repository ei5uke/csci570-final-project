import sys
import time
import psutil
import numpy as np

### Helper fxns ###
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

def write_output_file(file_path: str, output: list):
    """
    Create a new file and write the output. If file already exists, return error.
    parameters:
        file_path (str): a path to the output file
        output (list): the output of either the basic or efficient sequence alignment algorithm
    """
    f = open(file_path, "x")
    for i, line in enumerate(output):
        if i != len(output)-1:
            f.write(str(line) + "\n")
        else:
            f.write(str(line))
    f.close()

def process_memory():
    process = psutil.Process()
    memory_info = process.memory_info()
    memory_consumed = int(memory_info.rss/1024) 
    return memory_consumed

def time_wrapper(s: str, t: str):
    start_time = time.time() 
    algo_output = basic_sequence_alignment_algo(s, t)
    end_time = time.time()
    time_taken = (end_time - start_time)*1000
    return time_taken, algo_output
###################

# Provided penalties
ALPHAS = {
    'A': {'A': 0, 'C': 110, 'G': 48, 'T': 94,},
    'C': {'A': 110, 'C': 0, 'G': 118, 'T': 48},
    'G': {'A': 48, 'C': 118, 'G': 0, 'T': 110},
    'T': {'A': 94, 'C': 48, 'G': 110, 'T': 0}
}
DELTA = 30
##########################

def basic_sequence_alignment_algo(s: str, t: str):
    """
    Given two sequences, check for alignment
    parameters:
        s, t (str): a pair of sequences
    returns:
        a list containing the alignment cost, the alignment of the first str, and 
        the alignment of the second str
    """
    m, n = len(s), len(t)

    # DP matrix
    OPT = np.zeros((m+1, n+1), dtype=int)
    
    # Initialization, slide 8/28 in Lecture 8 - DP part 2
    for i in range(m+1):
        OPT[i][0] = i * DELTA
    for j in range(n+1):
        OPT[0][j] = j * DELTA

    # Recurrence DP, slide 7/28 in Lecture 8 - DP part 2
    for i in range(1, m+1):
        for j in range(1, n+1):
            OPT[i][j] = min(
                OPT[i-1][j-1] + ALPHAS[s[i-1]][t[j-1]],
                OPT[i-1, j] + DELTA,
                OPT[i, j-1] + DELTA
            )

    # Cost is determined via DP itself
    cost = OPT[-1][-1]

    # Backtracking to get the aligned strs
    aligned_s = []
    aligned_t = []

    i, j = m, n
    while i > 0 or j > 0:
        if i > 0 and j > 0 and OPT[i][j] == OPT[i-1][j-1] + ALPHAS[s[i-1]][t[j-1]]:
            aligned_s.append(s[i-1])
            aligned_t.append(t[j-1])
            i -= 1
            j -= 1
        elif i > 0 and OPT[i][j] == OPT[i-1][j] + DELTA:
            aligned_s.append(s[i-1])
            aligned_t.append("_")
            i -= 1
        else:
            aligned_s.append("_")
            aligned_t.append(t[j-1])
            j -= 1
    aligned_s.reverse()
    aligned_t.reverse()

    return [cost, ''.join(aligned_s), ''.join(aligned_t)]

if __name__ == "__main__":
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    s, t = read_input_file(input_file_path)
    time_taken, algo_output = time_wrapper(s, t)
    memory_used = process_memory()
    write_output = algo_output
    write_output.append(time_taken)
    write_output.append(memory_used)
    write_output_file(output_file_path, write_output)