from distutils.core import setup
#import py2exe, sys, os,PIL,urllib,zipfile
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'optimize': 2}},
    windows = [{'script': "SANITYFILE.py"}],
    zipfile = "shared.lib",
)