# -----------------------------------------+
# CSCI 127, Joy and Beauty of Data         |
# Program 3: Classics CSV Library          |
# Lukas Bernard                            |
# Last Modified: ??, 2020                  |
# -----------------------------------------+
# Provide a brief overview of the program. |
# -----------------------------------------+
import csv

# -----------------------------------------+
# Do not change anything below this line   |
# with the exception of code related to    |
# option 4.                                |
# -----------------------------------------+

# -----------------------------------------+
# menu                                     |
# -----------------------------------------+
# Prints a menu of options for the user.   |
# -----------------------------------------+

import operator
import collections

def menu():
    print()
    print("1. Identify the longest book by word count.")
    print("2. List a range of books by difficulty rating.")
    print("3. Identify all books by certain author.")
    print("4. Something interesting, non-trivial and not a variation of the above options.")
    print("5. Quit.")
    print()

def longest(input_file):
    data = open(input_file, "r", encoding = "ISO-8859-1")
    books = {}
    for row in data:
        the_dict = row.split(',')
        the_dict[-1] = the_dict[-1].strip()
        books[the_dict[-1]] = the_dict[3]
    del books['metrics.statistics.words']
    wordNumbers = list (books.keys())
    for i in range(0, len(wordNumbers)):
        wordNumbers[i] = int(wordNumbers[i])
    wordNumbers.sort(reverse=True)
    wordNumbers[0] = str(wordNumbers[0])
    print("The longest book is", books[wordNumbers[0]])
                     
def fk_difficulty_range(input_file, least, most):
    least = int(least)
    most = int(most)
    data = open(input_file, "r", encoding = "ISO-8859-1")
    books = {}
    document = data.readlines()[1:]
    for row in document:
        groups = row.split(',')
        books[groups[3]] = [float(groups[-15])]
    finaldict = collections.OrderedDict(sorted(books.items(), key = operator.itemgetter(1)))
    for piece in finaldict:
        totnum = list(finaldict.keys()).index(piece)
        if (totnum <= most) and (totnum >= least):
            print(totnum,"-", piece, "-", finaldict[piece])
        
def all_books_by_author(input_file, author):
    data = open(input_file, "r", encoding = "ISO-8859-1")
    lister = data.readlines()[1:]
    
    for row in lister:
        group = row.split(',')
        authorcombo = group[11].split(';')
        
        for value in authorcombo:
            if value == author:
                print(group[3], "by", authorcombo[1], authorcombo[0])
        
def common_month(input_file):
    data = open(input_file, "r", encoding = "ISO-8859-1")
    lister = data.readlines()[1:]
    monthlist = []
    counter = 0
    for row in lister:
        group = row.split(',')
        monthlist.append(group[15])
    number = monthlist[0]
    for i in monthlist:
        current = monthlist.count(i)
        if(current > counter):
            counter = current
            number = i
    print("The most common publishing month is: ", number)
            
    
# -----------------------------------------+
# main                                     |
# -----------------------------------------+
# Repeatedly query the user for options.   |
# -----------------------------------------+

def main():
    input_file = "classics.csv"
    choice = 0
    while (choice != 5):
        menu()
        choice = int(input("Enter your choice: "))
        print()
        if (choice == 1):
            longest(input_file)
        elif (choice == 2):
            least = input("Enter least difficult out of 1000 (e.g. 250): ")
            most = input("Enter most difficult out of 1000 (e.g. 300): ")
            print("Using the Flesch–Kincaid grade level formula.")
            fk_difficulty_range(input_file, least, most)
        elif (choice == 3):
            author = input("Enter last name of author (e.g. Dickens): ")
            all_books_by_author(input_file, author)
        elif (choice == 4):
            common_month(input_file)
        elif (choice != 5):
            print("That is not a valid option.  Please try again.")
    print("Goodbye!")

# -----------------------------------------+

main()
