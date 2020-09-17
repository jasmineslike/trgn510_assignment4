# TRGN510_Assignment4

Create a program called ensg2hugo.py that takes a comma-delimited file as an argument and a column number as an input, and print a file where the Ensembl gene name has become a HUGO name.

## Installation
1. To run this program, you need to install it first:\
   Type: `git clone https://github.com/jasmineslike/trgn510_assignment4.git`
2. Store all files in the same folder, this program should run in the terminal\
3. This program will search gene_name in `Homo_sapiens.GRCh37.75.gtf`:\
   Type: `wget http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz`\
   Type: `gunzip Homo_sapiens.GRCh37.75.gtf.gz`
4. This program provides the Unit Test file `expres.anal.csv`:\
   Type: `wget https://github.com/davcraig75/unit/expres.anal.csv`

## Usage
1. You need to pip install the library:\
   Type: `pip install gffutils`\
   IF SHOWS `PemissionError: Pemission denied`, Type: `python -m pip install --user gffutils`
2. Run the program in the command-line:\
   type: `python ensg2hugo.py -f2 expres.anal.csv >expres.anal.hugo.csv`\
   * It will make the output into a file called `expres.anal.hugo.csv`
   * It allow an option `-f [0-9]` where `-f2` would pick the 2nd column. If there is no `-f` then the first column is used

## Dependencies
1. wget
2. os:
3. re: regular expression
4. gffutils: read gtf file
5. dictionary: a list as a dictionary to look up substitutions.

## Known Issues
* 1494 Ensembl names in the Unit Test File cannot be found in `Homo_sapiens.GRCh37.75.gtf`, so assigned these Ensembl names as "unknown".

## Contact
Lili Xu\
lilixu@usc.edu
