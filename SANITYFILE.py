# -*- coding: iso-8859-1 -*-
from os import rename, listdir
import sys
import os
from string import maketrans

# Which file are we working with?
input_file = sys.argv[1]
#input_file = "001.epub"
# Where do does the file have to be saved?
#output_file = sys.argv[2]
#output_file = "toto1.jpg"
# Required size?
#size = int(sys.argv[3])
#size = 600








table = maketrans("æéèê'-?!: ", "aeee______")
#chaine = "? l'orée du bois"
fname = ' '.join(sys.argv[1:])
#print fname
#sys.exit(fname)
table = maketrans("çæéèê'-?!: ", "caeee______")
chaine = "? l'orée du bois"
fname = ' '.join(sys.argv[1:])
new_name= fname.translate(table, ' ').replace(' ','_').lower()

#sys.exit(new_name)

rename(fname,new_name)

#print chaine.translate(table, ' ')
#new_name= fname.translate(maketrans(" æéèê'-?!: ", "_aeee______")).lower()
#print new_name
#sys.exit('==1=')
#sys.exit(new_name)
#sys.exit('+++')
