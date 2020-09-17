# TRGN510_Assignment4

This is a program called "ensg2hugo.py" that takes a comma-delimited file as an argument and a column number as an input, and print a file where the Ensembl gene name has become a HUGO name.

## Installation
1. To get `Homo_sapiens.GRCh37.75.gtf`:\
   type: `wget http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz`\
   type: `gunzip Homo_sapiens.GRCh37.75.gtf.gz`
2. To get `expres.anal.csv`:\
   type: `wget https://github.com/davcraig75/unit/expres.anal.csv`
3. Make sure that these two files are in the same directory

## Usage
1. To install this program:\
   type: `git clone https://github.com/yuwen841019/TRGN510_Assignment4`
2. To run this program:
   type: `python ensg2hugo.py -f2 expres.anal.csv >expres.anal.hugo.csv`
3. It will then output a file `expres.anal.hugo.csv`.
4. There is an option “-f [0-9]” where -f2 would pick the 2nd column. If there is no “-f” then the first column is used.

## Dependencies
1. wget
2. fileinput
3. regex
4. pandas

## Result
Known: There are 17549 Ensembl names that can transfer to HUGO names.\
Unknown issue: There are 1494 Ensembl names that cannot be found in `Homo_sapiens.GRCh37.75.gtf`, so they are classified as"unknown".

## Contact
lilixu@usc.edu
