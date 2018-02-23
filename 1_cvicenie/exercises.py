# Do tohto suboru vkladajte svoje riesenia
# Nahradte klucove slovicko `pass` telom funkcie, ktoru vytvarate
# Funkcie su uvedene v takom poradi, v akom su zadane. 
# V komentari pri kazdej ulohe je poradove cislo ulohy. 
# Pri rieseni kazdej nasledujucej ulohy mozete pouzivat funkcie, ktore ste si predtym definovali

import re, time, random
from collections import defaultdict

# 1. Max of two numbers.
def max_num( a, b ):
    if a > b: 
           return a;
       
      else:
           return b;


# 2. Max of three numbers.
def max_of_three( a, b, c ):
       if (a >= b) and (a >= c): 
 +            return a;
 +        elif (b >= a) and (b >= c):
 +            return b;
 +        else:
 +            return c;


# 3. Calculates the length of a string.
def str_len( string ):
    counter =0
    for i in string:
        counter = counter+1
        retrun counter;
        
    


# 4. Returns whether the passed letter is a vowel.
def is_vowel( letter ):
    if letter in ('a', 'e', 'i', 'o', 'u'):
    return 1;
    else:
        return 0;


# 5. Translates an English frase into `Robbers language`.
# Sample:
#
#   This is fun
#   Tothohisos isos fofunon
#
def translate( string ):
    pass


# 6. Sum.
# Sums all the numbers in a list.
def sum( items ):
    pass


# 6.1. Multiply.
# Multiplies all the items in a list.
def multiply( items ):
    pass


# 7. Reverse.
# Reverses a string.
# 'I am testing' -> 'gnitset ma I'
def reverse( string ):
    pass


# 8. Is palindrome.
# Checks whether a string is palindrome.
# 'radar' > reversed : 'radar'
def is_palindrome( string ):
    pass


# 9. Is member.
# Checks whether a value x is contained in a group of values.
#   1 -> [ 2, 1, 0 ] : True
def is_member( x, group ):
    pass


# 10. Overlapping.
# Checks whether two lists have at least one number in common
def overlapping( a, b ):
    pass


# 11. Generate n chars.
# Generates `n` number of characters of the given one.
#
#   generate_n_chars( 5, 'n' )
#   -> nnnnn
#
def generate_n_chars( times, char ):
    pass


# 12. Historigram.
# Takes a list of integers and prints a historigram of it.
#   historigram( [ 1, 2, 3 ] ) ->
#       *
#       **
#       ***
#
def historigram( items ):
    pass


# 13. Max in list.
# Gets the larges number in a list of numbers.
def max_in_list( list ):
    pass


# 14. Map words to numbers.
# Gets a list of words and returns a list of integers
# representing the length of each word.
#
#   [ 'one', 'two', 'three' ] -> [ 3, 3, 5 ]
#
def map_words( words ):
    pass


# 15. Find longest wors.
# Receives a list of words and returns the length
# of the longest one.
#
#   [ 'one', 'two', 'three', 'four' ] -> 5
#
def longest_word( words ):
    pass


# 16. Filter long words.
# Receives a list of words and an integer `n` and returns
# a list of the words that are longer than n.
def filter_long_words( words, x ):
    pass


# 17. Version of palindrome that ignores punctuation, capitalization and
# spaces, so that a larger range of frases can be clasified as palindromes.
#
#   ( "Dammit, I'm mad!" ) -> is palindrome
#
def is_palindrome_advanced( string ):
    pass


# 18. Is pangram.
# Checks whether a phrase is pangram, that is, if
# it contains all the letters of the alphabet.
def is_pangram( phrase ):
    pass


# 19. 99 Bottles of beer.
# 99 Bottles of beer is a traditional song in the United States and Canada.
# It has a very repetitive lyrics and it is popular to sing it in very long trips.
# The lyrics of the song are as follows.
#
#   99 bottles of beer in the wall, 99 bottles of beer.
#   Take one down, pass it arrown, 98 bottles of beer.
#
# The song is repeated having one less bottle each time until there are no more
# bottles to count.
#
def sing_99_bottles_of_beer():
    pass


# 20. Note: exercise number 20 is the same as exercise # 30


# 21. Character frequency.
# Counts how many characters of the same letter there are in
# a string.
#
#   ( 'aabbccddddd' ) -> { 'a': 2, 'b': 2, 'c': 2, d: 5 }
#
def char_freq( string ):
    pass


# 22. ROT-13: Encrypt.
# Encrypts a string in ROT-13.
#
#   rot_13_encrypt( 'Caesar cipher? I much prefer Caesar salad!' ) ->
#   Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!
#
def rot_13_encrypt( string ):
    pass


