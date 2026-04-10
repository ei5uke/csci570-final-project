import sys
from file_piping import read_input_file, write_output_file

def basic_sequence_alignment_algo(s, t):
    """
    Given two sequences, check for alignment
    parameters:
        s, t (str): a pair of sequences
    returns:
        ...
    """

    # TODO
    return ""

if __name__ == "__main__":
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    s, t = read_input_file(input_file_path)
    output = basic_sequence_alignment_algo(s, t)
    write_output_file(output_file_path, output)