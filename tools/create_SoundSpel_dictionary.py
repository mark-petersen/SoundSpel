'''
This script starts with a word frequency list, and then adds look-ups from the DIAMBG SoundSpel file, and adds pronounciation from the cmu pronounciation dictionary.

usage:
python create_SoundSpel_dictionary.py
'''

#!/usr/bin/env python

import csv
import string as str

soundSpelFile = 'DIAMBG.csv'
pronounciationFile = 'cmudict.dict'
wordFrequencyFile = 'b1386.txt'
outFile1 = 'soundSpelDictionary.csv'
outFile2 = 'soundSpelDictionary_coca_only.csv'
outFile3 = 'soundSpelDictionary_with_coca.csv'

ssDict = {}
with open(soundSpelFile) as csv_file:
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

f1 = open(outFile1, 'w')
f2 = open(outFile2, 'w')
f3 = open(outFile3, 'w')

cocaDict = {}
with open(wordFrequencyFile) as csv_file:
    csv_reader2 = csv.reader(csv_file, delimiter='\t')
    line_count = 0
    f1.write(
            "ID" + "," +
            "word" + "," +
            "SoundSpel" + "," +
            "lemma" + "," +
            "partOfSpeach" + "," +
            "pronounciation1" + "," +
            "pronounciation2" + "," +
            "pronounciation3" + "," +
            "pronounciation4" + 
            "\n")
    f2.write(
            "cocaFreq" + "," +
            "bncFreq" + "," +
            "percentCaps" + "," +
            "AmBritSpelling" +
            "\n")
    f3.write(
            "ID" + "," +
            "word" + "," +
            "SoundSpel" + "," +
            "lemma" + "," +
            "partOfSpeach" + "," +
            "cocaFreq" + "," +
            "bncFreq" + "," +
            "percentCaps" + "," +
            "AmBritSpelling" + "," +
            "pronounciation1" + "," +
            "pronounciation2" + "," +
            "pronounciation3" + "," +
            "pronounciation4" + 
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
                        #print(iWord)
                        newWord.append(ssDict.get(iWord, 'NOTRANSLATE'))
                    newWord = str.join(newWord,'-')
                    #print(word,newWord)
                
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
            f1.write(
                    ID + "," +
                    word + "," +
                    ssWord + "," +
                    lemma + "," +
                    partOfSpeach + "," +
                    cmu1 + "," +
                    cmu2 + "," +
                    cmu3 + "," +
                    cmu4 + 
                    "\n")
            f2.write(
                    cocaFreq + "," +
                    bncFreq + "," +
                    percentCaps + "," +
                    AmBritSpelling +
                    "\n")
            f3.write(
                    ID + "," +
                    word + "," +
                    ssWord + "," +
                    lemma + "," +
                    partOfSpeach + "," +
                    cocaFreq + "," +
                    bncFreq + "," +
                    percentCaps + "," +
                    AmBritSpelling +
                    cmu1 + "," +
                    cmu2 + "," +
                    cmu3 + "," +
                    cmu4 + 
                    "\n")
        line_count += 1

f1.close()
f2.close()
f3.close()

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
