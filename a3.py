"""A board is a list of list of str. For example, the board
    ANTT
    XSOB
is represented as the list
    [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

A word list is a list of str. For example, the list of words
    ANT
    BOX
    SOB
    TO
is represented as the list
    ['ANT', 'BOX', 'SOB', 'TO']
"""

def is_valid_word(wordlist, word):
    """ (list of str, str) -> bool

    Return True if and only if word is an element of wordlist.

    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
    True
    """
    b = False
    for item in wordlist:
        if word == item:
            b = True
    return b


def make_str_from_row(board, row_index):
    """ (list of list of str, int) -> str

    Return the characters from the row of the board with index row_index
    as a single string.

    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'ANTT'
    """
    s = ''
    for i in board[row_index]:
        s = s + i
    return s
            

def make_str_from_column(board, column_index):
    """ (list of list of str, int) -> str

    Return the characters from the column of the board with index column_index
    as a single string.

    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'NS'
    """
    s = ''
    for item in board:
        for i in item[column_index]:
            s = s + i
    return s


def board_contains_word_in_row(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the rows of the board contains
    word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB')
    True
    """
    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True

    return False

## ERROR: IndexError
## list index out of range

def board_contains_word_in_column(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the columns of the board
    contains word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    False
    """
    i = 1
    row = 1
    column = 0
    first = board[0]

    while (word[0] != first[column]):
        column = column + 1

    for item in board[1::]:
        if item[column-1] == word[i]:
            row = row + 1
            i = i + 1
           
    if row == len(word):
        return True
    else:
        return False

## Message:
## ERROR: IndexError
## list index out of range

## Message:
## FAILURE: AssertionError
## False != True : Word not found.

def board_contains_word(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if word appears in board.

    Precondition: board has at least one row and one column.

    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT')
    True
    """
    i = 0
    for litera in word:
        for row in board:
            if litera in row:
                i = i + 1
            
    if i == len(word):
        return True
    else:
        return False
        


def word_score(word):
    """ (str) -> int

    Return the point value the word earns.

    Word length: < 3: 0 points
                 3-6: 1 point per character for all characters in word
                 7-9: 2 points per character for all characters in word
                 10+: 3 points per character for all characters in word

    >>> word_score('DRUDGERY')
    16
    """
    k = len(word)
    if k < 3:
        k = k * 0
    elif k <= 6:
        k = k * 1
    elif k <= 9:
        k = k * 2
    else:
        k = k * 3
    return k

def update_score(player_info, word):
    """ ([str, int] list, str) -> NoneType

    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.

    >>> update_score(['Jonathan', 4], 'ANT')
    """
    score = 1
    player_info[score] =  player_info[score] + len(word)


## Message:
## FAILURE: AssertionError
## 0 != 13 : Wrong number of words found on board.
def num_words_on_board(board, words):
    """ (list of list of str, list of str) -> int

    Return how many words appear on board.

    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
    3
    """
    i = 0
    for word in words:
        if board_contains_word(board, word) == True:
            i = i + 1
    return i


def read_words(words_file):
    """ (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    words_file. 

    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English  alphabet.
    """
    words = []
    for line in words_file:
        words.append(line.rstrip('\n'))
    #print(words)
    return words        
    

def read_board(board_file):
    """ (file open for reading) -> list of list of str

    Return a board read from open file board_file. The board file will contain
    one row of the board per line. Newlines are not included in the board.
    """
    line = []
    for lines in board_file:
        line.append(lines.rstrip('\n'))
#       print(line, end='')
    return line