# 22.1 ROT-13: Decrypt.
#
#   rot_13_decrypt( 'Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!' ) ->
#   Caesar cipher? I much prefer Caesar salad!
#
# Since we're dealing with offset 13 it means that decrypting a string
# can be accomplished with the encrypt function given that the alphabet contains
# 26 letters.
def rot_13_decrypt( string ):
    key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',
         'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
         'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
         'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',
         'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
         'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',
         'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
    pass


# 23. Correct.
# Takes a string and sees that 1) two or more occurences of a space
# are compressed into one. 2) Adds a space betweet a letter and a period
# if they have not space.
#
#   correct( 'This   is  very funny  and    cool.Indeed!' )
#   -> This is very funny and cool. Indeed!
#
def correct( string ):
    pass


# 24. Make third Form.
# Takes a singular verb and makes it third person.
#
#   ( 'run' ) -> 'runs'
#   ( 'Brush' ) -> 'brushes'
#
def make_3d_form( verb ):
    pass


# 25. Make `ing` form.
# Given an infinite verb this function returns the
# present participle of it.
#
#   ( 'go' ) -> 'going'
#   ( 'sleep' ) -> 'sleep'
#
def make_ing_form( verb ):
    pass

# 26. Largest Number.
# Given a list of numbers, this function returns the largest one,
# it does it using `reduce` function.
def max_in_list_v1( numbers ):
    pass


# 27. Map strings
# Maps a list of words into a list of integers representing each
# word length.
# It uses the `map()` higher-order-function.
def map_words_v1( words ):
    pass


# 27.1 Map strings.
# Does the same as #27 but uses `List comprehensions`.
# See http://www.secnetix.de/olli/Python/list_comprehensions.hawk
def map_words_v2( words ):
    pass


# 28. Find longest word.
# Using high-order-functions, this function receives a list of words,
# and return the longest one.
def find_longest_word_advanced( words ):
    pass


# 29. Filter Long Words.
# Takes a list of words and an integer and then return
# an array with all the words that are longer in length that
# the integer passed.
def filter_long_words_advanced( words, x ):
    pass


# 30. Translates a list of words from English into Swedish.
# There are a fixed amount of words available for translatation.
# Uses `map()`.
# Sample:
#
#   ( [ 'happy', 'new', 'year' ] ) -> [ 'happy', 'nya', 'år' ]
#
def translate_words( words ):

    d = { 'all': 'alla', 'and': 'och', 'best': 'bäst', 'birthday': 'födelsedag', 'cake': 'kaka', 'celebrate': 'fira', 'christmas': 'jul',
        'come': 'komma', 'dreams': 'drömmar', 'for': 'för', 'good': 'bra', 'happy': 'happy', 'hope': 'hopp', 'inviting': 'inbjudande', 'is': 'är',
        'merry': 'merry', 'new': 'nya',  'thanks': 'tack', 'the': 'den', 'to': 'till', 'true': 'sant', 'us': 'oss', 'we': 'vi',
        'wishes': 'önskemål', 'year': 'år', 'your': 'din' }

    pass


# 31. Map.
# `map()` is a python build-in function which receive a function `f`
# and a list as parameters, and calls the function `f` on every element
# from the list.
# The following function is an implementation of the functionality that
# `map()` accomplishes.
def map_v1( fn, iterable ):
    pass


# 31.1 Filter.
# As well as `map()`, `filter()` is a python built-in higer-order function,
# which get passed a function `f` and a list, and applies `f` to each of the elementf
# in the list, and return a list with only the elements that when passed to `f`
# made `f` return true.
def filter_v1( fn, iterable ):
    pass


# 31.2 Reduce.
# Reduce is also a built-in higer-priority function in python.
# It receives two parameters, the first, a function `f` which receives two
# arguments: `a`, `b`, and the second an iterable `iterable` which can ba a list.
# What `reduce()` does, is calling `f` passing it as parameters the first and the second
# elements in the list, after this, reduce captures the return value of the function
# and passes it to `f` as `a`, and as `b` passes the third element of the list,
# `reduce()` captures the return value and passes it to `f` as `a` and so on, until
# there are no more elements in the list.
#
#   nums = [ 1, 2, 3, 4, 5 ]
#   sum = lambda x, y: x + y
#   reduce_v1( sum, nums )
#  -> 15
#
def reduce_v1( fn, iterable ):
    pass

# 32. Find palidromes.
# Scans a file line by line findind palidromes in it
# and return an array with the palindromes found.
def find_palidromes( filename = 'data/palidromes-32.md' ):
    pass


