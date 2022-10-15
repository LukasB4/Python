# --------------------------------------
# CSCI 127, Lab 5                      |
# September 22, 2020                   |
# Lukas Bernard                        |
# --------------------------------------

def main(file_name):
    magnitude = average_magnitude(file_name)
    print("The average earthquake magnitude is {:.2f}\n".format(magnitude))
    
    earthquake_locations(file_name)
    
    lower_bound = float(input("Enter a lower bound for the magnitude: "))
    upper_bound = float(input("Enter an upper bound for the magnitude: "))
    how_many = count_earthquakes(file_name, lower_bound, upper_bound)
    print("Number of recorded earthquakes between {:.2f} and {:.2f} = {:d}".format(lower_bound, upper_bound, how_many))
    
def average_magnitude(file_name):
    fin = open(file_name, 'r')
    avmag = 0
    totmag = 0
    totnum = 0
    fin.readline()
    for line in fin:
        items = line.split(',')
        totmag += float(items[-8])
        totnum += 1
    avmag = totmag/totnum
    return avmag

def earthquake_locations(file_name):
    print("Alphabetical Order of Earthquake Locations")
    print("------------------------------------------")
    fin = open(file_name, 'r')
    listed = []
    finallisted = []
    lina = 1
    fin.readline()
    for line in fin:
        items = line.split(',')
        listed.append(items[-5])
    finallisted = list(set(listed))
    finallisted.sort()
    for i, item in enumerate(finallisted,1):
        print(i, '. ' + item, sep='',end=''"\n")
    print("")
    pass

def count_earthquakes(file_name, lower_bound, upper_bound):
    fin = open(file_name, 'r')
    listed = []
    listed2 = []
    fin.readline()
    for line in fin:
        items = line.split(",")
        listed.append(items[-8])
    for line in listed:
        listed2.append(float(line))
    count = len([elem for elem in listed2 if lower_bound <= elem <= upper_bound])
    
    return count
    
        
# --------------------------------------

main("earthquakes.csv")
