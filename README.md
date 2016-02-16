#Usage:

`easyProkkaComplete.py <reads directory> <reference fasta directory> <protein Fasta file>` 

#Description

 Scipt to easilly run PROKKA,  a software tool for the rapid annotation of prokaryotic genomes, one or more assembled contig file, saved in one directory. 
 
 Requires: PROKKA version 1.11 or similar, path to directory with assembled contigs, each in its own subdirectory, path to directory with the reference fasta files, path to Fasta file of trusted proteins to first annotate from.
 Ensures: SPAdes assembly outp1.11 

# Example of Usage:
`easyProkkaComplete.py ~/dummydirectory/assembled_reads/ ~/dummydirectory/reference_fastas/  ~/SDSE_protein_file.fasta`