def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    result = 0    
    for litera in dna:
        result = result + 1
    return result


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    b = False
    if get_length(dna1) > get_length(dna2):
        b = True
    return b

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """ 
    count = 0
    for litera in dna:
        if nucleotide == litera:
            count = count + 1
    return count


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    b = False
    if dna1.find(dna2) != -1:
        b = True        
    return b

def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if the DNA sequence is valid
    (that is, it contains no characters other than
    'A', 'T', 'C' and 'G').

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ATCGEC')
    False

    """
    b = True    
    for litera in dna:
        if litera != 'A' and litera != 'T' and litera != 'C' and litera != 'G':
            b = False
    return b

def insert_sequence(dna1, dna2, index):
    """
    (str, str, int) -> str

    Return the DNA sequence obtained by inserting the second DNA sequence
    into the first DNA sequence at the given index.
    (You can assume that the index is valid.)
    
    >>> insert_sequence('CCGG', 'AT', 2)
   'CCATGG'
    >>> insert_sequence('CCGTA', 'ATC', 5)
    False
    
    """
    dna ="" 
    dna = dna1[0:index] + dna2 + dna1[index:]
    return dna

def get_complement(dna1):
    '''
    (str) -> str

    Return the nucleotide's complement. We have
    intentionally not given you any examples for this function. 

    >>>get_complement('GAATTC')
    'CTTAAG'
    >>>get_complement('GGATCC')
    'CCTAGG'
    '''
    dna2 = ''
    for litera in dna1:
        if litera == 'A':
            dna2 = 'T'
        elif litera == 'T':
            dna2 = 'A'
        elif litera == 'G':
            dna2 = 'C'           
        elif litera == 'C':
            dna2 = 'G'            
    return dna2

def get_complementary_sequence(dna1):
    '''
    (str) -> str
    Return the DNA sequence that is complementary
    to the given DNA sequence

    >>>get_complement('GAATTC')
    'CTTAAG'
    >>>get_complement('GGATCC')
    'CCTAGG'
    '''
    dna2 = ''
    for litera in dna1:
        if litera == 'A':
            dna2 = dna2 + 'T'
        elif litera == 'T':
            dna2 = dna2 + 'A'
        elif litera == 'G':
            dna2 = dna2 + 'C'           
        elif litera == 'C':
            dna2 = dna2 + 'G'
    return dna2
