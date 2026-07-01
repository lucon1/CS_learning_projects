# 6.100A Fall 2022
# Problem Set 3
# Written by: sylvant, muneezap, charz, anabell, nhung, wang19k, asinelni, shahul, jcsands

# Problem Set 3
# Name: Lucas Harlien
# Collaborators:

# Purpose: Check for similarity between two texts by comparing different kinds of word statistics.

import string
import math


### DO NOT MODIFY THIS FUNCTION
def load_file(filename):
    """
    Args:
        filename: string, name of file to read
    Returns:
        string, contains file contents
    """
    # print("Loading file %s" % filename)
    inFile = open(filename, 'r')
    line = inFile.read().strip()
    for char in string.punctuation:
        line = line.replace(char, "")
    inFile.close()
    return line.lower()


### Problem 0: Prep Data ###
def text_to_list(input_text):
    """
    Args:
        input_text: string representation of text from file.
                    assume the string is made of lowercase characters
    Returns:
        list representation of input_text, where each word is a different element in the list
    """
    list_text = input_text.split()
    return list_text


### Problem 1: Get Frequency ###
def get_frequencies(input_iterable):
    """
    Args:
        input_iterable: a string or a list of strings, all are made of lowercase characters
    Returns:
        dictionary that maps string:int where each string
        is a letter or word in input_iterable and the corresponding int
        is the frequency of the letter or word in input_iterable
    Note: 
        You can assume that the only kinds of white space in the text documents we provide will be new lines or space(s) between words (i.e. there are no tabs)
    """
    dict_frequency = {}
    for elem in input_iterable:
        if elem not in dict_frequency:
            dict_frequency[elem] = 1
        else:
            dict_frequency[elem] += 1
    return dict_frequency


### Problem 2: Letter Frequencies ###
def get_letter_frequencies(word):
    """
    Args:
        word: word as a string
    Returns:
        dictionary that maps string:int where each string
        is a letter in word and the corresponding int
        is the frequency of the letter in word
    """
    return get_frequencies(word)


