import sys
import time
import psutil
import numpy as np
from basic import basic_sequence_alignment_algo

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
    algo_output = efficient_sequence_alignment_algo(s, t)
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

TRIVIAL = 2

def alignment_cost_column(X, Y):
    m = len(X)
    n = len(Y)

    # Use only 2 columns
    previous_col = np.zeros(n+1, dtype=int)
    current_col = np.zeros(n+1, dtype=int)

    # Aligning 0 chars of X with k chars of Y
    for k in range(0, n+1):
        previous_col[k] = k * DELTA

    # Recurrence
    for i in range(1, m+1):
        current_col[0] = i * DELTA
        for k in range(1, n+1):
            current_col[k] = min(previous_col[k-1] + ALPHAS[X[i-1]][Y[k-1]], 
                                 previous_col[k] + DELTA,
                                 current_col[k-1] + DELTA)
        for k in range(0, n+1):
            previous_col[k] = current_col[k]
    return previous_col

def divide_and_conquer_alignment(X, Y):
    m = len(X)
    n = len(Y)

    # Base case
    if m <= TRIVIAL or n <= TRIVIAL:
        result = basic_sequence_alignment_algo(X, Y)
        return [result[1], result[2]]
    
    # Divide step, split X in half
    X_mid = m // 2
    X_L = X[0:X_mid]
    X_R = X[X_mid:m]

    # Get optimal cost of alignment between X_L and (y1 ... yk)
    left_costs = alignment_cost_column(X_L, Y)

    # Get optimal cost of alignment between X_R and (yn-k ... yn)
    right_costs = alignment_cost_column(X_R[::-1], Y[::-1])[::-1]

    # Find split point k in Y that minimizes total cost
    final_k = 0
    final_cost = left_costs[0] + right_costs[0]
    for k in range(1, n+1):
        total = left_costs[k] + right_costs[k]
        if total < final_cost:
            final_k = k
            final_cost = total
    
    # Recurse on both halfs
    left = divide_and_conquer_alignment(X_L, Y[0:final_k])
    right = divide_and_conquer_alignment(X_R, Y[final_k:n])
    return [left[0] + right[0], left[1] + right[1]]


def efficient_sequence_alignment_algo(s: str, t: str):
    """
    Given two sequences, check for alignment
    parameters:
        s, t (str): a pair of sequences
    returns:
        a list containing the alignment cost, the alignment of the first str, and 
        the alignment of the second str
    """
    # Get alignment
    alignment = divide_and_conquer_alignment(s, t)
    aligned_s = alignment[0]
    aligned_t = alignment[1]

    # Compute cost
    cost = 0
    for i in range(len(aligned_s)):
        if aligned_s[i] == "_" or aligned_t[i] == "_":
            cost += DELTA
        else:
            cost += ALPHAS[aligned_s[i]][aligned_t[i]]

    return [cost, aligned_s, aligned_t]

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