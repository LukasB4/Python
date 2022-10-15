# -----------------------------------------------------
# CSCI 127, Lab 9                                     |
# October 21, 2020                                    |
# Lukas Bernard                                       |
# -----------------------------------------------------

# Your solution goes here.  Do not change anything below.
class Stack:
    
    def __init__(self):
        self.items = []
        
    def push(self, num):
        self.items.append(num)

    def pop(self):
        return self.items.pop(-1)

    def __str__(self):
        s = ' '
        for item in self.items:
            item = str(item)
            s += " " + item
        return "Contents:" + s
    
    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def __iadd__ (self, other):
        
        self.items.append(other)
        return self.__str__()
# -----------------------------------------------------

def main():
    numbers = Stack()

    print("Push 1, 2, 3, 4, 5")
    print("---------------------")
    for number in range(1, 6):
        numbers.push(float(number))
        print(numbers)

    print("\nPop one item")
    print("----------------")
    numbers.pop()
    print(numbers)

    print("\nPop all items")
    print("---------------")
    while not numbers.is_empty():
        print("Item popped:", numbers.pop())
        print(numbers)

    # Push 10, 11, 12, 13, 14
    for number in range(10, 15):
        numbers.push(number)

    # Push 15
    numbers += 15 # See: https://www.python-course.eu/python3_magic_methods.php
    print("\nPushed: 10, 11, 12, 13, 14, 15")
    print("-------------------------------")
    print(numbers)

# -----------------------------------------------------

main()
