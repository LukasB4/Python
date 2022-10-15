# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Lab 4
# Lukas Bernard
# Last Modified: September 16, 2020 
# ---------------------------------------
# This program converts a string to
# lowercase, then counts the iterations
# of each word throughout iteratively
# and recursively
# ---------------------------------------

def main():
    user_input = input("Enter words: ")
    words = make_word_list(user_input)
    print("Iterative Count:")
    count_freq_iteratively(words)

    words.sort()
    print("Recursive Count:")
    count_freq_recursively(words)


def make_word_list(user_input):
    punctuation = ".,!?;-'\""
    return_value = ""
    
    for character in user_input:
        if character not in punctuation:
            return_value += character
            
    return_value = return_value.lower()
            
    return return_value.split()

def count_freq_iteratively(words):
    checkedwords = ""

    for word in words:
        if word not in checkedwords:
            count = words.count(word)
            print(word, count)
            checkedwords += word

def count_freq_recursively(words):
    if len(words) != 0:
        count = words.count(words[0])
        print(words[0], count)
        wordtoremove = words[0]
        
        while(wordtoremove in words):
            words.remove(wordtoremove)
  
        count_freq_recursively(words)
        
            
main()
