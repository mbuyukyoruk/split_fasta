import math
import argparse
import sys
import subprocess
import re
import textwrap

try:
    from Bio import SeqIO
except:
    print("SeqIO module is not installed! Please install SeqIO and try again.")
    sys.exit()

try:
    import tqdm
except:
    print("tqdm module is not installed! Please install tqdm and try again.")
    sys.exit()

parser = argparse.ArgumentParser(prog='python split_fasta.py',
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=textwrap.dedent('''\

Author: Murat Buyukyoruk

        split_fasta help:

This script is developed to split large multifasta file into smaller files for easy manipulation. 

SeqIO package from Bio is required to fetch flank sequences. Additionally, tqdm is required to provide a progress bar since some multifasta files can contain long and many sequences.

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

      	'''))
parser.add_argument('-i', '--input', required=True, type=str, dest='filename',
                    help='Specify a original fasta file.\n')
parser.add_argument('-n', '--number', required=True, type=str, dest='number',
                    help='Specify a number of output file.\n')

results = parser.parse_args()
filename = results.filename
number = results.number

proc = subprocess.Popen("grep -c '>' " + filename, shell=True, stdout=subprocess.PIPE, text=True)
length = float(proc.communicate()[0].split('\n')[0])

div = math.ceil(float(length / (float(number))))

with tqdm.tqdm(range(int(length)), desc='Spliting...') as pbar:
    i = 1
    l = 1
    for record in SeqIO.parse(filename, "fasta"):
        if i < div:
            l = l
        if i > div:
            l += 1
            i = 1
        out = filename.split('.')[0] + "_" + str(l) + "." + filename.split('.')[1]
        pbar.update()
        f = open(out, 'a')
        sys.stdout = f
        print(record.format("fasta"))
        i += 1

