'''
Chop_fasta.

The program reads one or more input FASTA files, and chops it up
into separate files, one for each contained sequence
'''

from __future__ import print_function
from argparse import ArgumentParser
import sys
from Bio import SeqIO
import pkg_resources


EXIT_FILE_IO_ERROR = 1
EXIT_COMMAND_LINE_ERROR = 2
EXIT_FASTA_FILE_ERROR = 3
DEFAULT_VERBOSE = False
PROGRAM_NAME = "chop_fasta"


try:
    PROGRAM_VERSION = pkg_resources.require(PROGRAM_NAME)[0].version
except pkg_resources.DistributionNotFound:
    PROGRAM_VERSION = "undefined_version"


def exit_with_error(message, exit_status):
    '''Print an error message to stderr, prefixed by the program name and 'ERROR'.
    Then exit program with supplied exit status.

    Arguments:
        message: an error message as a string.
        exit_status: a positive integer representing the exit status of the
            program.
    '''
    print("{} ERROR: {}, exiting".format(PROGRAM_NAME, message), file=sys.stderr)
    sys.exit(exit_status)


def parse_args():
    '''Parse command line arguments.
    Returns Options object with command line argument values as attributes.
    Will exit the program on a command line error.
    '''
    parser = ArgumentParser(description='Chop fasta file up into pieces')
    parser.add_argument('--version',
                        action='version',
                        version='%(prog)s ' + PROGRAM_VERSION)
    parser.add_argument('--verbose',
                        action='store_true',
                        default=DEFAULT_VERBOSE,
                        help="Print more stuff about what's happening")
    parser.add_argument('fasta_files',
                        nargs='*',
                        metavar='FASTA_FILE',
                        type=str,
                        help='Input FASTA files')
    return parser.parse_args()



def chop_file(fasta_file):
    '''Chop up a single FASTA file into separate sequences.
    Write a new file for each sequence. The file name is derived from the
    sequence header in the FASTA file.

    Arguments:
       fasta_file: an open file object for the FASTA file
    Result:
       None
    '''
    for seq in SeqIO.parse(fasta_file, "fasta"):
        sequence_name = seq.id
        filename = sequence_name + ".fasta"
        SeqIO.write(seq, filename, "fasta")


def process_files(options):
    '''Chop up all the FASTA files on the command line

    Arguments:
       options: the command line options of the program
    Result:
       None
    '''
    if options.fasta_files:
        for fasta_filename in options.fasta_files:
            try:
                fasta_file = open(fasta_filename)
            except IOError as exception:
                exit_with_error(str(exception), EXIT_FILE_IO_ERROR)
            else:
                with fasta_file:
                    chop_file(fasta_file)
    else:
        chop_file(sys.stdin)


def main():
    "Orchestrate the execution of the program"
    options = parse_args()
    process_files(options)


# If this script is run from the command line then call the main function.
if __name__ == '__main__':
    main()
