def main():
    sentence = input("Enter a sentence: ")
    sentence = capitalization_punctuation(sentence)
    second_last(sentence)

def capitalization_punctuation(sentence):
    punctuation = ".,!?;-'\""
    return_Value = ''
    for character in sentence:
        if character not in punctuation:
            return_Value += character
    return_Value = return_Value.upper()

    return return_Value

def second_last(sentence):
    sentence = sentence.split()
    print("second word: ", sentence[1])
    print("last word: ", sentence[-1])
    
main()