### Problem 3: Similarity ###
def calculate_similarity_score(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary of letters of word1 or words of text1
        freq_dict2: frequency dictionary of letters of word2 or words of text2
    Returns:
        float, a number between 0 and 1, inclusive
        representing how similar the words/texts are to each other

        The difference in words/text frequencies = DIFF sums words
        from these three scenarios:
        * If an element occurs in dict1 and dict2 then
          get the difference in frequencies
        * If an element occurs only in dict1 then take the
          frequency from dict1
        * If an element occurs only in dict2 then take the
          frequency from dict2
         The total frequencies = ALL is calculated by summing
         all frequencies in both dict1 and dict2.
        Return 1-(DIFF/ALL) rounded to 2 decimal places
    """
    diff_freq = 0
    all_freq = sum(freq_dict1.values())+sum(freq_dict2.values())
    
    for k,v in freq_dict1.items():
        if k in freq_dict2.keys():
            diff_freq += abs(v - freq_dict2[k])
        else:
            diff_freq += v
    for k,v in freq_dict2.items():
        if k not in freq_dict1.keys():
            diff_freq += v
    sim_score = 1 - (diff_freq / all_freq) 
    return round(sim_score, 2)


### Problem 4: Most Frequent Word(s) ###
def get_most_frequent_words(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary for one text
        freq_dict2: frequency dictionary for another text
    Returns:
        list of the most frequent word(s) in the input dictionaries

    The most frequent word:
        * is based on the combined word frequencies across both dictionaries.
          If a word occurs in both dictionaries, consider the sum the
          freqencies as the combined word frequency.
        * need not be in both dictionaries, i.e it can be exclusively in
          dict1, dict2, or shared by dict1 and dict2.
    If multiple words are tied (i.e. share the same highest frequency),
    return an alphabetically ordered list of all these words.
    """
    combined_dict = freq_dict1.copy() #adding dicts together, seperation not impoprtant
    for k,v in freq_dict2.items():
        if k in combined_dict.keys():
            combined_dict[k] += v
        else:
            combined_dict[k] = v
    max_freq = max(combined_dict.values()) # find most frequent word/s value
    most_freq_list = [] # new list to house most freequent words in dictionaires
    for k,v in combined_dict.items():
        if v == max_freq: # if the value is equaal to the found max
            most_freq_list.append(k) # add it to the return list

    return sorted(most_freq_list)


### Problem 5: Finding TF-IDF ###
def get_tf(file_path):
    """
    Args:
        file_path: name of file in the form of a string
    Returns:
        a dictionary mapping each word to its TF

    * TF is calculatd as TF(i) = (number times word *i* appears
        in the document) / (total number of words in the document)
    * Think about how we can use get_frequencies from earlier
    """
    input_string = load_file(file_path) 
    input_list = text_to_list(input_string)
    new_dict = get_frequencies(input_list)
    
    for k,v in new_dict.items():
        new_dict[k] = v / len(input_list)
    return new_dict

def get_idf(file_paths):
    """
    Args:
        file_paths: list of names of files, where each file name is a string
    Returns:
       a dictionary mapping each word to its IDF

    * IDF is calculated as IDF(i) = log_10(total number of documents / number of
    documents with word *i* in it), where log_10 is log base 10 and can be called
    with math.log10()

    """
    input_strings = [] # create new list to house raw file inputs
    input_lists = [] # list to house individual document word lists
    combined_list = [] # to save all words together
    for i in range(len(file_paths)): # loop through all files
        input_strings.append(load_file(file_paths[i])) # add them to the input list
        input_lists.append(text_to_list(input_strings[i])) # convets strings to lists
        combined_list += input_lists[i]
        
    new_dict = get_frequencies(combined_list)
    for key in new_dict:
        appeared_in_docs = 0
        for doc in range(len(input_lists)):
            if key in input_lists[doc]:
                appeared_in_docs += 1
        new_dict[key] = math.log10(len(file_paths)/appeared_in_docs)
    return new_dict

def get_tfidf(tf_file_path, idf_file_paths):
    """
        Args:
            tf_file_path: name of file in the form of a string (used to calculate TF)
            idf_file_paths: list of names of files, where each file name is a string
            (used to calculate IDF)
        Returns:
           a sorted list of tuples (in increasing TF-IDF score), where each tuple is
           of the form (word, TF-IDF). In case of words with the same TF-IDF, the
           words should be sorted in increasing alphabetical order.

        * TF-IDF(i) = TF(i) * IDF(i)
        """
    tf_input_dict = get_tf(tf_file_path)
    idf_input_dict = get_idf(idf_file_paths)
    final_score = []
    for key in tf_input_dict:
        if key in idf_input_dict.keys():
            final_score.append((key,(tf_input_dict[key]*idf_input_dict[key])))
    
    return sorted(sorted(final_score), key=lambda tup: tup[1])


if __name__ == "__main__":
    pass
    ###############################################################
    ## Uncomment the following lines to test your implementation ##
    ###############################################################

    # #Tests Problem 0: Prep Data
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # print(world)      # should print ['hello', 'world', 'hello']
    # print(friend)     # should print ['hello', 'friends']

    # # Tests Problem 1: Get Frequencies
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # world_word_freq = get_frequencies(world)
    # friend_word_freq = get_frequencies(friend)
    # print(world_word_freq)    # should print {'hello': 2, 'world': 1}
    # print(friend_word_freq)   # should print {'hello': 1, 'friends': 1}

    # # Tests Problem 2: Get Letter Frequencies
    # freq1 = get_letter_frequencies('hello')
    # freq2 = get_letter_frequencies('that')
    # print(freq1)      #  should print {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    # print(freq2)      #  should print {'t': 2, 'h': 1, 'a': 1}

    # # Tests Problem 3: Similarity
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # world_word_freq = get_frequencies(world)
    # friend_word_freq = get_frequencies(friend)
    # word1_freq = get_letter_frequencies('toes')
    # word2_freq = get_letter_frequencies('that')
    # word3_freq = get_frequencies('nah')
    # word_similarity1 = calculate_similarity_score(word1_freq, word1_freq)
    # word_similarity2 = calculate_similarity_score(word1_freq, word2_freq)
    # word_similarity3 = calculate_similarity_score(word1_freq, word3_freq)
    # word_similarity4 = calculate_similarity_score(world_word_freq, friend_word_freq)
    # print(word_similarity1)       # should print 1.0
    # print(word_similarity2)       # should print 0.25
    # print(word_similarity3)       # should print 0.0
    # print(word_similarity4)       # should print 0.4

    # # Tests Problem 4: Most Frequent Word(s)
    # freq_dict1, freq_dict2 = {"hello": 5, "world": 1}, {"hello": 1, "world": 5}
    # most_frequent = get_most_frequent_words(freq_dict1, freq_dict2)
    # print(most_frequent)      # should print ["hello", "world"]

    # Tests Problem 5: Find TF-IDF
    # tf_text_file = 'tests/student_tests/hello_world.txt'
    # idf_text_files = ['tests/student_tests/hello_world.txt', 'tests/student_tests/hello_friends.txt']
    # tf = get_tf(tf_text_file)
    # idf = get_idf(idf_text_files)
    # tf_idf = get_tfidf(tf_text_file, idf_text_files)
    # print(tf)     # should print {'hello': 0.6666666666666666, 'world': 0.3333333333333333}
    # print(idf)    # should print {'hello': 0.0, 'world': 0.3010299956639812, 'friends': 0.3010299956639812}
    # print(tf_idf) # should print [('hello', 0.0), ('world', 0.10034333188799373)]

    