# 33. Semordnilap.
# A semordnilap is a word that when spelled backwards, produces other word.
# E.G.
#
#   strssed -> desserts
#
# This function, gets all the words in a file and finds all the words
# that when spelled backwards, are equal to other words in the file.
#
def find_semordnilaps( filename = 'data/words-33.md' ):
    pass


# 34. Character frequency table.
# Prints a table showing how many characters of each
# charachter there are in a text file
def char_freq_table( filename = 'data/the-dream.md' ):
    pass



# 35. Speak ICAO
#
# Given a string, this function will translate it to ICAO
# giving a speach of each letter's corresponding tranlation according ICAO dictionary.
# The pause betweet each spoken translated letter and each word can be set.
#
#  ( 'Hello', 0, 1 ) -> Will speach -> 'hotel' `wait 0 seconds`,  'echo' `wait 0 seconds`, 'lima' `wait 0 seconds`,
#      'lima' `wait 0 seconds`, 'oscar' `wait 0 seconds` `and then wait 1 second`
#
# Note: In order for this function to work you should have available `pyttsx` package
# instructions and download can be found in the following link
# https://github.com/parente/pyttsx
#
def speak_ICAO( string, letter_pause, word_pause ):
    pass



# 36. Hapax legomenon
# Finds words that happen to be used only once in a text.
def find_hapax_legomenons( filename = 'data/the-dream.md' ):
    pass


# 37. Add line numbers.
# Given a text file, this function will create a new text file
# in which all the lines from the original file are numbered
# from 1 to n.
def copy_file_count_lines( filename = 'data/text.txt' ):
    pass


# 38. Average_word_length.
# Calculates the average word length in a text file
# passed by the user.
def average_word_length( filename = 'data/the-dream.md' ):
    pass


# 39. Guess the number game.
# Command line game that will randomly select a number from 1 to 20
# and will ask the user to guess it.
def guess_the_number_game():
    pass


# 40. Anagram
# Command line game that given a list of colours will pick one,
# make an Anagram with it and ask the user to decript it.
def anagram_game( words ):
    pass


# 41. Lingo function
# Given two words, this function will compare them and show
# clues on the second one, that may lead to guess the first one.
def lingo( word, guess ):
    pass


# 41 Lingo Game
# Lingo is a game for guessing a hidden 5 characters word.
# Users enter a word and it is compared with the one to guess
# and clues are show for the user to finally guess the word.
def lingo_game():
    pass

# 42. Sentence Splitter
# Given a text file, this program separates its sentences based
# on a set of rules and then, returns the result.
def split_sentences( filename = 'data/text-42.md' ):
    pass


# 43 Helper: Load Words
# Returns an array of all the words in a file
def load_words( filename ):
    pass

# 43. Find Anagram
# Finds all the anagrams in a text file and returns a list
# with all the group of anagrams
# Adapted from answer at
# http://stackoverflow.com/questions/8286554/find-anagrams-for-a-list-of-words
def find_anagrams( filename = 'data/words-43.md' ):
    pass


# 44 Helper: Checks whether a set pairs of squared brackets
# is sintactically correct. This means, whether every opening bracket ( '[' )
# is closed.
# Example:
#    []        True
#    [][]      True
#    []][[]    False
#
def validate_brackets( string ):
    pass


# 44. Analyze backets
# This function generates a random string with `n` opening brackets ( '[' ) and `n`
# closing brackets ( ']' ) in a random order. After that, it checks to see whether
# the generated string is combrises for pairs of opening/closing brackets.
# After that, it print the output to the console like in this example.
# Example:
#
#    []        OK   ][        NOT OK
#    [][]      OK   ][][      NOT OK
#    [[][]]    OK   []][[]    NOT OK
#
def analyze_rand_brackets():
    pass


# 45 Helper:
# Checks whether the list has a word ending with
# a specific letter and return its position,
# returns false if there are no words that match
# the criteria.
def has_word_starting_with( letter, iterable ):
    pass


# 45. This function will generate a sequence with the
# highest possible list of pokemons in which the final letter
# of the name of the preceding one is the first letter of the
# following one
# Example:
#
#   banette -> emboar -> relicant -> tirtuga -> audino ...
#
def words_domino( filename = 'data/pokemons-list.md' ):
    pass


# 46. Anternade
# Given a word list, this function takes each word and tries to make two
# smaller words  using all the letters of that word.
# Example:
#
#   'board': makes 'bad' and 'or'
#   'waists': makes: 'wit' and 'ass'
#
def alternade( filename = 'data/words-43.md' ):
    pass
