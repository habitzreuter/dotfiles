#!/usr/bin/env python3

import sys
import requests

def doi2bib(doi):
  """
  Return a BibTeX string of metadata for a given DOI.
  From https://gist.github.com/jrsmith3/5513926
  """

  url = "http://dx.doi.org/" + doi

  headers = {"accept": "application/x-bibtex"}
  r = requests.get(url, headers = headers)

  return r.text

def help():
    """
    Prints help.
    """
    print('Usage: python3 annotate.py [DOI]')

if (len(sys.argv) != 2):
    help()
    sys.exit()

doi = sys.argv[1]
bibtex = doi2bib(doi)
print(bibtex)

