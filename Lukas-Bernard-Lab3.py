# ---------------------------------------------
# CSCI 127, Lab 3                              |
# September 9, 2020                            |
# Lukas Bernard                                |
# --------------------------------------------- 
# Calculate how many bilabial consonents       |
# (letters that make your lips touch: b, m, p) |
# are in a sentence using two techniques.      |
# ---------------------------------------------

def count_built_in(sentence):

    bilabial = sentence.count("B") + sentence.count("b") + \
    sentence.count("M") + sentence.count("m") + \
    sentence.count("P") + sentence.count("p")
    
    return bilabial

def count_iterative(sentence):

    bilabial = 0

    for f in sentence:
        if f == 'b' or f == 'B' or f == 'm' or f == 'M' \
           or f == 'p' or f == 'P':
            bilabial += 1
        

    return bilabial

# --------------------------------------

def main():
    answer = "yes"
    while (answer == "yes") or (answer == "y"):
        sentence = input("Please enter a sentence: ")
        sentence = sentence.lower()
        print()
        print("Counting bilabial consonents  using ...")
        print("---------------------------------------")
        print("Built-in function =", count_built_in(sentence))
        print("Iteration =", count_iterative(sentence))
        print()
        answer = input("Would you like to continue: ").lower()
        print()

# --------------------------------------

main()
