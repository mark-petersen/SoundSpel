'''
Convert single-line format to csv format. Single line
format is a single line, with only spaces in 
between each word.

usage: 
python create_csv_dictionary.py

where input.html is the original in standard spelling,
and output.html is in reform spelling.  
Create input.html by saving a page from your web
browser.  View output.html by openning that file
from disk in your web browser.

In addition, this script must have access to the 
file DIAMBG, a dictionary of American (reform) 
spelling, in the run directory.

Mark Petersen
August 2016
'''

import numpy as np
import string as str
import sys
    
################################################
#
#  Read and parse dictionary
#
################################################

# Open file of entries for American (reform) spelling.
f = open('DIAMBG', 'r')
rawString = f.read()
f.close()

################################################
#
#  Save translated text as new file
#
################################################

a = str.split(rawString)
f = open('DIAMBG.csv', 'w')

for i in range(len(a)/2):
    f.write(a[2*i] + "," + a[2*i+1] + "\n");
    
f.close()
