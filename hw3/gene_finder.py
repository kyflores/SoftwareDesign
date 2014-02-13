# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: YOUR NAME HERE
"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons
import random

def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
        Any imcomplete sets of 3 at the end will be ignored.
    """
    #>>> coding_strand_to_AA("ATGCGA")
    #'MR'
    aminoOutput='' #declare the output string.
    if(len(dna)%3!=0):
        print('There is an incomplete set of 3 base pairs.  It will be ignored.')
    for l in range(len(dna)/3):
        codon=dna[3*l:3*l+3] #In this for loop, examines the string 3 items at a time.
        for k in range(len(codons)):
            if codon in codons[k]:
                aminoOutput=aminoOutput+aa[k]
    return(aminoOutput)
            

def coding_strand_to_AA_unit_tests(): #not done
    """ Unit tests for the coding_strand_to_AA function """
    print('input: ACGTAG, expected output: T|, actual output:')+str(coding_strand_to_AA('ACGTAG'))
    print('input: TCAGCAK, expected output: SA, actual output:')+str(coding_strand_to_AA('TCAGCA'))
    

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    output=''
    for i in range(len(dna)):#Creates a new string with opposite base pairs.
        if dna[i]=='A':
            add='T'
        elif dna[i]=='C':
            add='G'
        elif dna[i]=='T':
            add='A'
        elif dna[i]=='G':
            add='C'
        output=output+add
    output=output[::-1]#Reverse the string!
    return output
            
def get_reverse_complement_unit_tests(): #not done 
    """ Unit tests for the get_complement function """
    print('input: GCATGCT, expected output:AGCATGC, actual output:')+str(get_reverse_complement('GCATGCT'))
    print('input: TGACGTAGA, expected output:TCTACGTCA, actual output:')+str(get_reverse_complement('TGACGTAGA'))
    
def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    #startCodons=codons[3] #Turns out this wasn't necessary.
    stopCodons=codons[10] #extract the 3 stop codon sequences to check later.
    endPos=len(dna)+1 #A variable to store the position of the first stop codon intialized so that the entire string is returned if no end codon.
    for l in range(len(dna)/3):
        codon=dna[3*l:3*l+3] #In this for loop, examines the string 3 items at a time.
        if codon in stopCodons:
            endPos=l*3 #sets endPos to the position of the first character of the stop codon.
            break #Stops the loop as soon as it finds a stop codon so that multiple reading frames can be found.
    return dna[0:endPos]
    
def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
    print('input: GCATGCTAG, expected output:GCATGC, actual output:')+str(rest_of_ORF('GCATGCTAG'))
    print('input: GCATGCGTAAATAG, expected output:GCATGCGTAAATAG, actual output:')+str(rest_of_ORF('GCATGCGTAATAG'))       
    #The second unit test tests for codons of incorrect lengths.
        
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    startCodons=codons[3]
    output_list=[]
    while len(dna)>0:
        codon=dna[0:3] #In this for loop, examines the string 3 items at a time.
        if codon in startCodons:
             dnaSet=rest_of_ORF(dna)
             output_list.append(dnaSet)
             dna=dna[len(dnaSet):len(dna)+1] #If a start codon is found, continue to the stop codon, 
                                             #save what you found, then delete it from dna.
        else:
             dna=dna[3:len(dna)+1] #If we examine a set of 3, and that set is not a start codon, remove it.  
                                   #This lets us ignore stuff at the front of the string that isn't in a reading frame!
    return output_list
    
def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """
    print('input: ATGCGAGACTAGATGCGACAGTAG, expected output:ATGCGAGAC, ATGCGACAG, actual output:')+str(find_all_ORFs_oneframe('ATGCGAGACTAGATGCGACAGTAG'))
    print('input: GCATGCGTAAATAG, expected output:[], actual output:')+str(find_all_ORFs_oneframe('GCATGCGTAATAG'))       

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    dna2=dna[1:len(dna)+1] #make copies where the dna is shifted over one.
    dna3=dna[2:len(dna)+1]
    output1=find_all_ORFs_oneframe(dna)
    output2=find_all_ORFs_oneframe(dna2)
    output3=find_all_ORFs_oneframe(dna3)
    return output1+output2+output3

def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
    print('input: ATGCATGCGAGCTAGATAG, expected output:ATGCATGCGAGC, ATGCGAGCTAGA actual output:')+str(find_all_ORFs('ATGCATGCGAGCTAGATAG'))    
    
def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    forward=find_all_ORFs(dna)
    reverse=find_all_ORFs(get_reverse_complement(dna))
    return forward + reverse

def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """

    # YOUR IMPLEMENTATION HERE

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""
    L=find_all_ORFs_both_strands(dna)
    comparisonValue=0; #A variable to store the length of the longest ORF found so far.
    output=''
    for i in range(len(L)):
        if len(L[i])>comparisonValue:
            output=L[i]
            comparisonValue=len(L[i])
    return output
            

def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """

    # YOUR IMPLEMENTATION HERE

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    comparisonValue=0
    for i in range (num_trials):
        dnaList=list(dna)
        random.shuffle(dnaList)
        dna=collapse(dnaList)
        K=longest_ORF(dna)
        if len(K)>comparisonValue:
            output=K
            comparisonValue=len(K)
    return output
        
        

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """

    # YOUR IMPLEMENTATION HERE