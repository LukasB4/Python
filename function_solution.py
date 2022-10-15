def main():
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    reps = int(input("Enter number of times to divide it: "))

    div_n_times(numerator, denominator, reps)

def div_n_times(numerator, denominator, reps):
    print("Dividing ", numerator)
    for i in range(reps):
        numerator = numerator / denominator
        print(numerator)
main()
