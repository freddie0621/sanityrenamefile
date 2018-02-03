# -*- coding: iso-8859-1 -*-
from os import rename, listdir
import sys
import os
from string import maketrans

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
(options, args) = parser.parse_args()
print options.filename

# Which file are we working with?
fname = options.filename




#print fname
#sys.exit(fname)
table = maketrans("'ôà,çæéèêë'-?!: ","_oa_caeeee______")



new_name= fname.translate(table,'').lower().replace(u'?','oe').replace('&','_')

#sys.exit(new_name)

rename(fname,new_name)


