# --------------------------------------
# CSCI 127, Lab 7                      |
# October 7, 2020                      |
# Lukas Bernard                        |
# --------------------------------------

def create_dictionary(file_name):
    filein = open(file_name, 'r')
    my_dict = {}
    for line in filein:
        the_dict = line.split(',')
        the_dict[-1] = the_dict[-1].strip()
        my_dict[the_dict[1]] = the_dict[0]
    my_dict[' '] = my_dict["space"]
    my_dict['\"'] = my_dict['quote']
    my_dict[','] = my_dict['comma']
    del my_dict['comma']
    del my_dict['space']
    del my_dict['quote']

    return my_dict

def translate(sentence, dictionary, sentinput):
    characterlist = list(sentence)
    
    for character in characterlist:
        if character in dictionary.keys():
            print(dictionary[character], "      ", character)
        else:
            print("UNDEFINED      ", character )
        
# --------------------------------------
def main():
    dictionary = create_dictionary("ascii-codes.csv")
    sentence = "A long time ago in a galaxy far, far away..."
    translate(sentence, dictionary, "output-1.txt")
    sentence = "Montana State University (406) 994-0211"
    translate(sentence, dictionary, "output-2.txt")
    sentence = "“True friends stab you in the front.” —Wilde"
    translate(sentence, dictionary, "output-3.txt")

# --------------------------------------

main()
