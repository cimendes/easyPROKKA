'''
easyPROKKAv version 0.1
Developed by Inês Mendes
'''

import sys
import os



try:
	readsDirectory=sys.argv[1]
	referenceDirectory=sys.argv[2]
	SDSE_file = sys.argv[3]
except IndexError:
	print "Invalid input."
	raise SystemExit

counter=1
currentDir=os.getcwd()

os.chdir(readsDirectory)
reads=os.listdir(readsDirectory)

if not reads:
	print "No reads directories found!"
	raise SystemExit

for item in reads:
	contig_file = item + "/contigs.fasta"

	newOutputDir=currentDir+"/prokka_results/"+item

	os.system("time prokka --outdir %s --locustag SDSE_%s --proteins %s --addgenes %s --centre X --compliant" % (newOutputDir, item, SDSE_file, contig_file))
	counter+=1

print "Reads annotation finished!"

os.chdir(referenceDirectory)
reference=os.listdir(referenceDirectory)
if not reference:
	print "No reference directories found!"
	raise SystemExit

for item in reference:
	reference_file=item
	name=item.split(".")
	name=str(name[0])
	newOutputDir=currentDir+"/prokka_results/"+name
	os.system("time prokka --outdir %s --locustag SDSE_%s --proteins %s --addgenes %s" % (newOutputDir, name, SDSE_file, reference_file))
	counter+=1

print "Reference annotation finished!"
