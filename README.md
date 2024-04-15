# split_fasta

Author: Murat Buyukyoruk

        split_fasta help:

This script is developed to split large multifasta file into smaller files for easy manipulation. 

SeqIO package from Bio is required to fetch flank sequences. Additionally, tqdm is required to provide a progress bar since some multifasta files can contain 
long and many sequences.

Syntax:

        python split_fasta.py -i demo.fasta -n 5

split_fasta dependencies:
	Bio module and SeqIO available in this package          refer to https://biopython.org/wiki/Download
	tqdm                                                    refer to https://pypi.org/project/tqdm/

Input Paramaters (REQUIRED):
----------------------------
	-i/--input		FASTA			Specify a multifasta file.

	-n/--number		Number			Specify a number of files to create for splitting fasta.

Basic Options:
--------------
	-h/--help		HELP			Shows this help text and exits the run.

