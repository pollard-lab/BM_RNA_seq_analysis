#!/usr/bin/python2.7
import os


####UNTESTED########

def get_TPM_Summary(transcripts):
    lines_to_output = ['Transcript']  # initilize header line
    lines_to_output.append(sfFiles)  # add column names for each .sf file
    for transcript in transcripts:
        lines_to_output.append(transcript_summary(transcript))
    return lines_to_output


def transcript_summary(transcript):
    single_line = [transcript]  # main list for the line

    # get all TPM value info from all files, add to list representing that line
    for file in sfFiles:
        single_line.append(get_TPM(file, transcript))
    return single_line


def get_TPM(file, transcript):
    with open(file) as f:
        lines = f.readlines()

    for line in lines:
        if transcript in line:
            x = float(line.split('\t')[3])
            x = float("{0:.4f}".format(x))
            if x == 0.0:
                x = 0
            return str(x)


def get_all_transcripts_names_from_file(file):

    with open(file) as f:
        lines = f.readlines()

    trans = []
    for line in lines:
        x = (line.split('\t')[0])
        trans.append(x)
    transcripts = trans[1:]
    return(transcripts)


if __name__ == "__main__":

    # load .sf files
    path = os.curdir
    files = os.listdir(path)
    sfFiles = [i for i in files if i.endswith('.sf')]

    transcripts = get_all_transcripts_names_from_file(sfFiles[0])  # get list of all transripts to get TPMs for
    output_lines = get_TPM_Summary(transcripts)  # get all lines to write to csv

    # write csv
    filename = "All_TPMs.csv"
    with open(filename, 'w+') as file:
        file.writelines(','.join(i) + '\n' for i in output_lines)

    print("Done.")
