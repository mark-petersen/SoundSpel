'''
Convert single-line format to csv format. Single line
format is a single line, with only spaces in
between each word.

usage: 
python create_csv_dictionary.py DIAMBG

'''

import string as str
import sys

if len(sys.argv)<1:
    print "input file required"
    sys.exit()
    
################################################
#
#  Read and parse dictionary
#
################################################

# Open file of entries for American (reform) spelling.
filename = sys.argv[1]
f = open(filename, 'r')
rawString = f.read()
f.close()

################################################
#
#  Save translated text as new file
#
################################################

a = str.split(rawString)
f = open(filename+'.csv', 'w')

for i in range(len(a)/2):
    f.write(a[2*i] + "," + a[2*i+1] + "\n");
    
f.close()
