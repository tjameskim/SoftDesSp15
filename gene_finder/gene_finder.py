# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: TJ Kim

"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons, aa_table
import random
from load import load_seq

def shuffle_string(s):
    """ Shuffles the characters in the input string
        NOTE: this is a helper function, you do not have to modify this in any way """
    return ''.join(random.sample(s,len(s)))

### YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###


def get_complement(nucleotide):
    """ Returns the complementary nucleotide

        nucleotide: a nucleotide (A, C, G, or T) represented as a string
        returns: the complementary nucleotide

        I have added 2 more doc tests because T and G may not output A and C respectively
        Now I am sure all 4 nucleotides are well complemented

    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    >>> get_complement('T')
    'A'
    >>> get_complement('G')
    'C'
    """
    # TODO: implement this
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'
    elif nucleotide == 'T':
        return 'A'

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    
    The doctest does not need anything added.
    That is because each test has all four nucleotides in an order that doesnt mirror itself.
    So when we get the correct output, there are very low chances it is by coincidence.
    >>> get_reverse_complement("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> get_reverse_complement("CCGCGTTCA")
    'TGAACGCGG'
    """
    # TODO: implement this
    complement_strand = '' # making an empty string for complementary strand 
    for nucleotide in dna:
        complement_strand = get_complement(nucleotide) + complement_strand 
        #^adds necleotide to beginning of string
    return complement_strand
    

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    
        I am adding one more doctest.
        I want to make sure a stop codon when not in the same triplet,
        cannot stop the string midway.
        Moreover, i need to test this when there is no stop codon in the dna.
        I dont want that to happen

    >>> rest_of_ORF("ATGTGAA")
    'ATG'
    >>> rest_of_ORF("ATGAGATAGG")
    'ATGAGA'
    >>> rest_of_ORF("ATGTTGAATAT")
    'ATGTTGAATAT'
    """
    thirds = [dna[i:i+3] for i in range(0, len(dna), 3)]
    #^divides dna strand into 3
    index = 0
    #^ sets initial index for while loop
    orf_mat = thirds
    #^ matrix set initialy to whole dna, if no stop codon, all will be shown

    while index < len(thirds):
        if thirds[index]  == 'TAG' or thirds[index] == 'TAA' or thirds[index] == 'TGA':
        #^ runs if there is a stop codon in corresponding list element
            orf_mat = thirds[:index]
            #^ reassigns matrix so that it has all the dna elements before stop codon
            index = len(thirds)
            #^ sets index to max value for if statement to hold, so it doesnt run anymore
        else:
            index = index + 1
            #^ reiterate loop with next element in matrix
    orf_rest = ''.join(orf_mat)
    #^ add all element in matrix together to make a string of rest of orf
    return orf_rest

def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs

        I added more tests.
        What will happen when there is a start codon nested inside an orf?
        make sure the nested orf doesn't show on the list
        Also what happens when the dna string does not start with ATG?
        can this output a list of 3 or more orfs?
        what if there is no ATG in the entire dna?
        what if the string starts with a stop codon

    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    >>> find_all_ORFs_oneframe("TAAATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    >>> find_all_ORFs_oneframe("ATGATGCATGAATGTAGATAGATGTGCCCC")
    ['ATGATGCATGAATGTAGA', 'ATGTGCCCC']
    >>> find_all_ORFs_oneframe("ATGTAGCCGATGTAGCCCATGTAGAA")
    ['ATG', 'ATG', 'ATG']
    >>> find_all_ORFs_oneframe("AAAAAAAAA")
    []
    >>> find_all_ORFs_oneframe("TGATAAATGAAATAGAAAATGAAA")
    ['ATGAAA', 'ATGAAA']
    """
    # TODO: implement this
    thirds = [dna[i:i+3] for i in range(0, len(dna), 3)]
    #^ divides dna strand to 3s
    non_nest_orf = []
    #^ makes empty matrix to store the final output orfs in a list
    index = 0
    #^ sets index for while loop

    while index < len(thirds):
        if thirds[index] == 'ATG':
        #^ if a start codon is found in the list
            dna_input = ''.join(thirds[index:])
            #^ all elements after the start codon is joined in the dna list we made
            found_orf = rest_of_ORF(dna_input)
            #^ and is run through previous function so it runs from ATG to next stop codon
            non_nest_orf += [found_orf]
            #^ add the orf to the matrix we made
            added_index = len(found_orf)/3
            #^ update index so while loop sweeps for points after the stop codon
            index = index + added_index
        else:
            index = index + 1
    return non_nest_orf
    #^ return a list of orf strings in given dna


def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs

    I want to test if one reading frame has multiple orfs.

    >>> find_all_ORFs("ATGCATGAATGTAG")
    ['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG']
    >>> find_all_ORFs("ATGAAATAGATGAAATAGAATGTTTTAGAATGCCCTAG")
    ['ATGAAA', 'ATGAAA', 'ATGTTT', 'ATGCCC']
    """
    # TODO: implement this
    output = []
    #^ blank matrix where we store all orfs possible
    for x in range(3):
        output += find_all_ORFs_oneframe(dna[x:])
    return output

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs

    I honestly do not know if this doctest is enough.
    The previous doctests in previous functions were thorough and left small margin for error.
    how will i improve this doctest?
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """
    # TODO: implement this
    both_orf_all = []
    #^ create empty matrix to store all orfs for both regular and reverse complement
    both_orf_all += find_all_ORFs(dna)
    #^ adds to the output list all the orfs w/ offsets from regular dna                
    reverse_dna = get_reverse_complement(dna)
    #^ pulls out the reverse complement strand to work with
    both_orf_all += find_all_ORFs(reverse_dna)
    #^ adds to the output list all the reverse complement dna's orf w/ offsets
    return both_orf_all


def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string

    I added new doc test. I can output something when there is no longest orf
    aka. no orf at all
    We return a empty string

    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    >>> longest_ORF("")
    ''
    """
    # TODO: implement this
    both_orf_all = find_all_ORFs_both_strands(dna)

    if len(both_orf_all) > 0:
        return max(both_orf_all, key = len)
    else:
        return ''

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    # TODO: implement this
    index = 0 # sets initial value for number of trials, hopefully greater than one
    shuffled_dnas = [] # empty list to add output dnas to

    while index < num_trials:
        dna_random = shuffle_string(dna)
        shuffled_dnas += [longest_ORF(dna_random)]
        index += 1
    return max(shuffled_dnas, key = len)

def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment

        We are not adding anymore doctests as the code assumed that the DNA sequence
        is already an orf.
        The only scenario is to worry about a string that is not divisable by 3.
        AKA the string does not have no leftovers from codons (like 1 or 2 nucleotides)
        So the 2nd doc tests tests when there is 2 nucleotides is leftover.

        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
    """
    # TODO: implement this
    thirds = [dna[i:i+3] for i in range(0, len(dna), 3)] #divide string of dna into 3
    protein_list = [] #empty list to input amino acids
    for codon in thirds:
        if len(codon) == 3:
            protein_list += aa_table[codon]
    # sweeping each codon in the list and changing it to a amino acid
    return ''.join(protein_list)

def gene_finder(dna):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.turn
    """
    # TODO: implement this
    threshold = len(longest_ORF_noncoding(dna,1500))
    all_orfs = find_all_ORFs_both_strands(dna)
    amino_acids = [] #empty matrix to store amino acid strings
    output = [] # final output

    for orf in all_orfs:
        if len(orf) >= threshold:
            amino_acids += coding_strand_to_AA(orf)
            output.append(''.join(amino_acids))
            amino_acids = []

    return output


if __name__ == "__main__":
    import doctest
    doctest.testmod()

dna = load_seq("./data/X73525.fa")
print gene_finder(dna)
