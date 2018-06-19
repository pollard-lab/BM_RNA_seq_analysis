#!/bin/bash
# This script generates TPMs for each fastq file in the current working directory
# $1 = transcriptome

echo "STEP_A: Creating Index Files"
salmon index -t $1 --index transcripts_index --type quasi -k 31

echo "STEP_B: Quantifying"
for fastq_file in *.fastq; do
    foldername=$(echo $fastq_file | cut -d'.' -f 1)
    foldername+="_counts"
    mkdir $foldername
    salmon quant --index transcripts_index --libType SR -r $fastq_file -o $foldername
done
echo

echo "STEP_C: parse the counts folders for TPMs"
mkdir copy_of_all_sf_files

for dir in *_counts*; do
	sf_new_name=$(echo $dir)
	sf_new_name+=".sf"
	cd $dir
	mv *.sf $sf_new_name
	cp $sf_new_name ..
	cd ..
	mv $sf_new_name copy_of_all_sf_files
done