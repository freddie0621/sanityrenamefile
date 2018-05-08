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
#print options.filename

# Which file are we working with?
fname = options.filename

import re
#print re.sub(r'[^\x00-\x7f]',r'_', fname)


#print fname
#sys.exit(fname)
#table = maketrans("'ôà,çæéèêë'-?!: ","_oa_caeeee______")



#new_name= fname.translate(table,'').lower().replace(u'?','oe').replace('&','_')
#new_name= re.sub(r'[^\x00-\x7f]',r'_', new_name)
fname1=fname.replace(' ','_').replace('é','e').replace('è','e').replace('î','i').replace('ê','e').replace('â','a').replace('ç','c').replace('\'','_')
new_name = ''.join([s for s in fname1 if s in '_.0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'])

#sys.exit(new_name)
print new_name
rename(fname,new_name)
