#!/usr/bin/env python3
import os
import sys
import getopt
import glob
import re
from collections import OrderedDict

pwd = os.getcwd()

somaticFolders = ["02-mapping",
        "03-bamconversion",
        "03.5-sortubam",
        "04-mergebam",
        "04.5-sortedlanes",
        "05-markduplicates",
        "06-baserecalibration",
        "07-ApplyBaseRecalibration",
        "07.5-AnalyzeRecalibration", 
        "08-Mutect",
        "08.5-LearnBias",
        "09-PileupSummary",
        "10-CalculateContaamination",
        "11-FilterMutectCalls",
        "13-Funcotator"]
# Parses arguments and returns the directory with the fastq files
def parse(argv):
    fastqDir = ''
    try:
        opts, args = getopt.getopt(argv,"hi:",["input-folder="])
    except getopt.GetoptError:
        print('callSom.py -i <inputfolder>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('callSom.py -i <inputfolder>')
            sys.exit()
        elif opt in ("-i", "--input-folder"):
            fastqDir = arg
    return fastqDir

# Gets sample names from the directory and returns a dictionary that maps
# sample name to all the corresponding fastq files
def getSampNames(fastqDir):
    files = glob.glob(f"{fastqDir}/*.fastq")
    names = []
    nameToFiles = {}
    for file in files:
        inter_name = os.path.splitext(os.path.basename(file))[0]
        #print(inter_name)
        final_name = re.search('^.+?(?=_L00)',inter_name)
        #print(final_name.group())
        names.append(final_name.group())
    names = list(OrderedDict.fromkeys(names))
    for name in names:
        nameToFiles[name] = [file for file in files if re.search(name, file)]
    #for name, fastqs in nameToFiles.items():
        #print(f"Name: {name} maps to {fastqs}")
    return nameToFiles

def mapSetReadgroup():


# Merges lanes for each sample. First does per read group mapping, and then merges and marks duplicates
def mergeLanes(samples):
    for name, fastqs in samples.items():

def main(argv):
    fastqDir = parse(argv)
    samples = getSampNames(fastqDir)

if __name__ == "__main__":
   main(sys.argv[1:])

