# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Lab 2: Season Checker
# Lukas Bernard
# Last Modified: September 2, 2020 
# ---------------------------------------
# A brief overview of the program.
# ---------------------------------------

def main():
    user_month = input("Enter month: ")
    user_day = int(input("Enter day: "))
    season = season_checker(user_month, user_day)
    print("That's a %s day." %season)

def season_checker(user_month, user_day):
    p = 0
    while p != 1:
        if (user_month == 'March' or user_month == 'march') and (1 <= user_day <= 19):
            season = 'Winter'
            p = 1
        elif (user_month == 'March' or user_month == 'march') and (20 <= user_day <= 31):
            season = 'Spring'
            p = 1
        elif (user_month == 'April' or user_month == 'april') and (1 <= user_day <= 30):
            season = 'Spring'
            p = 1
        elif (user_month == 'May' or user_month == 'may') and (1 <= user_day <= 31):
            season = 'Spring'
            p = 1
        elif (user_month == 'June' or user_month == 'june') and (1 <= user_day <= 20):
            season = 'Spring'
            p = 1
        elif (user_month == 'June' or user_month == 'june') and (21 <= user_day <= 30):
            season = 'Summer'
            p = 1
        elif (user_month == 'July' or user_month == 'july') and (1 <= user_day <= 31):
            season = 'Summer'
            p = 1
        elif (user_month == 'August' or user_month == 'august') and (1 <= user_day <= 31):
            season = 'Summer'
            p = 1
        elif (user_month == 'September' or user_month == 'september') and (1 <= user_day <= 21):
            season = 'Summer'
            p = 1
        elif (user_month == 'September' or user_month == 'september') and (22 <= user_day <= 30):
            season = 'Fall'
            p = 1
        elif (user_month == 'October' or user_month == 'october') and  (1<= user_day <= 31):
            season = 'Fall'
            p = 1
        elif (user_month == 'November' or user_month == 'november') and (1 <= user_day <= 30):
            season = 'Fall'
            p = 1
        elif (user_month == 'December' or user_month == 'december') and (1 <= user_day <= 20):
            season = 'Fall'
            p = 1
        elif (user_month == 'December' or user_month == 'december') and (21 <= user_day <= 31):
            season = 'Winter'
            p = 1
        elif (user_month == 'January' or user_month == 'january') and (1 <= user_day <= 31):
            season = 'Winter'
            p = 1
        elif (user_month == 'February' or user_month == 'february') and (1 <= user_day <= 29):
            season = 'Winter'
            p = 1
        else:
            print("That's an unrecognized date.")
            user_month = input("Enter month: ")
            user_day = int(input("Enter day: "))
    return season


            
main()
