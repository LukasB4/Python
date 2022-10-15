import string
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------
# CSCI 127, Lab 12                                |
# November 18, 2020                               |
# Lukas Bernard                                   |
# -------------------------------------------------

def my_chart(file_name, data):
    # TODO: 1. define this function to plot any interesting data from both example files
    #       2. document your code using docstrings as shown in the example functions below
    letters = list(string.ascii_uppercase)  
    numbers = list(range(0, 17))
    fields = dict(zip(letters, numbers))
    
    df = pd.read_csv(file_name)
    cols = list(df.columns)
    print("cols", cols)
    title = file_name[:-3]
    
    col = cols[fields[data]]
    slices = df[col].value_counts() # a pandas Series
    print(slices)
    df[col].value_counts().plot.pie(labels=slices.keys(), autopct='%1.1f%%', title=title,)
    
    plt.show()    
def count_fields_piechart(file_name, data):
    '''
    Plots a pie chart with percentages of same data field entries

        Parameters:
            file_name (str): The name and .csv extension of CSV file
            data (str): A capital letter designating spreadsheet column

        Returns:
            None
    '''
    
    letters = list(string.ascii_uppercase)  
    numbers = list(range(0, 26))
    fields = dict(zip(letters, numbers))
    
    df = pd.read_csv(file_name)
    cols = list(df.columns)
    title = file_name[:-3]
    
    col = cols[fields[data]]
    
    slices = df[col].value_counts()     # a pandas Series
    df[col].value_counts().plot.pie(labels=slices.keys(), autopct='%1.1f%%', title=title,)
    
    plt.show()
    
def square_barchart(file_name, horiz, vert):
    '''
    Plots a value sorted 1:1 bar chart of a data series with the horiz entries the along
    the x axis, and the range of vert entries on the y axis

        Parameters:
            file_name (str): The name and .csv extension of CSV file
            horiz (str): A capital letter designating spreadsheet column
            vert (str): A capital letter designating spreadsheet column

        Returns:
            None
    '''   
    
    letters = list(string.ascii_uppercase)  
    numbers = list(range(0, 26))            
    fields = dict(zip(letters, numbers))
    
    df = pd.read_csv(file_name)
    cols = list(df.columns) 
    title = file_name[:-3]
    
    x_axis = cols[fields[horiz]] 
    y_axis = cols[fields[vert]]
    df = df.sort_values(y_axis, ascending=False)
    
    df.plot(title=title, legend=False, x=x_axis, y=y_axis, kind="bar")

    plt.xlabel(x_axis)
    plt.ylabel(y_axis) 
    plt.show() 

# -------------------------------------------------

# Calls to example functions demonstrating usage:
#square_barchart("CS Classes F20.csv", 'A', 'B')
#square_barchart("CS Faculty F20.csv", 'A', 'B')
#count_fields_piechart("CS Classes F20.csv", "C")
my_chart("CS Faculty F20.csv", "B")
my_chart("Cs Classes F20.csv", "B")

# TODO: Comment out the three function calls above, and replace with
#       two calls to demo your function
