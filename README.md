# Overview 

The program reads one or more input FASTA files. It splits each file into multiple files, one for each sequence in the file. The name of the output file uses the sequence header. 

# Licence

This program is released as open source software under the terms of [MIT License](https://raw.githubusercontent.com/chop_fasta/chop_fasta/master/LICENSE)

# Installing

Chop_fasta can be installed using `pip` in a variety of ways (`%` indicates the command line prompt):

1. Inside a virtual environment: 
```
% virtualenv chop_fasta_dev
% source chop_fasta_dev/bin/activate
% pip install -U /path/to/chop_fasta
```
2. Into the global package database for all users:
```
% pip install -U /path/to/chop_fasta
```
3. Into the user package database (for the current user only):
```
% pip install -U --user /path/to/chop_fasta
```

# General behaviour

# Usage 

In the examples below, `%` indicates the command line prompt.

## Help message

Chop_fasta can display usage information on the command line via the `-h` or `--help` argument:
```
% chop_fasta -h
usage: chop_fasta [-h] [--version] [--verbose] [FASTA_FILE [FASTA_FILE ...]]

Chop fasta file up into pieces

positional arguments:
  FASTA_FILE  Input FASTA files

optional arguments:
  -h, --help  show this help message and exit
  --version   show program's version number and exit
  --verbose   Print more stuff about what's happening
```


# Exit status values

Chop_fasta returns the following exit status values:

* *0*: The program completed successfully.
* *1*: File I/O error. This can occur if at least one of the input FASTA files cannot be opened for reading. This can occur because the file does not exist at the specified path, or chop_fasta does not have permission to read from the file. 
* *2*: A command line error occurred. This can happen if the user specifies an incorrect command line argument. In this circumstance chop_fasta will also print a usage message to the standard error device (stderr).
* *3*: Input FASTA file is invalid. This can occur if chop_fasta can read an input file but the file format is invalid. 

# Bugs

File at our [Issue Tracker](https://github.com/chop_fasta-paper/chop_fasta/issues)
