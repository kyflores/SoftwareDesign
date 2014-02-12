# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:19:21 2014

@author: kyle
"""

from gene_finder import *
from amino_acids import aa, codons

#print(collapse(['AAA']))
#coding_strand_to_AA_unit_tests()
#get_reverse_complement_unit_tests()
#rest_of_ORF_unit_tests()
#get_reverse_complement_unit_tests()
#print(find_all_ORFs_oneframe('ATGCATGAATGTAGATAGATGTGCCCCAGATAG'))
#print(find_all_ORFs('ATGCATGAATGTAG'))
print(find_all_ORFs_both_strands('ATGCGAATGTAGCATCAAA'))