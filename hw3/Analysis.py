# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 19:49:22 2014

@author: kyle
"""

from gene_finder import *
from load import *

gene=load_seq('/home/kyle/SoftwareDesign/hw3/data/X73525.fa')
threshold=longest_ORF_noncoding(gene,1500)
print(threshold)
proteins=gene_finder(gene,threshold)
print(proteins)