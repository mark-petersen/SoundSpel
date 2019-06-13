'''
Convert single-line format to csv format. Single line
format is a single line, with only spaces in
between each word.

usage:
python create_csv_dictionary.py DIAMBG

'''

#!/usr/bin/env python

#from __future__ import absolute_import, division, print_function, \
#    unicode_literals

import argparse
import csv
import string as str

parser = argparse.ArgumentParser(
    description=__doc__, formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('-b', '--beginID', dest='beginID', type=int,
                    required=False, default='1',
                    help='First word ID for parsing, ie first row of the COCA file')
parser.add_argument('-e', '--endID', dest='endID', type=int,
                    required=False, default='100',
                    help='Last word ID for parsing, ie last row of the COCA file')
#parser.add_argument('-s', '--soundSpellFile', dest='soundSpellFile', type=str,
#                    required=False, default='DIAMBG.csv')#,
#                    #help='The name of the old SoundSpell file')
#parser.add_argument('-p', '--pronounciationFile', dest='pronounciationFile', type=str,
#                    required=False, default='cmudict_SPHINX_40.txt',
#                    help='The name of the pronounciation file')
#parser.add_argument('-c', '--wordFrequencyFile', dest='wordFrequencyFile', type=str,
#                    required=False, default='b1386.txt',
#                    help='The name of the word frequency file')
#parser.add_argument('-o', '--outFile', dest='outFile', type=str,
#                    required=False, default='soundSpellDictionary.csv',
#                    help='The name of the output file')

args = parser.parse_args()

soundSpellFile = 'DIAMBG.csv'
pronounciationFile = 'cmudict.dict'
wordFrequencyFile = 'b1386.txt'
outFile = 'soundSpellDictionary.csv'

ssDict = {}
with open(soundSpellFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        ssDict[row[0]] = row[1]

cmuDict1 = {}
cmuDict2 = {}
cmuDict3 = {}
cmuDict4 = {}
with open('cmudict.dict_1') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for row in csv_reader:
        cmuDict1[row[0]] = row[1]
with open('cmudict.dict_2') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for row in csv_reader:
        cmuDict2[row[0]] = row[1]
with open('cmudict.dict_3') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for row in csv_reader:
        cmuDict3[row[0]] = row[1]
with open('cmudict.dict_4') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for row in csv_reader:
        cmuDict4[row[0]] = row[1]

f = open(outFile, 'w')

cocaDict = {}
with open(wordFrequencyFile) as csv_file:
    csv_reader2 = csv.reader(csv_file, delimiter='\t')
    line_count = 0
    f.write(
            "ID" + "," +
            "word" + "," +
            "SSword" + "," +
            "cmu1" + "," +
            "cmu2" + "," +
            "cmu3" + "," +
            "cmu4" + "," +
            "lemma" + "," +
            "partOfSpeach" + "," +
            "percentCaps" + "," +
            "cocaFreq" + "," +
            "bncFreq" + "," +
            "AmBritSpelling" +
            "\n")

    for row in csv_reader2:
        if line_count > 2:
            ID = row[0]
            word = row[1].lower()
            ssWord = ssDict.get(word, '')
            if ssWord=='':
                if '-' in word:
                    newWord = []
                    wordSplit = str.split(word,'-')
                    for iWord in wordSplit:
                        print(iWord)
                        newWord.append(ssDict.get(iWord, 'NOTRANSLATE'))
                    newWord = str.join(newWord,'-')
                    print(word,newWord)
                
            cmu1 = cmuDict1.get(word, '')
            cmu2 = cmuDict2.get(word, '')
            cmu3 = cmuDict3.get(word, '')
            cmu4 = cmuDict4.get(word, '')
            lemma = row[2]
            partOfSpeach = row[3]
            percentCaps = row[4]
            AmBritSpelling = row[5]
            cocaFreq = row[7]
            bncFreq = row[8]
            f.write(
                    ID + "," +
                    word + "," +
                    ssWord + "," +
                    cmu1 + "," +
                    cmu2 + "," +
                    cmu3 + "," +
                    cmu4 + "," +
                    lemma + "," +
                    partOfSpeach + "," +
                    percentCaps + "," +
                    cocaFreq + "," +
                    bncFreq + "," +
                    AmBritSpelling +
                    "\n")
        line_count += 1

f.close()

# print("beginID %g",beginID)

################################################
#
#  Read and parse dictionary
#
################################################

# Open file of entries for American (reform) spelling.
#filename = sys.argv[1]
#f = open(filename, 'r')
#rawString = f.read()
#f.close()

################################################
#
#  Save translated text as new file
#
################################################

#a = str.split(rawString)
#f = open(filename+'.csv', 'w')
#
#for i in range(len(a)/2):
#    f.write(a[2*i] + "," + a[2*i+1] + "\n");
#
#f.close()
